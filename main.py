from fastapi import FastAPI
from routes.ServiceManager import route

app = FastAPI()


app.include_router(route)


