from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import JSONResponse
from app.schemas.request_schemas import Words, WordsWithOrder
from app.services.text_service import TextService
from typing import Annotated

router = APIRouter()
text_service = TextService()

@router.post("/vowel_count", response_model=dict[str, int])
async def count_vowels(body: Words):
    try:
        return text_service.count_vowels(body.words)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/sort", response_model=list[str])
async def sort_words(body: WordsWithOrder):
    try:
        return text_service.sort_words(body.words, body.order)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
