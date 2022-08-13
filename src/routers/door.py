from fastapi import APIRouter, Depends
from src.libs.door import Door, get_door

router = APIRouter()

@router.put('/door/lock', response_model=None)
async def lock_door(door: Door = Depends(get_door)):
    door.lock()

@router.delete('/door/lock', response_model=None)
async def unlock_door(door: Door = Depends(get_door)):
    door.unlock()