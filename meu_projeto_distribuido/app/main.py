# app/main.py
import os
import socket
from time import sleep
imp
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

# 1. CONFIGURAÇÃO DO BANCO DE DADOS
# Pega a URL de conexão da variável de ambiente que definimos no docker-compose.yml
DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy Engine
# O 'connect_args' é uma boa prática para certas configurações de DB.
engine = create_engine(DATABASE_URL)

# Sessão para interagir com o DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos ORM (nossas tabelas)
Base = declarative_base()

# 2. MODELO DA TABELA DE MERCADORIAS
class Mercadoria(Base):
    __tablename__ = "mercadorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    preco = Column(Float)
    descricao = Column(String)

# 3. LÓGICA PARA CRIAR A TABELA E POPULAR DADOS (para demonstração)
def create_db_and_tables():
    # Uma pequena espera para garantir que o DB está 100% pronto
    sleep(5) 
    try:
        Base.metadata.create_all(bind=engine)
        print("Tabelas criadas com sucesso (ou já existentes).")
        
        db = SessionLocal()
        if db.query(Mercadoria).count() == 0:
            print("Populando banco de dados com dados de exemplo...")
            db.add_all([
                Mercadoria(nome="Laptop Gamer", preco=7500.50, descricao="Notebook com placa de vídeo dedicada."),
                Mercadoria(nome="Mouse sem Fio", preco=120.00, descricao="Mouse ergonômico com 6 botões."),
                Mercadoria(nome="Teclado Mecânico", preco=350.75, descricao="Teclado com switches blue e RGB.")
            ])
            db.commit()
            print("Dados inseridos.")
        db.close()
    except Exception as e:
        print("Erro ao criar/popular tabelas:", e)


# 4. APLICAÇÃO FASTAPI
app = FastAPI()

# Pega o hostname do container para sabermos qual instância respondeu
hostname = socket.gethostname()

# Evento que roda quando a aplicação inicia
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Dependência para obter a sessão do banco de dados em cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 5. ENDPOINTS DA API
@app.get("/")
def read_root():
    return {
        "message": "Serviço de Mercadorias no ar!",
        "hostname_servidor": hostname
    }

@app.get("/mercadorias/")
def get_mercadorias(db: Session = Depends(get_db)):
    """
    Este endpoint pega todos os dados de mercadorias do banco de dados PostgreSQL.
    """
    mercadorias = db.query(Mercadoria).all()
    return {
        "mercadorias": mercadorias,
        "servidor_que_respondeu": hostname
    }