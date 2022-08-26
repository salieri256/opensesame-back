import os
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import user, active, door, lock, activity_log, lock_log

ALLOW_ORIGINS = json.loads( os.environ['ALLOW_ORIGINS'] )
ALLOW_METHODS = json.loads( os.environ['ALLOW_METHODS'] )
ALLOW_HEADERS = json.loads( os.environ['ALLOW_HEADERS'] )
ALLOW_CREDENTIALS = True if os.environ['ALLOW_CREDENTIALS'] == 'True' else False

app = FastAPI()

app.include_router(user.router)
app.include_router(active.router)
app.include_router(door.router)
app.include_router(lock.router)
app.include_router(activity_log.router)
app.include_router(lock_log.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=ALLOW_CREDENTIALS,
    allow_methods=ALLOW_METHODS,
    allow_headers=ALLOW_HEADERS,
)