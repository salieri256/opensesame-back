from fastapi import FastAPI
from src.routers import user, active, door, lock, activity_log, lock_log

app = FastAPI()

app.include_router(user.router)
app.include_router(active.router)
app.include_router(door.router)
app.include_router(lock.router)
app.include_router(activity_log.router)
app.include_router(lock_log.router)