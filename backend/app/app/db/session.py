from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.db.base import Base  # <- use full package path
from app.models import *     # <- import all models here

# Railway DB connection string
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:didEVuyzVUBZueyqVLuiSerouAzVTZyd@centerbeam.proxy.rlwy.net:59069/portal"

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()