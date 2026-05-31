
from pydantic import BaseModel


class Media(BaseModel):
    id: int 
    title: str
    release_year: int | None = None
    rating: int | None = None


class Copy(BaseModel):
    id: int
    media_id: int
    format: str
    notes: str | None = None
