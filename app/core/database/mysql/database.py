from typing import Iterator

from app.dependencies import get_settings
from app.config import Settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

__SETTINGS: Settings = get_settings()

__SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}".format(
    **dict(__SETTINGS)
)

engine = create_engine(__SQLALCHEMY_DATABASE_URI, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> Iterator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
