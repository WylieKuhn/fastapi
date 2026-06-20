# schemas.py
from pydantic import BaseModel
from datetime import datetime

class EventCreate(BaseModel):
    name: str
    venue: str
    address: str
    city: str
    state: str
    postCode: str
    country: str
    maxAttendees: int
    startDate: datetime
    endDate: datetime
    adminid: str

class GetEvent(BaseModel):
    adminid:str

class GetSingleEvent(BaseModel):
    id:int