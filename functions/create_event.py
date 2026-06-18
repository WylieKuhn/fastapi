from sqlalchemy import create_engine, DateTime
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
from DONOTPUSH.db_info import db_connection
from datetime import date, datetime
from pydantic import BaseModel


def create_event(name, venue, address, city, state, postCode,
                 country, maxAttendees, start, end, adminID
                 ):

    class Base(DeclarativeBase):
        pass

    class Event(Base):
        __tablename__="events"
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
        end_date: Mapped[datetime] = mapped_column(DateTime)
        moderators: Mapped[list[str]]
        uid: Mapped[str]
        created_at: Mapped[datetime] = mapped_column(DateTime)

    engine = create_engine(
        db_connection
    )

    Base.metadata.create_all(engine)

    new_user = Event( 
        name=name, 
        venue=venue, 
        address=address,
        city=city,
        state=state,
        post_code=postCode,
        country=country,
        max_attendees=maxAttendees,
        start_date=start,
        end_date=end,
        moderators=[adminID],
        uid=adminID,
        created_at=datetime.now()
    )
        
    with Session(engine) as session:
        session.add(new_user)
        session.commit()