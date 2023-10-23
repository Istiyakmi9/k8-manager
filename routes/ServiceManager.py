from fastapi import APIRouter, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List
from pydantic import BaseModel, Field
from datetime import date

from fastapi.responses import JSONResponse

from enum import IntEnum
from models.request_model import RequestModel

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


@route.get("/", response_class=HTMLResponse)
async def get(request: Request):
    pipelines = [{
        "Status": int(Status.Running),
        "PipelineId": "#123456789",
        "Trigger": "Developer",
        "Commit": "Message",
        "Stages": 1,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 1
    }, {
        "Status": int(Status.Failed),
        "PipelineId": "#123456789",
        "Trigger": "Developer",
        "Commit": "Message",
        "Stages": 2,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 2
    }, {
        "Status": int(Status.Passed),
        "PipelineId": "#123456789",
        "Trigger": "Developer",
        "Commit": "Message",
        "Stages": 3,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 3
    }, {
        "Status": int(Status.Running),
        "PipelineId": "#123456789",
        "Trigger": "Developer",
        "Commit": "Message",
        "Stages": 4,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 4
    }, {
        "Status": int(Status.Running),
        "PipelineId": "#123456789",
        "Trigger": "Developer",
        "Commit": "Message",
        "Stages": 1,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 5
    }, {
        "Status": int(Status.Warning),
        "PipelineId": "#123456789",
        "Trigger": "Developer",
        "Commit": "Message",
        "Stages": 4,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 6
    }]

    return templates.TemplateResponse("index.html", {"request": request, "pipelines": pipelines})


@route.put("/service/{id}")
def start_service(id: int, request_data: RequestModel) -> Response:
    print(id)
    print(request_data)
    return JSONResponse(content={"message": "hello"})
