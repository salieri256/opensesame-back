from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_db
import src.schemas.user as user_schema
import src.cruds.user as user_crud

router = APIRouter()

@router.get('/users', responses={
    status.HTTP_200_OK: {'model': list[user_schema.User]},
    status.HTTP_204_NO_CONTENT: {'model': None},
})
async def get_all_users(db: AsyncSession = Depends(get_db)):
    userList = await user_crud.get_all_users(db)

    if len(userList) == 0:
        return JSONResponse(status_code=204, content=None)

    return userList



@router.post('/users', status_code=201, responses={
    status.HTTP_201_CREATED: {'model': user_schema.User},
})
async def create_user(user_body: user_schema.UserBase, db: AsyncSession = Depends(get_db)):
    user = await user_crud.create_user(db, user_body)
    return user



@router.get('/users/{user_id}', responses={
    status.HTTP_200_OK: {'model': user_schema.User},
    status.HTTP_400_BAD_REQUEST: {'model': {'detail': str}},
})
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await user_crud.get_user(db, user_id)

    if user is None:
        raise HTTPException(status_code=400, detail='User not found')
    
    return user



@router.put('/users/{user_id}', responses={
    status.HTTP_200_OK: {'model': user_schema.User},
    status.HTTP_400_BAD_REQUEST: {'model': {'detail': str}},
})
async def update_user(user_id: int, user_body: user_schema.UserBase, db: AsyncSession = Depends(get_db)):
    user = await user_crud.get_user(db, user_id)

    if user is None:
        raise HTTPException(status_code=400, detail='User not found')

    return await user_crud.update_user(db, user_body, user)



@router.delete('/users/{user_id}', status_code=204, responses={
    status.HTTP_204_NO_CONTENT: {'model': None},
    status.HTTP_400_BAD_REQUEST: {'model': {'detail': str}},
})
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await user_crud.get_user(db, user_id)

    if user is None:
        raise HTTPException(status_code=400, detail='User not found')

    return await user_crud.delete_user(db, user)