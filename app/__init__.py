from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.api.text_routes import router

app = FastAPI(
    title="Case Pilar API",
    description="API for text processing: counting vowels and sorting words",
    version="1.0.0"
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    error_messages = {
        "enum": "O valor deve ser 'asc' ou 'desc'",
        "list_type": "Todos os elementos devem ser strings",
        "missing": "Este campo é obrigatório",
        "value_error": "Valor inválido para este campo"
    }
    
    error = exc.errors()[0] 
    field = error.get("loc", ["unknown"])[-1]
    error_type = error.get("type", "value_error")
    
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "Erro de validação",
            "detail": {
                "field": field,
                "message": error_messages.get(error_type, str(error.get("msg"))),
                "received": error.get("input")
            }
        }
    )

app.include_router(router, prefix="/api/v1", tags=["Case Pilar"])

__all__ = ["app"] 