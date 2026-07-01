from pydantic import BaseModel


class ChatRequest(BaseModel):

    document_id: int

    session_id: int

    question: str

    language: str = "English"