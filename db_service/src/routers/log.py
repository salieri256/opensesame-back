from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_db
import src.schemas.log as log_schema
import src.cruds.log as log_crud

router = APIRouter()

@router.get('/logs', response_model=list[log_schema.Log])
async def get_all_logs(db: AsyncSession = Depends(get_db)):
    return await log_crud.get_all_logs(db)