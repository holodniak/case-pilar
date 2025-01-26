from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import JSONResponse
from app.schemas.request_schemas import Words, WordsWithOrder
from app.services.text_service import TextService

router = APIRouter()
text_service = TextService()

@router.post("/vowel_count", response_model=dict[str, int])
async def count_vowels(request: Request, body: Words):
    if request.headers.get("content-type") != "application/json":
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Content-Type deve ser application/json"
        )
    
    try:
        return text_service.count_vowels(body.words)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/sort", response_model=list[str])
async def sort_words(request: Request, body: WordsWithOrder):
    if request.headers.get("content-type") != "application/json":
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Content-Type deve ser application/json"
        )
    
    try:
        return text_service.sort_words(body.words, body.order)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"], include_in_schema=False)
async def catch_all(path: str):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Rota não encontrada"
    )
