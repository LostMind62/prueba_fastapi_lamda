from fastapi import FastAPI ,APIRouter

from mangum import Mangum

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}


handler = Mangum(app)