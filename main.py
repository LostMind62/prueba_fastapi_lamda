from fastapi import FastAPI ,APIRouter
from fastapi import BackgroundTasks, FastAPI, Request, Form,Response
from pydantic import BaseModel
from jinja2 import Environment, FileSystemLoader, Template
from starlette.responses import HTMLResponse, FileResponse
from datetime import datetime
import pdfkit
import os
from mangum import Mangum

try:
    from mysql_conn import MySQLConnection
    from variables import Variable
except Exception as e:
    print("error" + str(e))


from mangum import Mangum

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}


handler = Mangum(app)