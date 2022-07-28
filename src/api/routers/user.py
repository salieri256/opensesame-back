from fastapi import APIRouter
import src.api.schemas.user as user_schema

router = APIRouter()

@router.get('/users', response_model=list[user_schema.User])
async def list_users():
    return [
        user_schema.User(id=1, name='Alice Bob', isActive=False, uidList=['0123456789abcdef'])
    ]

@router.post('/users', response_model=user_schema.UserCreateResponse)
async def create_user(user_body: user_schema.UserCreate):
    return user_schema.UserCreateResponse(id=1, isActive=False, **user_body.dict())

@router.put('/users/{user_id}', response_model=user_schema.UserCreateResponse)
async def update_user(user_id: int, user_body: user_schema.UserCreate):
    return user_schema.UserCreateResponse(id=user_id, isActive=False, **user_body.dict())

@router.delete('/users/{user_id}', response_model=None)
async def delete_user(user_id: int):
    return
