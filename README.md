# projeto4

API REST de filmes e gêneros feita com Django e Django REST Framework.

## Tecnologias

- Python 3
- Django
- Django REST Framework (com autenticação por token)
- django-filter
- SQLite

## Como subir o projeto

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd projeto4
```

### 2. Criar e ativar o ambiente virtual

Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows (CMD):

```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Criar o banco de dados

```bash
python manage.py migrate
```

### 5. Criar um usuário administrador

```bash
python manage.py createsuperuser
```

### 6. (Opcional) Importar os filmes do CSV

O script `importarDados.py` lê o arquivo `base_filmes.csv` e cadastra os filmes e gêneros no banco:

```bash
python importarDados.py
```

> Rode apenas uma vez: se executar de novo, os filmes serão cadastrados em duplicidade.

### 7. Rodar o servidor

```bash
python manage.py runserver
```

A API fica disponível em `http://localhost:8000/`. Para usar outra porta: `python manage.py runserver 8001`.

## Rotas

| Método | Rota | Descrição | Precisa de token |
|---|---|---|---|
| GET | `/api/` | Lista as rotas da API | Não |
| POST | `/api/token/` | Gera o token do usuário | Não |
| GET | `/api/generos/` | Lista os gêneros | Não |
| POST | `/api/generos/` | Cadastra um gênero | Sim |
| GET | `/api/generos/{id}/` | Detalha um gênero | Não |
| PUT / PATCH | `/api/generos/{id}/` | Atualiza um gênero | Sim |
| DELETE | `/api/generos/{id}/` | Remove um gênero | Sim |
| GET | `/api/filmes/` | Lista os filmes | Não |
| POST | `/api/filmes/` | Cadastra um filme | Sim |
| GET | `/api/filmes/{id}/` | Detalha um filme | Não |
| PUT / PATCH | `/api/filmes/{id}/` | Atualiza um filme | Sim |
| DELETE | `/api/filmes/{id}/` | Remove um filme | Sim |
| — | `/admin/` | Painel administrativo do Django | Login |

### Filtros de filmes

A listagem de filmes aceita filtros por `titulo`, `descricao` e `ano_lancamento`:

```
GET /api/filmes/?ano_lancamento=1999
GET /api/filmes/?titulo=Matrix
```

### Campos

**Gênero**

| Campo | Tipo |
|---|---|
| `nome` | texto |

**Filme**

| Campo | Tipo |
|---|---|
| `titulo` | texto |
| `descricao` | texto |
| `ano_lancamento` | número inteiro positivo |
| `genero` | id do gênero |
| `duracao` | texto (ex.: `"136"`) |

## Exemplos com curl

As consultas (GET) são liberadas. Para cadastrar, editar ou remover, é preciso enviar o token no cabeçalho `Authorization`.

Nos exemplos abaixo, troque `SEU_TOKEN` pelo token gerado no passo de autenticação.

### Linux Terminal

**Gerar o token**

```bash
curl -X POST http://localhost:8000/api/token/ \
 -H "Content-Type: application/json" \
 -d '{"username": "admin", "password": "sua_senha"}'
```

Resposta:

```json
{"token": "0123456789abcdef0123456789abcdef01234567"}
```

**POST em gêneros**

```bash
curl -X POST http://localhost:8000/api/generos/ \
 -H "Authorization: Token SEU_TOKEN" \
 -H "Content-Type: application/json" \
 -d '{"nome": "Ficção Científica"}'
```

**POST em filmes**

```bash
curl -X POST http://localhost:8000/api/filmes/ \
 -H "Authorization: Token SEU_TOKEN" \
 -H "Content-Type: application/json" \
 -d '{"titulo": "Matrix", "descricao": "Um hacker descobre a verdade sobre a realidade simulada.", "ano_lancamento": 1999, "genero": 1, "duracao": "136"}'
```

**GET em filmes**

```bash
curl http://localhost:8000/api/filmes/
```

**PUT em filmes**

```bash
curl -X PUT http://localhost:8000/api/filmes/1/ \
 -H "Authorization: Token SEU_TOKEN" \
 -H "Content-Type: application/json" \
 -d '{"titulo": "Matrix", "descricao": "Nova descrição.", "ano_lancamento": 1999, "genero": 1, "duracao": "136"}'
```

**DELETE em filmes**

```bash
curl -X DELETE http://localhost:8000/api/filmes/1/ \
 -H "Authorization: Token SEU_TOKEN"
```

### Windows CMD

No CMD, a quebra de linha é feita com `^` e as aspas dentro do JSON precisam ser escapadas com `\"`.

**Gerar o token**

```cmd
curl -X POST http://localhost:8000/api/token/ ^
 -H "Content-Type: application/json" ^
 -d "{\"username\": \"admin\", \"password\": \"sua_senha\"}"
```

**POST em gêneros**

```cmd
curl -X POST http://localhost:8000/api/generos/ ^
 -H "Authorization: Token SEU_TOKEN" ^
 -H "Content-Type: application/json" ^
 -d "{\"nome\": \"Drama\"}"
```

**POST em filmes**

```cmd
curl -X POST http://localhost:8000/api/filmes/ ^
 -H "Authorization: Token SEU_TOKEN" ^
 -H "Content-Type: application/json" ^
 -d "{\"titulo\": \"Matrix\", \"descricao\": \"Um hacker descobre a verdade sobre a realidade simulada.\", \"ano_lancamento\": 1999, \"genero\": 1, \"duracao\": \"136\"}"
```

**GET em filmes**

```cmd
curl http://localhost:8000/api/filmes/
```

**PUT em filmes**

```cmd
curl -X PUT http://localhost:8000/api/filmes/1/ ^
 -H "Authorization: Token SEU_TOKEN" ^
 -H "Content-Type: application/json" ^
 -d "{\"titulo\": \"Matrix\", \"descricao\": \"Nova descricao.\", \"ano_lancamento\": 1999, \"genero\": 1, \"duracao\": \"136\"}"
```

**DELETE em filmes**

```cmd
curl -X DELETE http://localhost:8000/api/filmes/1/ ^
 -H "Authorization: Token SEU_TOKEN"
```
