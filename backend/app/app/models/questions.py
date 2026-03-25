from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, TEXT
from sqlalchemy.sql import func
from app.app.db.base import Base
from sqlalchemy.orm import relationship

class Questions(Base):
    __tablename__ = "questions"

    question_id = Column(Integer, primary_key=True)
    assessments_id = Column(Integer, ForeignKey("Assessments.assessment_id"))
    question_text = Column(TEXT)
    section = Column(String(100))