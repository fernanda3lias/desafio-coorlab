# API Connection

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from finder import get_option

app = FastAPI()
info = {"city": "", "date": ""}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  
    allow_headers=["*"],  
)

class FormData(BaseModel):
    city: str
    day: str


@app.post("/submit-form")
async def submit_form(data: FormData):
    global info
    info = {"city": data.city, "date": data.day}
    return {"city": data.city, "date": data.day}


@app.get("/submit-form")
async def get_form():
    global info
    global results
    results = get_option(info["city"])

    return results


    
