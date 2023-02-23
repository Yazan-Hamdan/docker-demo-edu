from pydantic import BaseModel


class TodoReqModel(BaseModel):
    title: str
    description: str
