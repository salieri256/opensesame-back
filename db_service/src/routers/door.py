from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_db
import src.schemas.door as door_schema
import src.cruds.door as door_crud

router = APIRouter()

@router.get('/doors', responses={
    status.HTTP_200_OK: {'model': list[door_schema.Door]},
    status.HTTP_204_NO_CONTENT: {'model': None},
})
async def get_all_doors(db: AsyncSession = Depends(get_db)):
    doorList = await door_crud.get_all_doors(db)

    if len(doorList) == 0:
        return JSONResponse(status_code=204, content=None)

    return doorList



@router.post('/doors', status_code=201, responses={
    status.HTTP_201_CREATED: {'model': door_schema.Door},
})
async def create_door(door_body: door_schema.DoorBase, db: AsyncSession = Depends(get_db)):
    door = await door_crud.create_door(db, door_body)
    return door



@router.get('/doors/{door_id}', responses={
    status.HTTP_200_OK: {'model': door_schema.Door},
    status.HTTP_400_BAD_REQUEST: {'model': {'detail': str}},
})
async def get_door(door_id: int, db: AsyncSession = Depends(get_db)):
    door = await door_crud.get_door(db, door_id)

    if door is None:
        raise HTTPException(status_code=400, detail='Door not found')
    
    return door



@router.put('/doors/{door_id}', responses={
    status.HTTP_200_OK: {'model': door_schema.Door},
    status.HTTP_400_BAD_REQUEST: {'model': {'detail': str}},
})
async def update_door(door_id: int, door_body: door_schema.DoorBase, db: AsyncSession = Depends(get_db)):
    door = await door_crud.get_door(db, door_id)

    if door is None:
        raise HTTPException(status_code=400, detail='Door not found')

    return await door_crud.update_door(db, door_body, door)



@router.delete('/doors/{door_id}', status_code=204, responses={
    status.HTTP_204_NO_CONTENT: {'model': None},
    status.HTTP_400_BAD_REQUEST: {'model': {'detail': str}},
})
async def delete_door(door_id: int, db: AsyncSession = Depends(get_db)):
    door = await door_crud.get_door(db, door_id)

    if door is None:
        raise HTTPException(status_code=400, detail='Door not found')

    return await door_crud.delete_door(db, door)