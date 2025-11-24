# 🏋️‍♂️ WorkoutAPI — API de Academia para Competição de Crossfit  
API desenvolvida com **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Pydantic** e **Docker**, seguindo arquitetura profissional com camadas MVC + Service.  
Projeto criado para o desafio prático da **DIO – Desenvolvendo sua Primeira API com FastAPI, Python e Docker**.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI (assíncrona)**
- **SQLAlchemy**
- **Pydantic**
- **PostgreSQL**
- **Docker + Docker Compose**
- **FastAPI Pagination**
- **Uvicorn**
- **Alembic** (opcional)

---

## 🧱 Arquitetura do Projeto (MVC + Service)

```

app/
├── main.py
├── database/
│     └── db.py
├── models/
│     └── atleta.py
├── schemas/
│     └── atleta.py
├── services/
│     └── atleta_service.py
├── controllers/
│     └── atleta_controller.py
└── utils/
└── pagination.py (opcional)

````

- **Models** → ORM e tabelas  
- **Schemas** → Pydantic (validação)  
- **Controllers** → Rotas/Endpoints  
- **Services** → Regras de negócio  
- **Database** → Conexão com Postgres  

---

# 🔌 Instalação e Execução

## 📦 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/workout_api
cd workout_api
````

---

# 🐳 2. Rodar com Docker (recomendado)

### Subir o banco PostgreSQL

```bash
docker compose up -d
```

---

# 🐍 3. Criar ambiente Python

Se usar **Poetry** (recomendado):

```bash
poetry install
poetry shell
```

Ou com pip:

```bash
pip install -r requirements.txt
```

---

# ▶️ 4. Rodar a API

```bash
uvicorn app.main:app --reload
```

Acesse:

📍 URL base: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

📘 Documentação Swagger:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

📕 Documentação Redoc:
👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

# 🧪 Endpoints Disponíveis

## 👤 Atletas

### ➤ Listar todos os atletas (com paginação + filtros)

```
GET /atletas/?nome=lucas&cpf=123
```

Query parameters:

* `nome`: filtra por parte do nome
* `cpf`: filtra por CPF exato
* `limit`: paginação
* `offset`: paginação

Retorno customizado:

```json
{
  "items": [
    {
      "nome": "Lucas Gabriel",
      "centro_treinamento": "CT Power",
      "categoria": "RX"
    }
  ],
  "total": 1,
  "page": 1,
  "size": 10
}
```

---

### ➤ Obter atleta por ID

```
GET /atletas/1
```

---

### ➤ Criar atleta

```
POST /atletas/
```

```json
{
  "nome": "Priscila",
  "cpf": "12345678900",
  "centro_treinamento": "CT Power",
  "categoria": "Intermediário"
}
```

📌 **Validação de CPF duplicado**
Retorna:

```
Status: 303
{
  "detail": "Já existe um atleta cadastrado com o cpf: 12345678900"
}
```

---

### ➤ Deletar atleta

```
DELETE /atletas/1
```

---

# 🧩 Funcionalidades Implementadas (Desafio da DIO ✔)

| Requisito                                 | Status |
| ----------------------------------------- | ------ |
| Adicionar Query Parameters (nome e cpf)   | ✅      |
| Customizar resposta do GET All            | ✅      |
| Tratar erro sqlalchemy.exc.IntegrityError | ✅      |
| Mensagem personalizada                    | ✅      |
| Status code 303 em duplicidade de CPF     | ✅      |
| Paginação com fastapi-pagination          | ✅      |
| Arquitetura MVC + Service                 | ✅      |
| Código limpo e profissional               | ✅      |

---

# 🗃 Banco de Dados

### Tabela: **atletas**

| Campo              | Tipo       | Descrição      |
| ------------------ | ---------- | -------------- |
| id                 | Integer PK | Identificador  |
| nome               | String     | Nome do atleta |
| cpf                | String UNI | CPF único      |
| centro_treinamento | String     | CT             |
| categoria          | String     | Categoria      |

---

# 🛠 Como Rodar as Migrations (Opcional)

Se quiser usar o **Alembic**:

```bash
make create-migrations d="create_atletas"
make run-migrations
```

---

# 🧑‍💻 Autor

Projeto desenvolvido por **Lucas Gabriel**
📍 Santana do Livramento — RS

---

# ⭐ Dê um Star!

Se este projeto te ajudou, deixe uma ⭐ no repositório!
