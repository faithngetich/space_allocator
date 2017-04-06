from sqlalchemy import Column, Integer, String, Boolean
from base import Base


class Room(Base):
    __tablename__ = "Rooms"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    type = Column(String)
    members = Column(String)




    def __repr__(self):
        return 'name{}'.format(self.name)