# Case Técnico Pilar - Text Processing API

Uma API REST desenvolvida como parte do processo seletivo da Pilar, demonstrando boas práticas de desenvolvimento e arquitetura de software. A API oferece funcionalidades de processamento de texto, incluindo análise de vogais e ordenação de strings.

## Estrutura do Projeto

```
.
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   └── text_routes.py
│   ├── models/
│   ├── schemas/
│   │   └── request_schemas.py
│   └── services/
│       └── text_service.py
├── tests/
│   ├── integration/
│   │   └── test_api_routes.py
│   └── unit/
│       └── test_text_service.py
├── pyproject.toml
└── README.md
```

## Requisitos

- Python 3.8+
- Poetry (gerenciador de dependências)

### Nota para usuários de macOS
Se você estiver usando macOS e o comando `python3` não estiver disponível, você pode instalá-lo usando o Homebrew:
```bash
brew install python3
```

Para instalar o Poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

## Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd case-pilar
```

2. Instale as dependências usando Poetry:
```bash
poetry install
```

3. Ative o ambiente virtual do Poetry:
```bash
poetry shell
```

## Executando a Aplicação

Dentro do ambiente virtual do Poetry (após `poetry shell`):

1. Usando uvicorn diretamente (recomendado para desenvolvimento):
```bash
uvicorn app:app --reload
```

2. Ou através do módulo Python:
```bash
python -m app.main
```

A API estará disponível em `http://localhost:8000`

## Documentação da API

A documentação interativa (Swagger UI) está disponível em:
- `http://localhost:8000/docs`

A documentação alternativa (ReDoc) está disponível em:
- `http://localhost:8000/redoc`

## Endpoints

### 1. Contagem de Vogais
- **Endpoint**: `POST /api/v1/vowel_count`
- **Descrição**: Analisa e conta o número de vogais em cada palavra fornecida
- **Content-Type**: application/json (obrigatório)
- **Request Body**:
```json
{
    "words": ["desenvolvimento", "tecnologia", "inovacao"]
}
```
- **Resposta de Sucesso** (200 OK):
```json
{
    "desenvolvimento": 6,
    "tecnologia": 5,
    "inovacao": 5
}
```

### 2. Ordenação de Palavras
- **Endpoint**: `POST /api/v1/sort`
- **Descrição**: Ordena uma lista de palavras em ordem ascendente ou descendente
- **Content-Type**: application/json (obrigatório)
- **Request Body**:
```json
{
    "words": ["software", "desenvolvimento", "qualidade"],
    "order": "asc"
}
```
- **Resposta de Sucesso** (200 OK):
```json
["desenvolvimento", "qualidade", "software"]
```

## Respostas de Erro

A API utiliza códigos HTTP padrão para indicar o status da requisição:

### 1. Erro de Validação (422 Unprocessable Entity)
Quando os dados enviados não atendem às validações:

```json
{
    "error": "Erro de validação",
    "detail": {
        "field": "order",
        "message": "O valor deve ser 'asc' ou 'desc'",
        "received": "invalid"
    }
}
```

### 2. Content-Type Inválido (415 Unsupported Media Type)
Quando o Content-Type não é application/json:

```json
{
    "detail": "Unsupported Media Type"
}
```

### 3. Método Não Permitido (405 Method Not Allowed)
Quando usa um método HTTP não suportado (ex: GET em vez de POST):

```json
{
    "detail": "Method Not Allowed"
}
```
Headers incluem: `Allow: POST`

### 4. Rota Não Encontrada (404 Not Found)
Quando tenta acessar uma rota que não existe:

```json
{
    "detail": "Not Found"
}
```

## Executando Testes

Com o Poetry, você pode executar os testes facilmente:

```bash
# Executar todos os testes
poetry run pytest

# Executar testes com cobertura
poetry run pytest --cov=app tests/

# Executar apenas testes unitários
poetry run pytest tests/unit/

# Executar apenas testes de integração
poetry run pytest tests/integration/
```

## Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) - Framework web moderno e rápido
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Validação de dados
- [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI para Python
- [Pytest](https://docs.pytest.org/) - Framework de testes
- [Poetry](https://python-poetry.org/) - Gerenciamento de dependências

## Sobre o Desenvolvimento

Este projeto foi desenvolvido como parte do processo seletivo da Pilar, demonstrando:
- Arquitetura limpa e organizada
- Boas práticas de desenvolvimento
- Testes automatizados (unitários e de integração)
- Documentação clara e objetiva
- Uso de tecnologias modernas
- Tratamento adequado de erros
- Validações robustas 