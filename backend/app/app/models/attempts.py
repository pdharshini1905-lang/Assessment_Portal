from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, TEXT, Boolean
from sqlalchemy.sql import func
from app.app.db.base import Base
from sqlalchemy.orm import relationship

class Attempts(Base):
    __tablename__ = "attempts"

    attempt_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("Users.user_id"))
    assessment_id = Column(Integer, ForeignKey("Assessments.assessment_id"))
    started_at = Column(TIMESTAMP, default=func.now())
    submitted_at = Column(TIMESTAMP, default=func.now())
    score = Column(Integer)