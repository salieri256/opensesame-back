from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_db
import src.schemas.lock as lock_schema
import src.cruds.lock as lock_crud

router = APIRouter()

@router.get('/doors/{door_id}/lock', responses={
    status.HTTP_200_OK: {'model': lock_schema.Lock},
    status.HTTP_400_BAD_REQUEST: {'model': None},
})
async def get_lock(door_id: int, db: AsyncSession = Depends(get_db)):
    lock = await lock_crud.get_lock(db, door_id)

    if lock == None:
        raise HTTPException(status_code=400, detail='Door not locked')
    
    return lock



@router.post('/doors/{door_id}/lock', responses={
    status.HTTP_201_CREATED: {'model': lock_schema.Lock}
})
async def create_lock(door_id: int, db: AsyncSession = Depends(get_db)):
    return lock_crud.create_lock(db, door_id)



@router.delete('/doors/{door_id}/lock', responses={
    status.HTTP_204_NO_CONTENT: {'model': lock_schema.Lock},
    status.HTTP_400_BAD_REQUEST: {'model': None},
})
async def delete_lock(door_id: int, db: AsyncSession = Depends(get_db)):
    lock = await lock_crud.get_lock(db, door_id)

    if lock == None:
        raise HTTPException(status_code=400, detail='Door not locked')
    
    return await lock_crud.delete_lock(db, lock)