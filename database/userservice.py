from .models import User, UsedIds
from datetime import datetime
from database import get_db


def register_user_db(username: str, fio: str, phone_number: str, age: int, gender: str, region: str):
    db = next(get_db())

    existing_user = db.query(User).filter_by(phone_number=phone_number).first()
    if existing_user:
        return "User with this phone number already exists"

    # Определить следующий доступный идентификатор
    next_id = db.query(User.id).order_by(User.id.desc()).first()
    next_id = next_id[0] + 1 if next_id else 1

    # Проверить, не был ли этот идентификатор использован ранее
    while db.query(UsedIds).filter_by(id=next_id).first():
        next_id += 1

    new_user = User(
        id=next_id,
        username=username,
        fio=fio,
        phone_number=phone_number,
        age=age,
        gender=gender,
        region=region,
        created_at=datetime.now()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return "User successfully registered"


def delete_user_db(user_id: int):
    db = next(get_db())
    user = db.query(User).filter_by(id=user_id).first()
    if user:
        db.delete(user)
        db.commit()

        # Сохранить id в таблице использованных идентификаторов
        used_id = UsedIds(id=user.id)
        db.add(used_id)
        db.commit()
        return True
    return False


def get_all_users_db():
    db = next(get_db())
    users = db.query(User).all()
    return users


def get_detailed_user_db(user_id: int):
    db = next(get_db())
    user = db.query(User).filter_by(id=user_id).first()
    if user:
        return user
    return None


def search_user_db(query: str):
    db = next(get_db())
    users = db.query(User).filter(
        (User.username.like(f"%{query}%")) |
        (User.fio.like(f"%{query}%")) |
        (User.phone_number.like(f"%{query}%"))
    ).all()
    return users


