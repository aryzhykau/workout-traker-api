from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from mongoengine import *
from config import MONGO_CONNECTION_STRING
from entities.trainer.crud import get_questionnaire



connect(host=MONGO_CONNECTION_STRING)



app = FastAPI(title="workout-tracker-api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", status_code=200)
def healthcheck():
    return "OK"

@app.get("/trainers/{trainer_id}/questionnaire", tags=["trainers","questionaire"])
def get_questionnaire(trainer_id: str):
    questionnaire = get_questionnaire(tg_id=int(trainer_id))
    return questionnaire


@app.post("/trainers/{trainer_id}/questionnaire", tags=['trainers', 'questionnaire'])
def create_questionnaire(trainer_id: str):
    response = create_questionnaire(tg_id=trainer_id)





