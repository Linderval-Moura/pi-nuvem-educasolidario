<div align="center">

  <h1>🎒 EducaSolidario - Cloud Edition</h1>

  <p>
    <strong>Infraestrutura Ágil para Gestão de Doações Escolares 🚀</strong>
  </p>

  <p>
    <a href="https://flask.palletsprojects.com/" target="blank"><img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask Logo" /></a>
    <a href="https://aws.amazon.com/" target="blank"><img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS Logo" /></a>
    <a href="https://www.postgresql.org/" target="blank"><img src="https://img.shields.io/badge/PostgreSQL-3178C6?style=for-the-badge&logo=postgresql&logoColor=white" alt="Postgres Logo" /></a>
    <a href="https://www.docker.com/" target="blank"><img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Logo" /></a>
  </p>

</div>

<br />

O **EducaSolidario** é um projeto desenvolvido para a disciplina de Computação em Nuvem (IFCE). Esta versão foca na implantação de uma infraestrutura escalável utilizando **Docker Compose** em uma instância **IaaS (AWS EC2)**.

## 🏗️ Arquitetura da Solução

```mermaid
graph LR
    A[Usuário/Navegador] -->|HTTP Porta 80| B(Instância EC2 - AWS)
    subgraph Docker_Compose
        B --> C[Serviço Web: Flask]
        C -->|Consulta SQL| D[(Serviço DB: PostgreSQL 16)]
    end

    style B fill:#232f3e,color:#fff
    style C fill:#000,color:#fff
    style D fill:#3178c6,color:#fff
```

## 🚀 Objetivo
Demonstrar a execução de uma aplicação Web (Flask) integrada a um banco de dados (PostgreSQL), ambos orquestrados via Docker, rodando em uma máquina virtual na nuvem com acesso via IP público.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.9 (Flask)
* **Banco de Dados:** PostgreSQL 16
* **Orquestração:** Docker Compose
* **Infraestrutura:** AWS EC2 (ou Oracle Cloud)
* **Sistema Operacional:** Linux (Ubuntu/Amazon Linux)

## 📁 Estrutura do Repositório
```
/
├── app/
│   ├── app.py          # Lógica da aplicação Flask e conexão DB
│   ├── requirements.txt # Dependências (flask, psycopg2-binary)
│   └── Dockerfile      # Build da imagem da aplicação
├── db/
│   └── init.sql        # Script de criação de tabela e carga inicial
└── docker-compose.yml  # Orquestração dos serviços
```

## ⚙️ Como Executar (Na Instância Cloud)
Pré-requisitos 📋
* Instância EC2 rodando (Ubuntu recomendado).

* Docker e Docker Compose instalados na instância.

## Passo a Passo 🚀
Acesse sua instância via SSH:
```
ssh -i "sua-chave.pem" ubuntu@ip-publico-aws
```
Clone este repositório:
```
git clone [https://github.com/seu-usuario/educasolidario-cloud.git](https://github.com/seu-usuario/educasolidario-cloud.git)
cd educasolidario-cloud
```
Suba os serviços:
```
sudo docker compose up -d
```

Acesse no Navegador:

Abra ```http://seu-ip-publico-aws```

## 👥 Equipe (PI - UFCA)
* Juliett Figueirêdo (Desenvolvedor Cloud)
* Juan Carlos (Desenvolvedor Backend)
* Linderval Matias (Integrador & Editor)

📜 Licença
Este projeto foi desenvolvido para fins acadêmicos no curso de ADS - UFCA.
