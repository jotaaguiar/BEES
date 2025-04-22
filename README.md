# 🍺 BEES – Data Engineering Case

## 📌 Sobre o Projeto

Este projeto simula um pipeline de dados utilizando a arquitetura Medallion.

A orquestração é feita com **Apache Airflow** e a execução ocorre em ambiente **Docker**. A fonte de dados é a **Open Brewery DB API**.

---

## 🎯 Objetivo

Demonstrar a criação de um pipeline completo que abrange:

- Coleta de dados de uma API
- Processamento e transformação dos dados
- Armazenamento otimizado em camadas (Bronze → Silver → Gold)
- Orquestração de tarefas com Airflow
- Execução em ambiente isolado e escalável com Docker

---

## 🚀 Como Executar Localmente

### Pré-requisitos

- **Docker**
- **Docker Compose**
- Caso não possua o Docker Localmente, instruções para a instalação ao final da documentação.
### Passos para execução

1. Inicie os containers:
   ```bash
   docker-compose up --build
   ```

2. Acesse a interface do Apache Airflow:
   - **URL**: [http://localhost:8080](http://localhost:8080)
   - **Usuário**: `airflow`
   - **Senha**: `airflow`
   - Inicio a Dag Com uma Trigger manual

---

## 🏗️ Arquitetura do Pipeline

O pipeline segue uma estrutura de três camadas:

1. 🔹 **Bronze**  
   - Dados brutos coletados diretamente da API, armazenados em formato **JSON**.

2. 🔸 **Silver**  
   - Dados convertidos para o formato **Parquet**, otimizando o armazenamento e a leitura.
   - Particionamento dos dados por **estado da cervejaria**.

3. 🏅 **Gold**  
   - Aplicação de regras de negócios.
   - Agregação de dados: contagem de cervejarias por tipo e estado.

---

## 📂 Organização do Data Lake

```bash
data_lake/
├── bronze/        # Dados crus (JSON)
├── silver/        # Dados tratados (Parquet), particionados por estado
└── gold/          # Dados finais com agregações (estado e tipo)
```

---

## 📊 Resultado Esperado

Após a execução do pipeline no Airflow:

- Os dados estarão organizados localmente na pasta `data_lake/`
- Cada camada representará um nível de tratamento e estruturação dos dados
- A camada **Gold** entregará dados prontos para consumo analítico

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **PySpark**
- **Apache Airflow**
- **Docker**
- **Open Brewery DB API**

---

## 💻 Instalação do Docker

### 🧱 Instalar o WSL 2

No **PowerShell** como Administrador, execute:

```powershell
wsl --install
```

### 🐳 Baixar e Instalar o Docker Desktop

1. Acesse: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
2. Clique em **Download for Windows (WSL2)**
3. Siga o assistente de instalação (**Next > Next > Finish**)
4. Ao abrir o Docker pela primeira vez:
   - Aceite instalar o **WSL 2 Backend** se solicitado
   - Verifique a mensagem **"Docker is running"**

### 🔍 Verificar Instalação

No terminal do **VSCode** ou **PowerShell**, execute:

```bash
docker --version
docker compose version
```

Você deve ver as versões do Docker e Docker Compose instaladas.

---

