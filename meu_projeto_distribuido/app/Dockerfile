# app/Dockerfile

# 1. Use uma imagem base oficial do Python
FROM python:3.10-slim

# 2. Defina o diretório de trabalho dentro do container
WORKDIR /code

# 3. Copie o arquivo de dependências para o diretório de trabalho
COPY ./requirements.txt /code/requirements.txt

# 4. Instale as dependências
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 5. Copie o código da aplicação para o diretório de trabalho
COPY . /code/

# 6. Exponha a porta que a aplicação vai rodar
EXPOSE 8000

# 7. Defina o comando para iniciar a aplicação quando o container rodar
#    --host 0.0.0.0 é crucial para que a aplicação seja acessível de fora do container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]