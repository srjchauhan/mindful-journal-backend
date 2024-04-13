import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import desc
from db import get_db
from db.model import JournalModel
from llm import LLM
from routers.model import JournalAnswerRequest
from datetime import datetime
from .utils import get_current_user

router = APIRouter(
    prefix="/journal",
    tags=["journal"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/get_journals",
)
async def get_journal(
    text: str, llm: LLM = Depends(LLM), user=Depends(get_current_user)
):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    chat_message = llm.user_prompt(text)
    journal = llm.get_journal(chat_message)
    return journal


@router.post(
    "/post_journal",
)
async def post_journal(
    journal: JournalAnswerRequest, user=Depends(get_current_user), db=Depends(get_db)
):
    session_id = str(uuid.uuid4())
    time = datetime.now()
    for i in journal.data:
        new_journal = JournalModel(
            user_id=user.id,
            journal=journal.journal,
            prompt=i.prompt,
            answer=i.answer,
            session_id=session_id,
            time_stamp=time,
        )
        db.add(new_journal)
        db.commit()
    return {"message": "Journal created successfully!"}


@router.get("/get_user_journals")
async def get_user_journals(user=Depends(get_current_user), db=Depends(get_db)):
    journals = (
        db.query(JournalModel)
        .filter(JournalModel.user_id == user.id)
        .order_by(desc(JournalModel.id))
        .all()
    )
    print(journals, "journals")
    all_journals = {}
    for journal in journals:
        if journal.session_id in all_journals:
            all_journals[journal.session_id]["data"].append(
                {"prompt": journal.prompt, "answer": journal.answer}
            )
        else:
            all_journals[journal.session_id] = {
                "data": [{"prompt": journal.prompt, "answer": journal.answer}],
                "time_stamp": journal.time_stamp.timestamp(),
                "journal": journal.journal,
            }
    data = [
        {
            "journal": all_journals[i]["journal"],
            "data": all_journals[i]["data"],
            "time_stamp": all_journals[i]["time_stamp"],
        }
        for i in all_journals.keys()
    ]
    return {"data": data}


@router.get("/random_journals")
async def random_journal(user=Depends(get_current_user), llm: LLM = Depends(LLM)):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    journal = llm.get_random_journal()
    return journal
