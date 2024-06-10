from fastapi import APIRouter, HTTPException
from database.userservice import *

users_router = APIRouter(tags=['Управление пользователями'], prefix='/users')


@users_router.post('/api/register_user')
async def register_new_user(
        username: str,
        fio: str,
        phone_number: str,
        age: int,
        region: str,
        gender: str = None
):

    new_user = register_user_db(
        username=username,
        fio=fio,
        phone_number=phone_number,
        age=age,
        region=region,
        gender=gender
    )

    if new_user != "User successfully registered":
        raise HTTPException(status_code=400, detail=new_user)
    return {"message": new_user}


@users_router.delete('/api/delete_account')
async def delete_user(
        user_id: int
):
    result = delete_user_db(user_id)
    if result:
        raise HTTPException(status_code=404, detail=result)
    return {"message": result}


@users_router.get('/api/get_all_users')
async def get_all_users():
    users = get_all_users_db()
    return {"users": users}


@users_router.get('/api/get_detailed_user')
async def get_detailed_user(
        user_id: int
):
    user = get_detailed_user_db(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@users_router.get('/api/search_user')
async def search_user(
        query: str
):
    result = search_user_db(query)
    if result:
        return {'detail': result}
    return {'Такого пользователя нету'}


