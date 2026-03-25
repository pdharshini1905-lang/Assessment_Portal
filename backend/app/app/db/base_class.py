from app.db.session import engine
from app.db.base import Base
from app.models import users,questions,options,attempts,assessments,answers
# Create all tables in Railway DB

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")