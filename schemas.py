from pydantic import BaseModel
from typing import Optional

class SMessageAdd(BaseModel):
    message: str

class SMessageGet(SMessageAdd):
    id: int