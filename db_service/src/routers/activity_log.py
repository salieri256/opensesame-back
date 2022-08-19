from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_db
from src.libs.unix_time import get_unix_time
import src.schemas.activity_log as activity_log_schema
import src.cruds.activity_log as activity_log_crud

router = APIRouter()

@router.get('/logs/activities', responses={
    status.HTTP_200_OK: {'model': list[activity_log_schema.ActivityLog]},
    status.HTTP_204_NO_CONTENT: {'model': None}
})
async def get_all_lock_logs(db: AsyncSession = Depends(get_db)):
    activityLogList = await activity_log_crud.get_all_activity_logs(db)

    if len(activityLogList) == 0:
        return JSONResponse(status_code=204, content=None)

    return activityLogList



@router.post('/logs/activities', status_code=201, responses={
    status.HTTP_201_CREATED: {'model': activity_log_schema.ActivityLog},
})
async def create_lock_log(activity_log_body: activity_log_schema.ActivityLogBase, unix_time: int = Depends(get_unix_time), db: AsyncSession = Depends(get_db)):
    activityLog = await activity_log_crud.create_activity_log(db, activity_log_body)
    return activityLog