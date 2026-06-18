# models.py
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime
from datetime import datetime

class Base(DeclarativeBase):
    pass


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str]
    venue: Mapped[str]
    address: Mapped[str]
    city: Mapped[str]
    state: Mapped[str]
    post_code: Mapped[str]
    country: Mapped[str]
    max_attendees: Mapped[int]
    start_date: Mapped[datetime] = mapped_column(DateTime)
    end_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    adminid: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime)