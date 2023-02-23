from pydantic import BaseModel


class TodoResModel(BaseModel):
    id: str
    title: str
    description: str
    done: bool
