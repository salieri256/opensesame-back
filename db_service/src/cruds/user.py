from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
import src.models.user as user_model
import src.schemas.user as user_schema

async def create_user(db: AsyncSession, user_base: user_schema.UserBase) -> user_model.User:
    user = user_model.User(**user_base.dict())

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user



async def get_all_users(db: AsyncSession) -> list[user_model.User]:
    statement = select(user_model.User)
    result: Result = await db.execute(statement)
    users = result.scalars().all()
    return users



async def get_user(db: AsyncSession, user_id: int) -> user_model.User | None:
    statement = select(user_model.User).filter(user_model.User.id == user_id)
    result: Result = await db.execute(statement)
    user = result.first()
    return user[0] if user is not None else None



async def update_user(db: AsyncSession, user_base: user_schema.UserBase, original: user_model.User) -> user_model.User:
    original.name = user_base.name
    original.nfcId = user_base.nfcId

    db.add(original)
    await db.commit()
    await db.refresh(original)

    return original



async def delete_user(db: AsyncSession, original: user_model.User) -> None:
    await db.delete(original)
    await db.commit()