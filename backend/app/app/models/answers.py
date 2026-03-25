from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base


class   Answers(Base):
    __tablename__ = "answers"

    answer_id = Column(Integer, primary_key=True)
    attempt_id = Column(Integer, ForeignKey("attempts.attempt_id"))
    question_id = Column(Integer, ForeignKey("questions.question_id"))
    selected_option_id = Column(Integer)
