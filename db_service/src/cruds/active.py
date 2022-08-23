from sqlalchemy.ext.asyncio import AsyncSession
import src.models.user as user_model
import src.schemas.active as active_schema

async def create_active(db: AsyncSession, original: user_model.User) -> active_schema.Active:
    original.isActive = True
    
    db.add(original)
    await db.commit()
    await db.refresh(original)

    return active_schema.Active(isActive=original.isActive)



async def get_active(db: AsyncSession, original: user_model.User) -> active_schema.Active:
    return active_schema.Active(isActive=original.isActive)



async def delete_active(db: AsyncSession, original: user_model.User) -> active_schema.Active:
    original.isActive = False

    db.add(original)
    await db.commit()
    await db.refresh(original)

    return active_schema.Active(isActive=original.isActive)