from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_db
import src.schemas.bad_request as bad_request_schema
import src.schemas.lock as lock_schema
import src.cruds.door as door_crud
import src.cruds.lock as lock_crud

router = APIRouter()

@router.get('/doors/{door_id}/lock', responses={
    status.HTTP_200_OK: {'model': lock_schema.Lock},
    status.HTTP_400_BAD_REQUEST: {'model': bad_request_schema.BadRequest},
})
async def get_door_lock(door_id: int, db: AsyncSession = Depends(get_db)):
    door = await door_crud.get_door(db, door_id)

    if door is None:
        return JSONResponse(
            status_code=400,
            content=jsonable_encoder( bad_request_schema.BadRequest(detail='User not found') )
        )
    
    lock = await lock_crud.get_lock(db, door)
    return lock



@router.post('/doors/{door_id}/lock', responses={
    status.HTTP_200_OK: {'model': lock_schema.Lock},
    status.HTTP_400_BAD_REQUEST: {'model': bad_request_schema.BadRequest},
})
async def create_door_lock(door_id: int, db: AsyncSession = Depends(get_db)):
    door = await door_crud.get_door(db, door_id)

    if door is None:
        return JSONResponse(
            status_code=400,
            content=jsonable_encoder( bad_request_schema.BadRequest(detail='User not found') )
        )

    lock = await lock_crud.create_lock(db, door)
    return lock



@router.delete('/doors/{door_id}/lock', responses={
    status.HTTP_200_OK: {'model': lock_schema.Lock},
    status.HTTP_400_BAD_REQUEST: {'model': bad_request_schema.BadRequest},
})
async def delete_door_lock(door_id: int, db: AsyncSession = Depends(get_db)):
    door = await door_crud.get_door(db, door_id)

    if door is None:
        return JSONResponse(
            status_code=400,
            content=jsonable_encoder( bad_request_schema.BadRequest(detail='User not found') )
        )

    lock = await lock_crud.delete_lock(db, door)
    return lock