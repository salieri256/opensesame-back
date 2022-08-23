from fastapi import FastAPI, Depends, Response
from src.door import Door, get_door

app = FastAPI()

@app.post('/lock')
def lock_door(door: Door = Depends(get_door)):
    door.lock()
    return Response()

@app.delete('/lock')
def unlock_door(door: Door = Depends(get_door)):
    door.unlock()
    return Response()