import os
import json
from fastapi import FastAPI, Depends, Response
from fastapi.middleware.cors import CORSMiddleware
from src.door import Door, get_door

ALLOW_ORIGINS = json.loads( os.environ['ALLOW_ORIGINS'] )
ALLOW_METHODS = json.loads( os.environ['ALLOW_METHODS'] )
ALLOW_HEADERS = json.loads( os.environ['ALLOW_HEADERS'] )
ALLOW_CREDENTIALS = True if os.environ['ALLOW_CREDENTIALS'] == 'True' else False

app = FastAPI()

@app.post('/lock')
def lock_door(door: Door = Depends(get_door)):
    door.lock()
    return Response()

@app.delete('/lock')
def unlock_door(door: Door = Depends(get_door)):
    door.unlock()
    return Response()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=ALLOW_CREDENTIALS,
    allow_methods=ALLOW_METHODS,
    allow_headers=ALLOW_HEADERS,
)