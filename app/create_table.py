from app.database import engine
from app.models import Base

print("Creating employee table...")
Base.metadata.create_all(bind=engine)
print("Employee table created successfully in fastapi_db!")
