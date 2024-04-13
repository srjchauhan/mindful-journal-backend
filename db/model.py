from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"


class JournalModel(Base):
    __tablename__ = "users_journals"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    journal = Column(String, nullable=False)
    prompt = Column(String, nullable=False)
    answer = Column(String, nullable=True)
    time_stamp = Column(DateTime, nullable=False, default=datetime.now())
    user_id = Column(
        Integer,
        ForeignKey(UserModel.id),
        nullable=False,
    )
    session_id = Column(String, nullable=False)

    def __repr__(self):
        return f"Journal(id={self.id}, journal={self.journal}, prompt={self.prompt}, answer={self.answer}), time_stamp={self.time_stamp}"

    def to_dict(self):
        return {
            "id": self.id,
            "journal": self.journal,
            "prompt": self.prompt,
            "answer": self.answer,
            "time_stamp": self.time_stamp.isoformat(),
        }
