from models.migrate import eng
from sqlalchemy.orm import sessionmaker
from models.room import Room
from models.person import Person
class Amity():
    
    def __init__(self):
        Session = sessionmaker(bind=eng)
        self.session = Session()
        self.all_staff = []
        self.all_fellows = []
        self.living_spaces = []
        self.offices = []
        self.accomodation_list = []
        self.allocated_rooms = {}
    
    def create_room(self, rtype, rname):
        self.session.add(Room(name=rname, type=rtype, members=''))
        self.session.commit()
       
    def list_rooms(self):
        rs = ses.query(room).all()
        for room in rs:
            print room.Name
    
        
        
    def add_person(self, name, occupation, wants_accomodation = 'N'):
        self.session.add(Person(name=name, type=occupation, wants_accomodation='N'))
        self.session.commit()
    
        # self.name = name
        # self.occupation = occupation
    
    def reallocate_person(self, name, newroom):
        pass

    def load_people():
        pass

    def print_allocations(self):
        pass

    def print_unallocated(self, name):
        pass

    def print_room(self, rname):
        pass