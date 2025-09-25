import random
from locust import HttpUser, task, between, events

class APICRUDUser(HttpUser):
    """
    Utilizador virtual que realiza um ciclo completo de operações CRUD.
    """
    wait_time = between(1, 3)  # Espera entre 1 a 3 segundos entre as tarefas
    mercadoria_id = None

    def on_start(self):
        """
        Isto é executado quando um utilizador virtual é iniciado.
        Vamos criar uma nova mercadoria para cada utilizador.
        """
        # Dados para a nova mercadoria. Usamos random para evitar dados duplicados.
        novo_produto = {
            "nome": f"Produto de Teste {random.randint(1, 10000)}",
            "preco": round(random.uniform(10.0, 500.0), 2),
            "descricao": "Criado pelo teste de carga do Locust."
        }
        
        with self.client.post("/mercadorias/", json=novo_produto, name="/mercadorias/ [CRIAR]", catch_response=True) as response:
            if response.status_code == 201:
                # Se o produto foi criado com sucesso, guardamos o ID
                self.mercadoria_id = response.json()["id"]
                response.success()
            else:
                response.failure(f"Falha ao criar mercadoria. Status: {response.status_code}")

    @task(10) # Esta tarefa será executada 10 vezes mais que as outras
    def ler_todas_mercadorias(self):
        self.client.get("/mercadorias/", name="/mercadorias/ [LER TODOS]")

    @task(5) # Esta tarefa tem um peso médio
    def ler_uma_mercadoria(self):
        if self.mercadoria_id:
            self.client.get(f"/mercadorias/{self.mercadoria_id}", name="/mercadorias/{id} [LER UM]")

    @task(3) # Esta tarefa é menos frequente
    def atualizar_mercadoria(self):
        if self.mercadoria_id:
            dados_atualizados = {
                "nome": f"Produto Atualizado {self.mercadoria_id}",
                "preco": round(random.uniform(20.0, 600.0), 2),
                "descricao": "Este produto foi atualizado pelo Locust."
            }
            self.client.put(f"/mercadorias/{self.mercadoria_id}", json=dados_atualizados, name="/mercadorias/{id} [ATUALIZAR]")

    def on_stop(self):
        """
        Isto é executado quando um utilizador virtual é parado (no fim do teste).
        Vamos apagar a mercadoria que criámos.
        """
        if self.mercadoria_id:
            self.client.delete(f"/mercadorias/{self.mercadoria_id}", name="/mercadorias/{id} [APAGAR]")
