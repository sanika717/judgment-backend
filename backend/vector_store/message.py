from pydantic import BaseModel


class MessageResponse(BaseModel):

    id: int
    sender: str
    content: str