from fastapi import APIRouter, Depends, status, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_db
import src.schemas.bad_request as bad_request_schema
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
        return Response(status_code=204)

    return userList



@router.post('/users', status_code=201, responses={
    status.HTTP_201_CREATED: {'model': user_schema.User},
})
async def create_user(user_body: user_schema.UserBase, db: AsyncSession = Depends(get_db)):
    user = await user_crud.create_user(db, user_body)
    return user



@router.get('/users/{user_id}', responses={
    status.HTTP_200_OK: {'model': user_schema.User},
    status.HTTP_400_BAD_REQUEST: {'model': bad_request_schema.BadRequest},
})
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await user_crud.get_user(db, user_id)

    if user is None:
        return JSONResponse(
            status_code=400,
            content=jsonable_encoder( bad_request_schema.BadRequest(detail='User not found') )
        )
    
    return user



@router.put('/users/{user_id}', responses={
    status.HTTP_200_OK: {'model': user_schema.User},
    status.HTTP_400_BAD_REQUEST: {'model': bad_request_schema.BadRequest},
})
async def update_user(user_id: int, user_body: user_schema.UserBase, db: AsyncSession = Depends(get_db)):
    user = await user_crud.get_user(db, user_id)

    if user is None:
        return JSONResponse(
            status_code=400,
            content=jsonable_encoder( bad_request_schema.BadRequest(detail='User not found') )
        )

    return await user_crud.update_user(db, user_body, user)



@router.delete('/users/{user_id}', status_code=204, responses={
    status.HTTP_204_NO_CONTENT: {'model': None},
    status.HTTP_400_BAD_REQUEST: {'model': bad_request_schema.BadRequest},
})
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await user_crud.get_user(db, user_id)

    if user is None:
        return JSONResponse(
            status_code=400,
            content=jsonable_encoder( bad_request_schema.BadRequest(detail='User not found') )
        )

    return await user_crud.delete_user(db, user)