from sqlalchemy import Column, Integer, String
from base import Base


class Person(Base):
    __tablename__ = "People"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    type = Column(String)
    wants_accomodation = Column(Boolean)

    def __repr__(self):
        return 'name{}'.format(self.name)


class Room(Base):
    __tablename__ = "Rooms"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    type = Column(String)
    members = Column(String)


    def __repr__(self):
        return 'name{}'.format(self.name)


