from typing import Any, Optional
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
import src.models.log as log_model
import src.schemas.log as log_schema

async def create_log(db: AsyncSession, log_create: log_schema.Log) -> log_model.Log:
    log = log_model.Log(**log_create.dict())
    db.add(log)
    await db.commit()
    await db.refresh(log)
    return log

async def get_all_logs(db: AsyncSession) -> Any:
    statement = select(log_model.Log)
    result: Result = await db.execute(statement)
    logs = result.scalars().all()
    return logs