from sqlalchemy import Column, DateTime, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base
from sqlalchemy.orm import relationship

class Section(Base):

    __tablename__ = "section"

    section_id = Column(Integer , primary_key=True)
    section_name = Column(String(100))

    question_section = relationship("Questions",back_populates="section")

