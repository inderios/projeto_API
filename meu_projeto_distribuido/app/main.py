# app/main.py
import os
import socket
from time import sleep
from contextlib import asynccontextmanager
from decimal import Decimal
from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import create_engine, String, Numeric
from sqlalchemy.orm import sessionmaker, Session, declarative_base, Mapped, mapped_column

# --- CONFIGURAÇÃO DO BANCO DE DADOS ---
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise ValueError("A variável de ambiente DATABASE_URL não foi definida.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- MODELO DO BANCO (SQLAlchemy) ---
class Mercadoria(Base):
    __tablename__ = "mercadorias"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String, index=True)
    preco: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    descricao: Mapped[str] = mapped_column(String)

# --- SCHEMAS DA API (Pydantic) ---

# Schema para criar ou atualizar uma mercadoria (não inclui o ID)
class MercadoriaCreateUpdateSchema(BaseModel):
    nome: str
    preco: Decimal
    descricao: str

# Schema para exibir uma mercadoria na resposta (inclui o ID)
class MercadoriaSchema(MercadoriaCreateUpdateSchema):
    id: int

    class Config:
        from_attributes = True

# Schema para a resposta da lista de mercadorias
class MercadoriasResponse(BaseModel):
    mercadorias: List[MercadoriaSchema]
    servidor_que_respondeu: str

# --- LÓGICA DE INICIALIZAÇÃO ---
def create_db_and_tables():
    # Esta função agora é chamada apenas uma vez no início da aplicação
    sleep(5)
    try:
        Base.metadata.create_all(bind=engine)
        print("Tabelas criadas com sucesso (ou já existentes).")
        db = SessionLocal()
        if db.query(Mercadoria).count() == 0:
            print("Populando banco de dados com dados de exemplo...")
            db.add_all([
                Mercadoria(nome="Laptop Gamer", preco=Decimal("7500.50"), descricao="Notebook com placa de vídeo dedicada."),
                Mercadoria(nome="Mouse sem Fio", preco=Decimal("120.00"), descricao="Mouse ergonômico com 6 botões."),
                Mercadoria(nome="Teclado Mecânico", preco=Decimal("350.75"), descricao="Teclado com switches blue e RGB.")
            ])
            db.commit()
            print("Dados inseridos.")
        db.close()
    except Exception as e:
        print(f"Erro ao criar/popular tabelas: {e}")

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando a aplicação e criando tabelas...")
    create_db_and_tables()
    yield
    print("Finalizando a aplicação.")

# --- APLICAÇÃO FASTAPI ---
app = FastAPI(lifespan=lifespan)
hostname = socket.gethostname()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ENDPOINTS DA API (CRUD) ---

# CREATE - Criar uma nova mercadoria
@app.post("/mercadorias/", response_model=MercadoriaSchema, status_code=status.HTTP_201_CREATED)
def create_mercadoria(mercadoria: MercadoriaCreateUpdateSchema, db: Session = Depends(get_db)):
    db_mercadoria = Mercadoria(**mercadoria.model_dump())
    db.add(db_mercadoria)
    db.commit()
    db.refresh(db_mercadoria)
    return db_mercadoria

# READ (All) - Ler todas as mercadorias
# Esta é a única função para o endpoint GET /mercadorias/
@app.get("/mercadorias/", response_model=MercadoriasResponse)
def read_all_mercadorias(db: Session = Depends(get_db)):
    mercadorias_db = db.query(Mercadoria).all()
    return {
        "mercadorias": mercadorias_db,
        "servidor_que_respondeu": hostname
    }

# READ (One) - Ler uma mercadoria específica
@app.get("/mercadorias/{mercadoria_id}", response_model=MercadoriaSchema)
def read_one_mercadoria(mercadoria_id: int, db: Session = Depends(get_db)):
    db_mercadoria = db.query(Mercadoria).filter(Mercadoria.id == mercadoria_id).first()
    if db_mercadoria is None:
        raise HTTPException(status_code=404, detail="Mercadoria não encontrada")
    return db_mercadoria

# UPDATE - Atualizar uma mercadoria
@app.put("/mercadorias/{mercadoria_id}", response_model=MercadoriaSchema)
def update_mercadoria(mercadoria_id: int, mercadoria: MercadoriaCreateUpdateSchema, db: Session = Depends(get_db)):
    db_mercadoria = db.query(Mercadoria).filter(Mercadoria.id == mercadoria_id).first()
    if db_mercadoria is None:
        raise HTTPException(status_code=404, detail="Mercadoria não encontrada")
    
    for key, value in mercadoria.model_dump().items():
        setattr(db_mercadoria, key, value)
        
    db.commit()
    db.refresh(db_mercadoria)
    return db_mercadoria

# DELETE - Apagar uma mercadoria
@app.delete("/mercadorias/{mercadoria_id}", status_code=status.HTTP_200_OK)
def delete_mercadoria(mercadoria_id: int, db: Session = Depends(get_db)):
    db_mercadoria = db.query(Mercadoria).filter(Mercadoria.id == mercadoria_id).first()
    if db_mercadoria is None:
        raise HTTPException(status_code=404, detail="Mercadoria não encontrada")
    
    db.delete(db_mercadoria)
    db.commit()
    return {"message": "Mercadoria removida com sucesso"}