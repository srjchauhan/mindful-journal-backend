from pydantic import BaseModel


class Journal(BaseModel):
    journal: str
    prompt: list[str]


class JournalResponse(BaseModel):
    status: str
    data: list[Journal]


class PromptAnswer(BaseModel):
    prompt: str
    answer: str


class JournalAnswerRequest(BaseModel):
    journal: str
    data: list[PromptAnswer]
