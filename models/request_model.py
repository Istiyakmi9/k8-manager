from datetime import date
from pydantic import BaseModel


class RequestModel(BaseModel):
    Status: int
    PipelineId: str
    Project: str
    Trigger: str
    Commit: str
    Stages: int
    UpdatedOn: date
    RunTime: date
    ProjectId: int
