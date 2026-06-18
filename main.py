from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from models import Event, Base
from schemas import EventCreate
from sqlalchemy import create_engine
from datetime import datetime
from sqlalchemy.orm import Session
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # Vite dev server
        "http://127.0.0.1:5173",
        "https://your-frontend-domain.com"  # production later
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
engine = create_engine(os.getenv("db_connection"))
Base.metadata.create_all(engine)


@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get("/status")
async def status():
    return {"status": "Rockin", "message": "Hamlin 4 Champ"}

@app.post("/createevent")
async def signuphandler(event: EventCreate):
    try:
        db_event = Event(
            name=event.name,
            venue=event.venue,
            address=event.address,
            city=event.city,
            state=event.state,
            post_code=event.postCode,
            country=event.country,
            max_attendees=event.maxAttendees,
            start_date=event.startDate,
            end_date=event.endDate,
            adminid=event.adminid,
            created_at=datetime.now()
        )

        with Session(engine) as session:
            session.add(db_event)
            session.commit()

        return {"status": "success"}
    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))