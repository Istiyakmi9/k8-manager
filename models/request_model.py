from pydantic import BaseModel


class RequestModel(BaseModel):
    application_name: str
    delay: int
    action: str
