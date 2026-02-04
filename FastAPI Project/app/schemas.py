from pydantic import BaseModel


class exPost(BaseModel):
    title: str
    content: str
