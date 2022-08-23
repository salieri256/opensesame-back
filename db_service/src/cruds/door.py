from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
import src.models.door as door_model
import src.schemas.door as door_schema

async def create_door(db: AsyncSession, door_base: door_schema.DoorBase) -> door_model.Door:
    door = door_model.Door(**door_base.dict())

    db.add(door)
    await db.commit()
    await db.refresh(door)

    return door



async def get_all_doors(db: AsyncSession) -> list[door_model.Door]:
    statement = select(door_model.Door)
    result: Result = await db.execute(statement)
    doors = result.scalars().all()
    return doors



async def get_door(db: AsyncSession, door_id: int) -> door_model.Door | None:
    statement = select(door_model.Door).filter(door_model.Door.id == door_id)
    result: Result = await db.execute(statement)
    door = result.first()
    return door[0] if door is not None else None



async def update_door(db: AsyncSession, door_base: door_schema.DoorBase, original: door_model.Door) -> door_model.Door:
    original.name = door_base.name

    db.add(original)
    await db.commit()
    await db.refresh(original)

    return original



async def delete_door(db: AsyncSession, original: door_model.Door) -> None:
    await db.delete(original)
    await db.commit()