from sqlalchemy.ext.asyncio import AsyncSession
import src.models.door as door_model
import src.schemas.lock as lock_schema

async def create_lock(db: AsyncSession, original: door_model.Door) -> lock_schema.Lock:
    original.isLocked = True
    
    db.add(original)
    await db.commit()
    await db.refresh(original)

    return lock_schema.Lock(isLocked=original.isLocked)



async def get_lock(db: AsyncSession, original: door_model.Door) -> lock_schema.Lock:
    return lock_schema.Lock(isLocked=original.isLocked)



async def delete_lock(db: AsyncSession, original: door_model.Door) -> lock_schema.Lock:
    original.isLocked = False

    db.add(original)
    await db.commit()
    await db.refresh(original)

    return lock_schema.Lock(isLocked=original.isLocked)