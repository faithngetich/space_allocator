# from models.migrate import eng
# from sqlalchemy.orm import sessionmaker
from models.rooms import Office
from models.rooms import LivingSpace
class Amity(object):
    all_staff = []
    all_fellows = []
    all_rooms = []
    living_spaces = {'None' : []}
    office_spaces = {'None' : []}
    accomodation_list = []
    allocated_rooms = {}

    def create_room(self, room_type, room_name):
        """creates a specified room""" 
        if room_name.upper() in [room.name for room in Amity.all_rooms]:
            print("sorry, Room already exist.")
        else:
            mapping = {'O': Office, 'L': LivingSpace}
            new_room = mapping[room_type.upper()], (room_name.upper())
            Amity.all_rooms.append(new_room)
            if room_type.upper() == 'O':
                Amity.office_spaces[room_name.upper()] = []
            elif room_type.upper() == 'L':
                Amity.living_spaces[room_name.upper()] = []
            print(room_name.upper() + "created successfully")

space = Amity()
space.create_room('O', 'valahala') 
print(Amity.all_rooms)

# create = Amity()            
# amity = create.create_room("office", "tet")
# print(amity.room_type,amity.room_name)
    
       
    # def add_person(self, person):
    #     pass

    # def reallocate_person(self, person_id, new_room_name):
    #     pass
    
    # def print_allocations(self):
    #     pass
    
    # def print_unallocated(self):
    #     pass
    
    # def print_room(self, room_name):
    #     pass

    # def save_state(self):
    #     pass
    
    # def load_state(self):
    #     pass

    # def load_people(self, filename):
    #     pass

