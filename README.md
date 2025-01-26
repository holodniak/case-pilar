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
│   └── test_text_service.py
├── requirements.txt
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
- **Validações**:
  - Lista não pode estar vazia
  - Todos os elementos devem ser strings
  - Palavras não podem estar vazias ou conter apenas espaços
- **Exemplo de Request**:
```json
{
    "words": ["desenvolvimento", "tecnologia", "inovacao"]
}
```
- **Exemplo de Response (Sucesso)**:
```json
{
    "desenvolvimento": 7,
    "tecnologia": 5,
    "inovacao": 5
}
```
- **Exemplo de Response (Erro - Lista com elementos não-string)**:
```json
{
    "error": "Erro de validação",
    "details": [
        {
            "field": "words",
            "message": "Todos os elementos devem ser strings",
            "received": [123, "texto", true]
        }
    ]
}
```

### 2. Ordenação de Palavras
- **Endpoint**: `POST /api/v1/sort`
- **Descrição**: Ordena uma lista de palavras em ordem ascendente ou descendente
- **Content-Type**: application/json (obrigatório)
- **Validações**:
  - Lista não pode estar vazia
  - Todos os elementos devem ser strings
  - Palavras não podem estar vazias ou conter apenas espaços
  - Ordem deve ser exatamente "asc" ou "desc"
- **Exemplo de Request (Sucesso)**:
```json
{
    "words": ["software", "desenvolvimento", "qualidade"],
    "order": "asc"
}
```
- **Exemplo de Response (Sucesso)**:
```json
["desenvolvimento", "qualidade", "software"]
```
- **Exemplo de Response (Erro - Ordem inválida)**:
```json
{
    "error": "Erro de validação",
    "details": [
        {
            "field": "order",
            "message": "O valor deve ser 'asc' ou 'desc'",
            "received": "crescente"
        }
    ]
}
```

## Códigos de Status HTTP

A API utiliza os seguintes códigos de status HTTP:

- `200 OK`: Requisição bem-sucedida
- `400 Bad Request`: Dados inválidos no corpo da requisição
- `404 Not Found`: Rota não encontrada
- `415 Unsupported Media Type`: Content-Type não é application/json
- `422 Unprocessable Entity`: Dados válidos sintaticamente mas semanticamente incorretos
- `500 Internal Server Error`: Erro interno do servidor

### Exemplos de Erros Comuns

1. **Content-Type Incorreto**:
```json
{
    "detail": "Content-Type deve ser application/json"
}
```

2. **Rota Não Encontrada**:
```json
{
    "detail": "Rota não encontrada"
}
```

3. **Validação de Dados**:
```json
{
    "error": "Erro de validação",
    "details": [
        {
            "field": "words",
            "message": "A lista de palavras não pode estar vazia",
            "received": []
        }
    ]
}
```

## Executando Testes

Com o Poetry, você pode executar os testes facilmente:

```bash
# Executar todos os testes
poetry run pytest

# Executar testes com cobertura
poetry run pytest --cov=app tests/
```

## Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) - Framework web moderno e rápido
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Validação de dados
- [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI para Python
- [Pytest](https://docs.pytest.org/) - Framework de testes

## Sobre o Desenvolvimento

Este projeto foi desenvolvido como parte do processo seletivo da Pilar, demonstrando:
- Arquitetura limpa e organizada
- Boas práticas de desenvolvimento
- Testes automatizados
- Documentação clara e objetiva
- Uso de tecnologias modernas 