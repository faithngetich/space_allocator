from base import Base
from sqlalchemy import create_engine
from person import Person
from room import Room

eng = create_engine('sqlite:///amity.db')

Base.metadata.bind = eng
Base.metadata.create_all()