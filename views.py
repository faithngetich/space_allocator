# from models.migrate import eng
# from sqlalchemy.orm import sessionmaker
from models.persons import Fellow
from models.persons import Staff
from models.rooms import LivingSpace
from models.rooms import OfficeSpace
from models.rooms import Room


class Amity(object):
    all_staff = []
    all_fellows = [{"person_type" : "fellow", "person_name" : "Tetio"}]
    living_spaces = [{"room_type" : "living_space", "room_name" : "Vazlhala"}]
    offices = []
    accomodation_list = []
    allocated_rooms = {}

    def create_room(self, list_of_rooms, room_type):        
        pass

    def add_person(self, person):
        pass

    def reallocate_person(self, person_id, new_room_name):
        pass
    
    def print_allocations(self):
        pass
    
    def print_unallocated(self):
        pass
    
    def print_room(self, room_name):
        pass

    def save_state(self):
        pass
    
    def load_state(self):
        pass

    def load_people(self, filename):
        pass

