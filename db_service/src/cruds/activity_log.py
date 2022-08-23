from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
import src.models.activity_log as activity_log_model
import src.schemas.activity_log as activity_log_schema

async def create_activity_log(db: AsyncSession, activity_log_base: activity_log_schema.ActivityLogBase, unix_time: int) -> activity_log_model.ActivityLog:
    activity_log = activity_log_model.ActivityLog(unixTime=unix_time, **activity_log_base.dict())
    
    db.add(activity_log)
    await db.commit()
    await db.refresh(activity_log)

    return activity_log



async def get_all_activity_logs(db: AsyncSession) -> list[activity_log_model.ActivityLog]:
    statement = select(activity_log_model.ActivityLog)
    result: Result = await db.execute(statement)
    activity_logs = result.scalars().all()
    return activity_logs



async def get_activity_log(db: AsyncSession, activity_log_id: int) -> activity_log_model.User | None:
    statement = select(activity_log_model.ActivityLog).filter(activity_log_model.ActivityLog.id == activity_log_id)
    result: Result = await db.execute(statement)
    activity_log = result.first()
    return activity_log[0] if activity_log is not None else None



async def update_activity_log(db: AsyncSession, activity_log_base: activity_log_schema.ActivityLogBase, original: activity_log_model.ActivityLog) -> activity_log_model.ActivityLog:
    original.isActive = activity_log_base.isActive
    original.userId = activity_log_base.userId
    
    db.add(original)
    await db.commit()
    await db.refresh(original)

    return original



async def delete_activity_log(db: AsyncSession, original: activity_log_model.ActivityLog) -> None:
    await db.delete(original)
    await db.commit()