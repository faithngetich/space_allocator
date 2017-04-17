# from models.migrate import eng
# from sqlalchemy.orm import sessionmaker
from models.rooms import Office
from models.rooms import LivingSpace
from models.persons import Fellow
from models.persons import Staff

import random

class Amity(object):
    all_staff = []
    all_fellows = []
    all_rooms = []
    all_people = []
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
            new_room = mapping[room_type.upper()](room_name.upper())
            Amity.all_rooms.append(new_room)
            if room_type.upper() == 'O':
                Amity.office_spaces[room_name.upper()] = []
            elif room_type.upper() == 'L':
                Amity.living_spaces[room_name.upper()] = []
            print(room_name.upper() + "created successfully")

    def generate_random_office_spaces(self):
        """Generates random office"""
        offices = [room for room in Amity.all_rooms if room.room_type == "OFFICE"]
        available_offices = []
        for office in offices:
            if office.room_capacity > len(Amity.office_spaces[office.room_name]):
                available_offices.append(office.room_name)

            # selected_room = 'None'

        if len(available_offices):
            selected_room = random.choice(available_offices)
        else:
            selected_room = None
        return selected_room

    def generate_random_living_spaces(self):
        """Generates random living spaces"""
        # self.create_room('L', "MyRoom")
        livingSpaces = [room for room in Amity.all_rooms if room.room_type == "living_space"]
        available_living_space = []
        for living_space in livingSpaces:
            if living_space.room_capacity > len(Amity.living_spaces[living_space.room_name]):
                available_living_space.append(living_space.room_name)

        if len(available_living_space):
            selected_room = random.choice(available_living_space)
        else:
            selected_room = None
        return selected_room

    def add_person(self, first_name, last_name, category, wants_accomodation='N'):
        """Adds person to Amity and randomly allocates the person"""
        amity = Amity()
        allocated_office = self.generate_random_office_spaces()
        if allocated_office:
            mapping = {"F": Fellow, "S":Staff}
            person_id = len (Amity.all_people) + 1
            new_person = mapping[category.upper()](person_id, first_name.upper(),last_name.upper(), category)
            Amity.all_people.append(new_person)
            Amity.office_spaces[allocated_office].append(first_name.upper() + " " + last_name.upper())
        else:
            print("No office space available")
        if wants_accomodation.upper() == 'Y' and category == 'F':
            
            allocated_living_space = self.generate_random_living_spaces()
            amity.living_spaces[allocated_living_space].append(first_name.upper() + "" + last_name.upper())
        print("Adding process completed succesfully")
    
# create = Amity()            
# amity = create.add_person("faith", "tet", "F", "Y")
# print(amity)
    
       
