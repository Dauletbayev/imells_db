from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# Подключение к базе данных/создание базы данных
# SQLALCHEMY_DATABASE_URL = 'sqlite:///data.db'
### postgres: logi, 1234: password ###
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:1234@localhost/imells'
# Создание движка бд
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=20, max_overflow=10)
# Переменная для создания сессий
SessionLocal = sessionmaker(bind=engine)
# Создание шаблона для базы классов бд
Base = declarative_base()

# Создание сессий


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
