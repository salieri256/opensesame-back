from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_db
import src.schemas.user as user_schema
import src.cruds.user as user_crud

router = APIRouter()

@router.get('/users', response_model=list[user_schema.User])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    return await user_crud.get_all_users(db)

@router.post('/users', response_model=user_schema.User)
async def create_user(user_body: user_schema.UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_crud.create_user(db, user_body)

@router.get('/users/{user_id}', response_model=user_schema.User)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await user_crud.get_user(db, user_id)

    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    
    return user

@router.put('/users/{user_id}', response_model=user_schema.User)
async def update_user(user_id: int, user_body: user_schema.UserCreate, db: AsyncSession = Depends(get_db)):
    user = await user_crud.get_user(db, user_id)

    if user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return await user_crud.update_user(db, user_body, user)

@router.delete('/users/{user_id}', response_model=None)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await user_crud.get_user(db, user_id)

    if user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return await user_crud.delete_user(db, user)