from sqlalchemy import JSON, Column, Integer, String, TIMESTAMP, ForeignKey, TEXT
from sqlalchemy.sql import func
from app.db.base import Base
from sqlalchemy.orm import relationship

class Questions(Base):
    __tablename__ = "questions"

    question_id = Column(Integer, primary_key=True)
    assessments_id = Column(Integer, ForeignKey("assessments.assessment_id"))

    question_type = Column(String(255))
    question_text = Column(JSON)
    question_section = Column(String(255))
    question_sectionid = Column(Integer,ForeignKey("section.section_id"))
    correct_option = Column(String(1))
