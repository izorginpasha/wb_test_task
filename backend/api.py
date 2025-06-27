from fastapi import APIRouter
from schemas import ProductResponse

api_router = APIRouter(prefix="/products", tags=['products'])

api_router.get("/", response_model=list[ProductResponse])
async def get_habits_endpoint(user_id: int, db: db_dependency, current_user: str = Depends(get_current_user)):
    return await get_habits(db, user_id)