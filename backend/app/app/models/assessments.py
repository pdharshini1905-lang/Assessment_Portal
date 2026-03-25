from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.app.db.base import Base

class Assessments(Base):
    __tablename__ = "assessments"

    assessment_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    total_questions = Column(Integer)
    duration_minutes = Column(Integer)
    pass_mark = Column(Integer)