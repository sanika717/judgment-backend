from pydantic import BaseModel
from pydantic import ConfigDict


class DocumentResponse(BaseModel):

    id: int
    title: str
    status: str
    language: str

    model_config = ConfigDict(
        from_attributes=True
    )