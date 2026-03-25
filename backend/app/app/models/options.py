from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, TEXT, Boolean,CHAR
from sqlalchemy.sql import func
from app.db.base import Base
from sqlalchemy.orm import relationship

class Options(Base):
    __tablename__ = "options"

    option_id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("questions.question_id"))
    option_label = Column(CHAR(1))
    option_text = Column(TEXT)
    is_correct = Column(Boolean)

    questions = relationship("Questions",back_populates="user_questions")

