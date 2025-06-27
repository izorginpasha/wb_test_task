# schemas.py
from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    sale_price: float
    rating: float
    feedbacks: int

    class Config:
        orm_mode = True
