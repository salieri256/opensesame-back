from fastapi import APIRouter

router = APIRouter()

@router.get('/logs/active')
async def list_active_logs():
    pass
