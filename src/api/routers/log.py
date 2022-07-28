from fastapi import APIRouter
import src.api.schemas.log as log_schema

router = APIRouter()

@router.get('/logs/active', response_model=list[log_schema.ActiveLog])
async def list_active_logs():
    return [
        log_schema.ActiveLog(id=1, isActive=False, unixTime=0, userId=1)
    ]
