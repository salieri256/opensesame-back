from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_db
import src.schemas.active as active_schema
import src.cruds.active as active_crud

router = APIRouter()

@router.get('/users/{user_id}/active', responses={
    status.HTTP_200_OK: {'model': active_schema.Active},
    status.HTTP_400_BAD_REQUEST: {'model': None},
})
async def get_active(user_id: int, db: AsyncSession = Depends(get_db)):
    active = await active_crud.get_active(db, user_id)

    if active == None:
        raise HTTPException(status_code=400, detail='User not active')

    return active



@router.post('/users/{user_id}/active', responses={
    status.HTTP_201_CREATED: {'model': active_schema.Active},
})
async def create_active(user_id: int, db: AsyncSession = Depends(get_db)):
    return await active_crud.create_active(db, user_id)



@router.delete('/users/{user_id}/active', responses={
    status.HTTP_204_NO_CONTENT: {'model': None},
    status.HTTP_400_BAD_REQUEST: {'model': None},
})
async def delete_active(user_id: int, db: AsyncSession = Depends(get_db)):
    active = await active_crud.get_active(db, user_id)

    if active is None:
        raise HTTPException(status_code=400, detail='User not active')

    return await active_crud.delete_active(db, active)