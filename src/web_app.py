import datetime

import fastapi

from model import CountLettersResponse

api_router = fastapi.APIRouter()


@api_router.get("/sum", response_model=float)
def sum_(a: float, b: float):
    return a + b


@api_router.get("/count_letters", response_model=CountLettersResponse)
def count_letters(text: str):
    letters_count = {}
    for letter in text:
        if letter in letters_count:
            letters_count[letter] += 1
        else:
            letters_count[letter] = 1
    return CountLettersResponse(
        counted_at=datetime.datetime.now(),
        counters=letters_count
    )
