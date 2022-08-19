from fastapi import FastAPI
from src.routers import user, active, lock, log

app = FastAPI()

app.include_router(user.router)
app.include_router(active.router)
app.include_router(lock.router)
app.include_router(log.router)