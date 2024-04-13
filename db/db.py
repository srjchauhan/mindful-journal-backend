from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Configure database connection details (replace with your credentials)
DATABASE_URL = "sqlite:///data/journal.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    from model import UserModel, JournalModel
    UserModel.metadata.create_all(engine)
    JournalModel.metadata.create_all(engine)
