<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guia Interativo | API de Mercadorias Distribuída</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {
            --bg-main: #F8F7F4;
            --bg-secondary: #EAE7DC;
            --text-primary: #44403c;
            --text-secondary: #78716c;
            --accent: #4338ca;
            --accent-light: #6366f1;
            --border-color: #d6d3d1;
        }
        body {
            background-color: var(--bg-main);
            color: var(--text-primary);
            font-family: 'Inter', sans-serif;
        }
        .nav-link {
            transition: all 0.2s ease-in-out;
            border-bottom: 2px solid transparent;
        }
        .nav-link.active {
            border-bottom-color: var(--accent);
            color: var(--accent);
            font-weight: 600;
        }
        .nav-link:hover {
            color: var(--accent-light);
        }
        .content-section {
            display: none;
        }
        .content-section.active {
            display: block;
        }
        .code-block {
            background-color: #f3f4f6;
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
            position: relative;
        }
        .copy-button {
            position: absolute;
            top: 0.75rem;
            right: 0.75rem;
            background-color: var(--bg-secondary);
            color: var(--text-secondary);
            border: 1px solid var(--border-color);
            padding: 0.25rem 0.5rem;
            border-radius: 0.25rem;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .copy-button:hover {
            background-color: #d1d5db;
            color: var(--text-primary);
        }
        .diagram-component {
            border: 2px solid var(--border-color);
            transition: all 0.3s ease-in-out;
            cursor: pointer;
        }
        .diagram-component:hover, .diagram-component.highlighted {
            border-color: var(--accent);
            transform: translateY(-4px);
            box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            height: 40vh;
            max-height: 400px;
        }
    </style>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- Chosen Palette: Serene Dev -->
    <!-- Application Structure Plan: A SPA with tab-based navigation is chosen for its clarity and common use, preventing long scrolling. The structure is thematic: 1. Visão Geral (an interactive architecture diagram for immediate context), 2. Arquitetura (deep dive into code for each component), 3. Como Executar (practical, task-oriented instructions), and 4. Performance (visual proof of the project's success). This non-linear structure allows different users (managers, developers) to access information in the order most relevant to them, prioritizing usability over mirroring the project's file structure. -->
    <!-- Visualization & Content Choices: Architecture -> Goal:Organize -> Viz:Interactive HTML/CSS Diagram -> Interaction:Click to highlight & get info -> Justification:Visually intuitive, encourages exploration -> Method:Vanilla JS + Tailwind. Code Files -> Goal:Inform -> Viz:Styled Code Blocks -> Interaction:Copy-to-clipboard -> Justification:Developer usability -> Method:Vanilla JS. Performance -> Goal:Compare/Impact -> Viz:Chart.js Bar Chart -> Interaction:Static visualization of before/after caching -> Justification:Clearly shows quantitative improvement, adds "wow" factor -> Library:Chart.js. -->
    <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
</head>
<body class="antialiased">

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 md:py-12">
        <header class="text-center mb-10 md:mb-16">
            <h1 class="text-4xl md:text-5xl font-bold tracking-tight text-stone-900">API de Mercadorias Distribuída</h1>
            <p class="mt-4 text-lg md:text-xl text-stone-600 max-w-3xl mx-auto">Um guia interativo para a arquitetura, execução e performance de um sistema de microsserviços de alta performance.</p>
        </header>

        <nav class="flex justify-center border-b border-stone-300 mb-8">
            <button data-tab="overview" class="nav-link py-3 px-4 md:px-6 text-sm md:text-base font-medium text-stone-600">Visão Geral</button>
            <button data-tab="architecture" class="nav-link py-3 px-4 md:px-6 text-sm md:text-base font-medium text-stone-600">Arquitetura</button>
            <button data-tab="run" class="nav-link py-3 px-4 md:px-6 text-sm md:text-base font-medium text-stone-600">Como Executar</button>
            <button data-tab="performance" class="nav-link py-3 px-4 md:px-6 text-sm md:text-base font-medium text-stone-600">Performance</button>
        </nav>

        <main>
            <!-- Visão Geral Section -->
            <section id="overview" class="content-section">
                <div class="text-center mb-12">
                    <h2 class="text-3xl font-bold text-stone-800">Anatomia do Sistema</h2>
                    <p class="mt-2 text-stone-600">Esta aplicação é um ecossistema de serviços que trabalham em conjunto. Clique em um componente abaixo para aprender sobre a sua função.</p>
                </div>

                <div class="space-y-4 md:space-y-0 md:grid md:grid-cols-11 md:gap-4 md:items-center text-center">
                    <!-- Client -->
                    <div class="col-span-2">
                        <div class="flex flex-col items-center">
                            <span class="text-6xl">🌐</span>
                            <p class="font-semibold mt-2">Utilizador</p>
                        </div>
                    </div>

                    <!-- Arrow -->
                    <div class="col-span-1 flex justify-center">
                        <span class="text-4xl text-stone-400">→</span>
                    </div>

                    <!-- Nginx -->
                    <div class="col-span-2">
                        <div id="diagram-nginx" class="diagram-component p-4 rounded-lg bg-white shadow-sm">
                            <span class="text-5xl">🚪</span>
                            <h3 class="font-bold mt-2">Nginx</h3>
                            <p class="text-xs text-stone-500">Gateway &<br>Load Balancer</p>
                        </div>
                    </div>
                    
                    <!-- Arrow -->
                    <div class="col-span-1 flex justify-center">
                       <span class="text-4xl text-stone-400">→</span>
                    </div>

                    <!-- App Replicas -->
                    <div class="col-span-2">
                        <div class="space-y-3">
                            <div id="diagram-app" class="diagram-component p-3 rounded-lg bg-white shadow-sm">
                                <span class="text-2xl">⚙️</span> <p class="text-sm font-semibold">API Réplica 1</p>
                            </div>
                            <div class="diagram-component p-3 rounded-lg bg-white shadow-sm">
                                <span class="text-2xl">⚙️</span> <p class="text-sm font-semibold">API Réplica 2</p>
                            </div>
                            <div class="diagram-component p-3 rounded-lg bg-white shadow-sm">
                                <span class="text-2xl">⚙️</span> <p class="text-sm font-semibold">API Réplica 3</p>
                            </div>
                        </div>
                    </div>

                    <!-- Arrows to Cache/DB -->
                    <div class="col-span-1 flex flex-col items-center justify-around">
                        <span class="text-4xl text-stone-400">→</span>
                        <span class="text-4xl text-stone-400 mt-16">→</span>
                    </div>

                    <!-- Cache and DB -->
                    <div class="col-span-2 space-y-4">
                        <div id="diagram-cache" class="diagram-component p-4 rounded-lg bg-white shadow-sm">
                             <span class="text-5xl">⚡️</span>
                            <h3 class="font-bold mt-2">Redis</h3>
                            <p class="text-xs text-stone-500">Cache<br>Distribuído</p>
                        </div>
                         <div id="diagram-db" class="diagram-component p-4 rounded-lg bg-white shadow-sm">
                             <span class="text-5xl">🗄️</span>
                            <h3 class="font-bold mt-2">PostgreSQL</h3>
                            <p class="text-xs text-stone-500">Banco de<br>Dados</p>
                        </div>
                    </div>

                </div>

                <div id="diagram-info" class="mt-12 p-6 rounded-lg bg-stone-100 border border-stone-200 min-h-[120px]">
                    <h3 id="diagram-title" class="text-xl font-bold text-stone-800">Visão Geral da Arquitetura</h3>
                    <p id="diagram-description" class="mt-2 text-stone-600">O utilizador faz um pedido que é recebido pelo Nginx. O Nginx atua como um porteiro inteligente, distribuindo a carga entre as três réplicas da aplicação FastAPI para garantir alta disponibilidade. Cada réplica da API primeiro consulta o cache Redis para uma resposta ultra-rápida. Se os dados não estiverem no cache, a API busca-os no banco de dados PostgreSQL, a nossa fonte da verdade, e guarda uma cópia no Redis para futuros pedidos.</p>
                </div>
            </section>

            <!-- Arquitetura Section -->
            <section id="architecture" class="content-section">
                 <div class="text-center mb-12">
                    <h2 class="text-3xl font-bold text-stone-800">Componentes do Sistema</h2>
                    <p class="mt-2 text-stone-600">Explore o código e a função de cada serviço que compõe a nossa arquitetura.</p>
                </div>
                <div class="space-y-8">
                    <div>
                        <h3 class="text-2xl font-semibold text-stone-800"> orchestrator Orquestração: `docker-compose.yml`</h3>
                        <p class="mt-1 text-stone-600 mb-4">Este é o maestro. Ele define todos os serviços (API, Nginx, DB, Cache), como eles se ligam e inicia todo o ecossistema com um único comando.</p>
                        <div class="code-block">
                             <button class="copy-button">Copiar</button>
                            <pre class="p-4 text-sm overflow-x-auto"><code class="language-yaml"># docker-compose.yml (Versão com Caching)
version: '3.8'

services:
  db:
    image: postgres:13-alpine
    container_name: db
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=admin
      - POSTGRES_DB=mercadorias_db
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready", "-U", "admin", "-d", "mercadorias_db"]
      interval: 10s
      timeout: 5s
      retries: 5

  cache:
    image: redis:7-alpine
    container_name: cache
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  app:
    build:
      context: ./app
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_healthy
    environment:
      - DATABASE_URL=postgresql://admin:admin@db:5432/mercadorias_db
      - CACHE_URL=redis://cache:6379
    deploy:
      replicas: 3

  nginx:
    build:
      context: ./nginx
    ports:
      - "80:80"
    depends_on:
      - app

volumes:
  postgres_data:
                            </code></pre>
                        </div>
                    </div>
                    <div>
                        <h3 class="text-2xl font-semibold text-stone-800">⚙️ Aplicação Principal: `app/main.py`</h3>
                        <p class="mt-1 text-stone-600 mb-4">O cérebro do sistema. Uma API FastAPI com um CRUD completo, lógica de cache com Redis e modelos de dados Pydantic/SQLAlchemy.</p>
                        <div class="code-block">
                             <button class="copy-button">Copiar</button>
                            <pre class="p-4 text-sm overflow-x-auto"><code class="language-python"># app/main.py (Versão com Caching)
import os
import socket
import json
from time import sleep
from contextlib import asynccontextmanager
from decimal import Decimal
from typing import List

import redis
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy import create_engine, String, Numeric
from sqlalchemy.orm import sessionmaker, Session, declarative_base, Mapped, mapped_column

# --- CONFIGURAÇÃO DOS SERVIÇOS ---
DATABASE_URL = os.getenv("DATABASE_URL")
CACHE_URL = os.getenv("CACHE_URL")

if not DATABASE_URL or not CACHE_URL:
    raise ValueError("As variáveis de ambiente DATABASE_URL e CACHE_URL devem ser definidas.")

# --- Conexão com o Banco de Dados ---
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- Conexão com o Cache (Redis) ---
cache = redis.from_url(CACHE_URL, decode_responses=True)

# ... (Restante do código CRUD)
                            </code></pre>
                        </div>
                    </div>
                </div>
            </section>
            
            <!-- Como Executar Section -->
            <section id="run" class="content-section">
                <div class="text-center mb-12">
                    <h2 class="text-3xl font-bold text-stone-800">Colocar para Funcionar</h2>
                    <p class="mt-2 text-stone-600">Siga um dos fluxos de trabalho abaixo, dependendo do seu objetivo.</p>
                </div>
                <div class="grid md:grid-cols-2 gap-8">
                    <div class="bg-white p-6 rounded-lg border border-stone-200 shadow-sm">
                        <h3 class="text-xl font-bold text-stone-800">Modo 1: Sistema Completo</h3>
                        <p class="text-stone-600 mt-2 mb-4 text-sm">A forma recomendada. Inicia todos os serviços (Nginx, 3x API, DB, Cache) juntos.</p>
                        <ol class="list-decimal list-inside space-y-3 text-stone-700">
                           <li>Navegue para a pasta raiz do projeto.</li>
                           <li>Execute o comando Docker Compose:</li>
                        </ol>
                         <div class="code-block mt-3">
                             <button class="copy-button">Copiar</button>
                            <pre class="p-4 text-sm"><code class="language-bash">docker-compose up --build</code></pre>
                        </div>
                        <p class="mt-4 text-sm text-stone-600">A API estará disponível em `http://localhost/mercadorias/`.</p>
                    </div>
                     <div class="bg-white p-6 rounded-lg border border-stone-200 shadow-sm">
                        <h3 class="text-xl font-bold text-stone-800">Modo 2: Desenvolvimento Local</h3>
                        <p class="text-stone-600 mt-2 mb-4 text-sm">Ideal para editar o código Python e ver as alterações em tempo real.</p>
                        <ol class="list-decimal list-inside space-y-3 text-stone-700">
                           <li>Num terminal, inicie o DB e o Cache:</li>
                        </ol>
                        <div class="code-block mt-3">
                             <button class="copy-button">Copiar</button>
                            <pre class="p-4 text-sm"><code class="language-bash">docker-compose up db cache</code></pre>
                        </div>
                        <ol class="list-decimal list-inside space-y-3 text-stone-700 mt-3" start="2">
                           <li>Noutro terminal, navegue para a pasta `app`, ative o `venv` e inicie o Uvicorn:</li>
                        </ol>
                        <div class="code-block mt-3">
                             <button class="copy-button">Copiar</button>
                            <pre class="p-4 text-sm"><code class="language-bash"># Dentro da pasta 'app'
uvicorn main:app --reload</code></pre>
                        </div>
                     </div>
                </div>
            </section>

            <!-- Performance Section -->
            <section id="performance" class="content-section">
                 <div class="text-center mb-12">
                    <h2 class="text-3xl font-bold text-stone-800">Impacto na Performance</h2>
                    <p class="mt-2 text-stone-600 max-w-2xl mx-auto">A implementação de teorias de sistemas distribuídos, como o caching, resolve gargalos críticos. O gráfico abaixo ilustra a melhoria drástica no tempo de resposta sob carga pesada.</p>
                </div>
                <div class="bg-white p-4 md:p-6 rounded-lg border border-stone-200 shadow-sm">
                    <h3 class="text-lg font-semibold text-center text-stone-800 mb-4">Tempo de Resposta (95º Percentil) - Antes vs. Depois do Cache</h3>
                    <div class="chart-container">
                        <canvas id="performanceChart"></canvas>
                    </div>
                </div>
                 <div class="mt-8 text-center">
                    <h3 class="text-xl font-bold text-stone-800">Como Testar Você Mesmo</h3>
                    <p class="mt-2 text-stone-600 mb-4">Use o Locust para simular milhares de utilizadores e ver estes resultados em tempo real.</p>
                     <div class="code-block max-w-md mx-auto">
                        <button class="copy-button">Copiar</button>
                        <pre class="p-4 text-sm"><code class="language-bash"># Requer 'pip install locust'
locust -f locustfile.py</code></pre>
                    </div>
                 </div>
            </section>
        </main>
    </div>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        const tabs = document.querySelectorAll('.nav-link');
        const sections = document.querySelectorAll('.content-section');
        const copyButtons = document.querySelectorAll('.copy-button');
        const diagramComponents = document.querySelectorAll('.diagram-component');
        const diagramInfo = {
            title: document.getElementById('diagram-title'),
            description: document.getElementById('diagram-description')
        };
        
        const diagramContent = {
            "diagram-nginx": {
                title: "🚪 Nginx (Gateway & Load Balancer)",
                description: "O Nginx é a porta de entrada única para todos os pedidos. Ele atua como um 'reverse proxy', recebendo o tráfego e distribuindo-o de forma inteligente entre as várias instâncias da API. Isto garante que nenhuma instância fique sobrecarregada (load balancing) e aumenta a disponibilidade do sistema."
            },
            "diagram-app": {
                title: "⚙️ Réplicas da API (FastAPI)",
                description: "O coração do sistema. Temos três cópias idênticas da nossa API a funcionar em paralelo. Se uma falhar, as outras continuam a servir os pedidos. Esta replicação horizontal é a chave para a escalabilidade e alta disponibilidade."
            },
            "diagram-cache": {
                title: "⚡️ Cache Distribuído (Redis)",
                description: "Um armazém de dados em memória ultra-rápido. Quando a API busca um dado pela primeira vez, ela guarda uma cópia no Redis. Nos pedidos seguintes para o mesmo dado, a resposta é quase instantânea, evitando uma consulta lenta ao banco de dados e melhorando drasticamente a performance."
            },
            "diagram-db": {
                title: "🗄️ Banco de Dados (PostgreSQL)",
                description: "A nossa fonte da verdade. O PostgreSQL armazena todos os dados das mercadorias de forma persistente e segura. É consultado apenas quando os dados não são encontrados no cache, garantindo a consistência da informação."
            },
            "default": {
                title: "Visão Geral da Arquitetura",
                description: "O utilizador faz um pedido que é recebido pelo Nginx. O Nginx atua como um porteiro inteligente, distribuindo a carga entre as três réplicas da aplicação FastAPI para garantir alta disponibilidade. Cada réplica da API primeiro consulta o cache Redis para uma resposta ultra-rápida. Se os dados não estiverem no cache, a API busca-os no banco de dados PostgreSQL, a nossa fonte da verdade, e guarda uma cópia no Redis para futuros pedidos."
            }
        };

        function setActiveTab(tabId) {
            tabs.forEach(tab => {
                tab.classList.toggle('active', tab.dataset.tab === tabId);
            });
            sections.forEach(section => {
                section.classList.toggle('active', section.id === tabId);
            });
            window.location.hash = tabId;
        }

        tabs.forEach(tab => {
            tab.addEventListener('click', () => setActiveTab(tab.dataset.tab));
        });

        const initialTab = window.location.hash.substring(1) || 'overview';
        setActiveTab(initialTab);

        copyButtons.forEach(button => {
            button.addEventListener('click', () => {
                const code = button.nextElementSibling.querySelector('code').innerText;
                navigator.clipboard.writeText(code).then(() => {
                    button.textContent = 'Copiado!';
                    setTimeout(() => {
                        button.textContent = 'Copiar';
                    }, 2000);
                });
            });
        });
        
        diagramComponents.forEach(component => {
            component.addEventListener('click', () => {
                const componentId = component.id;
                
                diagramComponents.forEach(comp => comp.classList.remove('highlighted'));
                component.classList.add('highlighted');

                const content = diagramContent[componentId] || diagramContent.default;
                diagramInfo.title.textContent = content.title;
                diagramInfo.description.textContent = content.description;
            });
        });

        const ctx = document.getElementById('performanceChart');
        if (ctx) {
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Tempo de Resposta (ms)'],
                    datasets: [{
                        label: 'Sem Cache (95º Percentil)',
                        data: [12000],
                        backgroundColor: 'rgba(239, 68, 68, 0.6)',
                        borderColor: 'rgba(239, 68, 68, 1)',
                        borderWidth: 1
                    }, {
                        label: 'Com Cache Redis (95º Percentil)',
                        data: [250],
                        backgroundColor: 'rgba(34, 197, 94, 0.6)',
                        borderColor: 'rgba(34, 197, 94, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Tempo de Resposta (milissegundos)'
                            }
                        }
                    },
                    plugins: {
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return `${context.dataset.label}: ${context.raw} ms`;
                                }
                            }
                        },
                        legend: {
                            position: 'bottom',
                        }
                    }
                }
            });
        }
    });
</script>

</body>
</html>
