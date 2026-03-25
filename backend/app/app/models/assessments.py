from sqlalchemy import Column, DateTime, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base

class Assessments(Base):
    __tablename__ = "assessments"

    assessment_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    total_questions = Column(Integer)
    pass_mark=Column(Integer)
    total_mark=Column(Integer)
    duration_minutes = Column(Integer)
    level=Column(String(255))
    Created_At = Column(DateTime, server_default=func.now())
    Updated_At = Column(DateTime, server_default=func.now(), onupdate=func.now())

  