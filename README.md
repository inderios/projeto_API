API de Mercadorias - Um Sistema Distribuído de Alta Performance
Este projeto implementa uma API RESTful completa para um CRUD (Criar, Ler, Atualizar, Apagar) de mercadorias, construída sobre uma arquitetura de microsserviços moderna, escalável e otimizada para alta performance.

🌟 Funcionalidades e Teorias Implementadas
API RESTful Completa: CRUD completo para gestão de mercadorias.

Arquitetura Distribuída: O sistema é composto por múltiplos serviços independentes que comunicam através de uma rede.

Alta Disponibilidade e Escalabilidade Horizontal: Três réplicas do serviço de aplicação (API) são executadas em paralelo.

Balanceamento de Carga: Um Nginx atua como reverse proxy, distribuindo o tráfego de forma equitativa entre as instâncias da API.

Cache Distribuído: Um serviço de cache com Redis é utilizado para acelerar drasticamente as operações de leitura e reduzir a carga no banco de dados, implementando o padrão "Cache-Aside".

Persistência de Dados: Um banco de dados PostgreSQL serve como a fonte única da verdade para os dados.

Orquestração com Docker Compose: Todos os serviços (API, Nginx, PostgreSQL, Redis) são definidos e orquestrados para funcionar em conjunto com um único comando.

Diagrama da Arquitetura
🚀 Como Colocar para Funcionar
Siga as instruções abaixo para executar o projeto.

Pré-requisitos
Docker e Docker Compose instalados.

Python 3.10+ e pip instalados (apenas para os modos de desenvolvimento local).

Modo 1: Executar o Sistema Completo (Recomendado)
Este modo inicia todos os serviços (Nginx, 3x API, PostgreSQL, Redis) em conjunto. É a forma mais fácil e completa de executar o projeto.

Navegue para a pasta raiz do projeto no seu terminal.

cd /caminho/para/meu_projeto_distribuido

Execute o Docker Compose. O comando --build garante que as suas imagens são construídas com o código mais recente.

docker-compose up --build

Aceda à API. Após a inicialização, a API estará disponível no seu navegador em:

http://localhost/mercadorias/

Modo 2: Desenvolvimento Local da API (com Recarregamento Automático)
Este modo é ideal para quando você está a editar ativamente o código Python (main.py) e quer ver as alterações refletidas instantaneamente.

Inicie os serviços de que depende (Banco de Dados e Cache). No terminal, na pasta raiz, execute:

docker-compose up db cache

Abra um segundo terminal.

Navegue para a pasta da aplicação e ative o ambiente virtual.

# Navegue para a pasta
cd meu_projeto_distribuido/app

# Crie e ative o ambiente virtual (apenas na primeira vez)
python -m venv .venv
# No Windows (CMD): .\.venv\Scripts\activate
# No Windows (PowerShell): .\.venv\Scripts\Activate.ps1
# No Linux/macOS: source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

Inicie o servidor Uvicorn. O ficheiro .env na pasta app irá configurar a ligação ao banco de dados que está a ser executado no Docker.

uvicorn main:app --reload

A sua API estará agora a ser executada em http://localhost:8000.

Modo 3: Teste de Carga com Locust
Para simular milhares de utilizadores a aceder à sua API e testar a performance.

Garanta que o sistema completo está a ser executado (siga o Modo 1).

Abra um segundo terminal.

Navegue para a pasta raiz e ative um ambiente virtual (pode usar o mesmo da app ou criar um novo).

# Ative o ambiente virtual
# No Windows (CMD): .\app\.venv\Scripts\activate

# Instale o Locust
pip install locust

Inicie o Locust, apontando para o ficheiro de teste.

locust -f locustfile.py

Abra o seu navegador em http://localhost:8089, configure o número de utilizadores e o Host (http://localhost), e inicie o teste.
