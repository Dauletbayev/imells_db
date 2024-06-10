from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True)
    fio = Column(String)
    phone_number = Column(String, unique=True)
    age = Column(Integer)
    gender = Column(String, default='None')
    region = Column(String)
    order_count = Column(Integer, default=0)  # Количество заказов
    frequent_tariff = Column(String)
    created_at = Column(DateTime)


class UsedIds(Base):
    __tablename__ = 'used_ids'
    id = Column(Integer, primary_key=True, autoincrement=False)
    used = Column(Boolean, default=True)
