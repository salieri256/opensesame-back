from fastapi import FastAPI
from src.routers import user, log, door

app = FastAPI()

app.include_router(user.router)
app.include_router(log.router)
app.include_router(door.router)