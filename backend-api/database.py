import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/medisalud")

# Retry connecting to database in case it is booting up
engine = None
for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        connection.close()
        print("Successfully connected to the database!")
        break
    except Exception as e:
        print(f"Database connection attempt {i+1}/10 failed. Retrying in 3 seconds...")
        time.sleep(3)

if not engine:
    # Fallback to create the engine anyway so the server fails quickly if needed
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
