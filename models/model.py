import os
import sys
import sqlalchemy

from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from sqlalchemy import create_engine




Base = declarative_base()


class Person(Base):
    """creates a people's table"""
    __tablename__ = "People"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    wants_accomodation = Column(Boolean)

    def __repr__(self):
        return 'first name{} last name{}'.format(self.first_name,self.last_name)


class Room(Base):
    """creates rooms tables"""
    __tablename__ = "Rooms"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    room_type = Column(String, nullable=False)
    room_capacity = Column(Integer, nullable=False)
    occupants = Column(String,nullable=True)


class DatabaseCreator(object):
    """creating database connection to object"""
    def __init__(self, db_name=None):
        self.db_name = db_name + '.db'
        self.engine = create_engine('sqlite:///' + self.db_name)
        Base.metadata.create_all(self.engine)
        session_maker = sessionmaker(bind=self.engine)
        self.session = session_maker()

    


