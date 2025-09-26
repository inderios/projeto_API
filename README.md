
# Projeto API Distribuída com FastAPI, Nginx e PostgreSQL

Este projeto demonstra a implementação de uma API RESTful distribuída utilizando FastAPI, com um balanceador de carga Nginx e um banco de dados PostgreSQL, tudo orquestrado com Docker Compose.

## Arquitetura

A arquitetura da aplicação é composta pelos seguintes serviços:

* **FastAPI (`app`)**: Três réplicas da aplicação principal que fornecem os endpoints da API para operações CRUD (Criar, Ler, Atualizar, Apagar) de mercadorias. A aplicação utiliza SQLAlchemy para interagir com o banco de dados.
* **PostgreSQL (`db`)**: O banco de dados relacional que persiste os dados das mercadorias. Utiliza a imagem oficial `postgres:13-alpine` e armazena os dados em um volume para garantir a persistência.
* **Nginx (`nginx`)**: Atua como um balanceador de carga (load balancer), distribuindo as requisições recebidas na porta 80 entre as três instâncias do serviço da aplicação FastAPI.

## Funcionalidades

A API permite gerenciar um cadastro de mercadorias, suportando as seguintes operações:

* **Criar** uma nova mercadoria.
* **Listar** todas as mercadorias cadastradas.
* **Obter** os detalhes de uma mercadoria específica pelo seu ID.
* **Atualizar** as informações de uma mercadoria existente.
* **Apagar** uma mercadoria do banco de dados.

## Como Executar o Projeto

### Pré-requisitos

* Docker
* Docker Compose

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_DIRETORIO>
    ```

2.  **Suba os containers:**
    No diretório `meu_projeto_distribuido`, execute o seguinte comando para construir as imagens e iniciar os serviços em background:
    ```bash
    docker-compose up -d --build
    ```
    Este comando irá:
    * Construir a imagem para a aplicação FastAPI a partir do `app/Dockerfile`.
    * Construir a imagem para o Nginx a partir do `nginx/Dockerfile`.
    * Baixar a imagem do PostgreSQL.
    * Iniciar os containers para os serviços `db`, `app` (com 3 réplicas) e `nginx`.

3.  **Acesse a API:**
    A API estará acessível através do Nginx na URL: `http://localhost/mercadorias/`

## Endpoints da API

A seguir estão os endpoints disponíveis na API:

| Método | Rota                          | Descrição                                                                      |
| :----- | :---------------------------- | :----------------------------------------------------------------------------- |
| `POST` | `/mercadorias/`               | Cria uma nova mercadoria no banco de dados.                                    |
| `GET`  | `/mercadorias/`               | Retorna uma lista com todas as mercadorias e o nome do servidor que atendeu à requisição. |
| `GET`  | `/mercadorias/{mercadoria_id}` | Retorna os detalhes de uma mercadoria específica.                              |
| `PUT`  | `/mercadorias/{mercadoria_id}` | Atualiza os dados de uma mercadoria existente.                                 |
| `DELETE`| `/mercadorias/{mercadoria_id}` | Remove uma mercadoria do banco de dados.                                       |

## Teste de Carga com Locust

O projeto inclui um arquivo `locustfile.py` para realizar testes de carga na API, simulando o comportamento de um usuário que realiza operações CRUD.

### Como Executar os Testes

1.  **Instale o Locust:**
    ```bash
    pip install locust
    ```

2.  **Execute o Locust:**
    A partir do diretório raiz do projeto, execute o comando abaixo, apontando para o host onde a aplicação está rodando (o Nginx, neste caso).
    ```bash
    locust -f meu_projeto_distribuido/locustfile.py --host=http://localhost
    ```

3.  **Acesse a interface web do Locust:**
    Abra o seu navegador e acesse `http://localhost:8089`. Configure o número de usuários e a taxa de eclosão (spawn rate) para iniciar os testes.

## Tecnologias Utilizadas

* **Backend**: FastAPI, Uvicorn
* **Banco de Dados**: PostgreSQL, SQLAlchemy, Psycopg2
* **Containerização**: Docker, Docker Compose
* **Balanceador de Carga**: Nginx
* **Teste de Carga**: Locust
