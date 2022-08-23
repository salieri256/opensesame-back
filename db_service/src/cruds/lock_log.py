from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
import src.models.lock_log as lock_log_model
import src.schemas.lock_log as lock_log_schema

async def create_lock_log(db: AsyncSession, lock_log_base: lock_log_schema.LockLogBase, unix_time: int) -> lock_log_model.LockLog:
    lock_log = lock_log_model.LockLog(unixTime=unix_time, **lock_log_base.dict())
    
    db.add(lock_log)
    await db.commit()
    await db.refresh(lock_log)

    return lock_log



async def get_all_lock_logs(db: AsyncSession) -> list[lock_log_model.LockLog]:
    statement = select(lock_log_model.LockLog)
    result: Result = await db.execute(statement)
    lock_logs = result.scalars().all()
    return lock_logs



async def get_lock_log(db: AsyncSession, lock_log_id: int) -> lock_log_model.LockLog | None:
    statement = select(lock_log_model.LockLog).filter(lock_log_model.LockLog.id == lock_log_id)
    result: Result = await db.execute(statement)
    lock_log = result.first()
    return lock_log[0] if lock_log is not None else None



async def update_lock_log(db: AsyncSession, lock_log_base: lock_log_schema.LockLogBase, original: lock_log_model.LockLog) -> lock_log_model.LockLog:
    original.isLocked = lock_log_base.isLocked
    original.doorId = lock_log_base.doorId
    original.userId = lock_log_base.userId
    
    db.add(original)
    await db.commit()
    await db.refresh(original)

    return original



async def delete_lock_log(db: AsyncSession, original: lock_log_model.LockLog) -> None:
    await db.delete(original)
    await db.commit()