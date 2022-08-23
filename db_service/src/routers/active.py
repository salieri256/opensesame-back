from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_db
import src.schemas.bad_request as bad_request_schema
import src.schemas.active as active_schema
import src.cruds.user as user_crud
import src.cruds.active as active_crud

router = APIRouter()

@router.get('/users/{user_id}/active', responses={
    status.HTTP_200_OK: {'model': active_schema.Active},
    status.HTTP_400_BAD_REQUEST: {'model': bad_request_schema.BadRequest},
})
async def get_user_active(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await user_crud.get_user(db, user_id)

    if user is None:
        return JSONResponse(
            status_code=400,
            content=jsonable_encoder( bad_request_schema.BadRequest(detail='User not found') )
        )
    
    active = await active_crud.get_active(db, user)
    return active



@router.post('/users/{user_id}/active', responses={
    status.HTTP_200_OK: {'model': active_schema.Active},
    status.HTTP_400_BAD_REQUEST: {'model': bad_request_schema.BadRequest},
})
async def create_user_active(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await user_crud.get_user(db, user_id)

    if user is None:
        return JSONResponse(
            status_code=400,
            content=jsonable_encoder( bad_request_schema.BadRequest(detail='User not found') )
        )

    active = await active_crud.create_active(db, user)
    return active



@router.delete('/users/{user_id}/active', responses={
    status.HTTP_200_OK: {'model': active_schema.Active},
    status.HTTP_400_BAD_REQUEST: {'model': bad_request_schema.BadRequest},
})
async def delete_user_active(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await user_crud.get_user(db, user_id)

    if user is None:
        return JSONResponse(
            status_code=400,
            content=jsonable_encoder( bad_request_schema.BadRequest(detail='User not found') )
        )

    active = await active_crud.delete_active(db, user)
    return active