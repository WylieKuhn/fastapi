from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
from DONOTPUSH.db_info import db_connection
from datetime import date
from pydantic import BaseModel


def signUp(firebaseID, firstName, lastName, displayName, email, birthDate):

    class Base(DeclarativeBase):
        pass

    class User(Base):
        __tablename__="users"
        id: Mapped[int] = mapped_column(primary_key=True)
        firebase_id: Mapped[str]
        first_name: Mapped[str]
        last_name: Mapped[str]
        display_name: Mapped[str]
        email: Mapped[str]
        birthday: Mapped[date]
        created_at: Mapped[date]

    engine = create_engine(
        db_connection
    )

    Base.metadata.create_all(engine)

    new_user = User(
        firebase_id=firebaseID, 
        first_name=firstName, 
        last_name=lastName, 
        display_name=displayName,
        email=email,
        birthday = birthDate,
        created_at = date.today(),
    )
        



    with Session(engine) as session:
        session.add(new_user)
        session.commit()