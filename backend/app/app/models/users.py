from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from app.app.db.base import Base


class Users(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    password = Column(String(255))
    created_at = Column(TIMESTAMP, default=func.now())