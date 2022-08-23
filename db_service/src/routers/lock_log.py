from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_db
from src.libs.unix_time import get_unix_time
import src.schemas.lock_log as lock_log_schema
import src.cruds.lock_log as lock_log_crud

router = APIRouter()

@router.get('/logs/locks', responses={
    status.HTTP_200_OK: {'model': list[lock_log_schema.LockLog]},
    status.HTTP_204_NO_CONTENT: {'model': None}
})
async def get_all_lock_logs(db: AsyncSession = Depends(get_db)):
    lockLogList = await lock_log_crud.get_all_lock_logs(db)

    if len(lockLogList) == 0:
        return Response(status_code=204)

    return lockLogList



@router.post('/logs/locks', status_code=201, responses={
    status.HTTP_201_CREATED: {'model': lock_log_schema.LockLog},
})
async def create_lock_log(lock_log_body: lock_log_schema.LockLogBase, unix_time: int = Depends(get_unix_time), db: AsyncSession = Depends(get_db)):
    lockLog = await lock_log_crud.create_lock_log(db, lock_log_body, unix_time)
    return lockLog