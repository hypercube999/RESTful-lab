from typing import Dict

from pydantic import BaseModel
from datetime import datetime


class CountLettersResponse(BaseModel):
    counted_at: datetime
    counters: Dict[str, int]
