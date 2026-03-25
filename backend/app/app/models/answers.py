from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Boolean
from sqlalchemy.sql import func
from app.db.base import Base
from sqlalchemy.orm import relationship


class Answers(Base):
    __tablename__ = "answers"

    answer_id = Column(Integer, primary_key=True)
    attempt_id = Column(Integer, ForeignKey("attempts.attempt_id"))
    question_id = Column(Integer, ForeignKey("questions.question_id"))
    selected_option_id = Column(Integer)
    is_skipped = Column(Boolean(0))

    answer = relationship("Attempts",back_populates="attempt_answer")
    question = relationship("Questions",back_populates="attempt_question")

