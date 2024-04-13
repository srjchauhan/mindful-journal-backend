import uvicorn
from app import app
from db.model import UserModel, JournalModel
from db import engine

if __name__ == "__main__":
    UserModel.metadata.create_all(engine)
    JournalModel.metadata.create_all(engine)
    uvicorn.run(app, host="0.0.0.0", port=8181)