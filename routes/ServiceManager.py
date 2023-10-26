from fastapi import APIRouter, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List, Dict
from pydantic import BaseModel, Field
from datetime import date
import json

from fastapi.responses import JSONResponse

from enum import IntEnum
from models.request_model import RequestModel
from service.job_service import JobStarter

route = APIRouter()
templates = Jinja2Templates(directory="templates")


class Status(IntEnum):
    Passed = 1
    Failed = 2
    Running = 3
    Warning = 4


class Student(BaseModel):
    id: int
    name: str = Field(None, title="name of student", max_length=10)
    subjects: List[str] = []


@route.post("/students/")
async def student_data(s1: Student):
    return s1


@route.get("/api")
async def get(request: Request) -> list[dict]:
    pipelines = [{
        "Status": int(Status.Running),
        "PipelineId": "#123456789",
        "Project": "Mysql Service",
        "Trigger": "restart",
        "Commit": "Message",
        "Stages": 1,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 1
    }, {
        "Status": int(Status.Failed),
        "PipelineId": "#123456789",
        "Project": "EMS Server",
        "Trigger": "none",
        "Commit": "Message",
        "Stages": 2,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 2
    }, {
        "Status": int(Status.Passed),
        "PipelineId": "#123456789",
        "Project": "EMS UI",
        "Trigger": "none",
        "Commit": "Message",
        "Stages": 3,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 3
    }, {
        "Status": int(Status.Running),
        "PipelineId": "#123456789",
        "Project": "BottomHalf Site",
        "Trigger": "none",
        "Commit": "Message",
        "Stages": 4,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 4
    }, {
        "Status": int(Status.Running),
        "PipelineId": "#123456789",
        "Project": "New Project",
        "Trigger": "none",
        "Commit": "Message",
        "Stages": 1,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 5
    }, {
        "Status": int(Status.Warning),
        "PipelineId": "#123456789",
        "Project": "New Project 2",
        "Trigger": "none",
        "Commit": "Message",
        "Stages": 4,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 6
    }]

    return pipelines


@route.put("/api/service/{id}")
def start_service(id: int, request_data: RequestModel) -> Response:
    job = JobStarter()
    job.run_service(request_data)
    return JSONResponse(content={"message": "hello"})
