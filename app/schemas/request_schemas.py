from enum import Enum
from typing import List

from pydantic import BaseModel, Field, field_validator


class SortOrder(str, Enum):
    ASC = "asc"
    DESC = "desc"


class Words(BaseModel):
    words: List[str] = Field(
        min_length=1,
        description="Lista de palavras para processar",
        examples=[["desenvolvimento", "tecnologia", "inovacao"]],
    )

    @field_validator("words")
    def validate_words(self, words: List[str]) -> List[str]:
        if not words:
            raise ValueError("A lista de palavras não pode estar vazia")

        if any(not isinstance(word, str) for word in words):
            raise ValueError("Todos os elementos devem ser strings")

        if any(not word.strip() for word in words):
            raise ValueError(
                "As palavras não podem estar vazias ou conter apenas espaços"
            )

        return [word.strip() for word in words]


class WordsWithOrder(Words):
    order: SortOrder = Field(
        description=(
            "Ordem de classificação ('asc' para ascendente, 'desc' para descendente)"
        ),
        examples=["asc"],
    )
