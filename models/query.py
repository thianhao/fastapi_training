from pydantic import BaseModel
from typing import Optional


class Query(BaseModel):
    city: str
    factor: Optional[str] = 'overall'
