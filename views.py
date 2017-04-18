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
        if room_name.upper() in [room.room_name for room in Amity.all_rooms]:
            print("sorry, Room already exist.")
        else:
            mapping = {'O': Office, 'L': LivingSpace}
            new_room = mapping[room_type.upper()](room_name.upper())
            Amity.all_rooms.append(new_room)
            if room_type.upper() == 'O':
                Amity.office_spaces[room_name.upper()] = []
            elif room_type.upper() == 'L':
                Amity.living_spaces[room_name.upper()] = []
            print(room_name.upper() + " " + "created successfully")

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
        livingSpaces = [room for room in Amity.all_rooms if room.room_type == "LIVING_SPACE"]
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
        mapping = {"F": Fellow, "S":Staff}
        new_person = mapping[category.upper()](first_name.upper(), last_name.upper())
        Amity.all_people.append(new_person)
        allocated_office = self.generate_random_office_spaces()
        if allocated_office:
            Amity.office_spaces[allocated_office].append(new_person.full_name)
            print(new_person.full_name + " added successfully to " + allocated_office)
        else:
            print("No office space available")
        if wants_accomodation.upper() == 'Y' and category == 'F':
            allocated_living_space = self.generate_random_living_spaces()
            if allocated_living_space is None:
                print("No available living spaces")
            else:
                Amity.living_spaces[allocated_living_space].append(new_person.full_name)
                print(new_person.full_name + " added successfully to " + allocated_living_space)
        print("Adding process completed succesfully")

    def reallocate_person(self, first_name, last_name, room_type, new_room):
        """ moves person from one room to another room"""
        full_name = first_name.upper() + " " + last_name.upper()
        fellows = [person.full_name for person in Amity.all_people if person.category == "FELLOW"]
        staff = [person.full_name for person in Amity.all_people if person.category == "STAFF"]
        available_lspaces = [room.room_name for room in Amity.all_rooms 
                            if room.room_type == "LIVING_SPACE" 
                            and len(Amity.living_spaces[room.room_name]) < LivingSpace.room_capacity]
        available_offices = [room.room_name for room in Amity.all_rooms
                            if room.room_type == "OFFICE"
                            and len(Amity.office_spaces[room.room_name]) < Office.room_capacity]
        if full_name not in fellows and full_name not in staff:
            print("Sorry, the person doesn't exist.")

        elif new_room.upper() not in available_lspaces and new_room.upper() not in available_offices:
            print("The room requested does not exist or is not available")
            print("Available office \n", available_offices)
            print("Available living space \n", available_lspaces)
        else:
            if room_type.upper() == "L":
                if new_room in available_offices and new_room not in available_lspaces:
                    print("The room selected is not a living space")
                elif full_name not in fellows:
                    return "The person has to exist and be a fellow!"
                else:
                    for room in Amity.living_spaces.keys():
                        if full_name in Amity.living_spaces[room]:
                            lspace = Amity.living_spaces[room]
                            lspace.remove(full_name)
                            Amity.office_spaces[new_room.upper()].append(full_name)
                            print("successfully reallocated")


space = Amity()
space.create_room('L', "MyRoom")
space.create_room('O', 'valhala')
space.add_person('faith', 'dede', 'F', 'Y')

space.reallocate_person('faith', 'dede', 'L', 'valhala')
print(Amity.living_spaces)
print(Amity.office_spaces)
print(space.reallocate_person('faith', 'dede', 'L', 'valhala'))
print(Amity.living_spaces)
print(Amity.all_rooms)

#     def load_people(filename):
#         """loads people from a txt file to the app"""
#         with open (filename, 'r') as people_file:
#             for person_details in people_file:
#                 details = person_details.rstrip().split()
#                 accomodate = details[3] if len(details) == 4 else "N"
#                 Amity.add_person(details[0], details[1], details[2], accomodate)
#                 print("Successfully loaded people")

# space = Amity()
# space.add_person('faith', 'dede', 'F', 'Y')
# space.load_people('faith')
# print(Amity.living_spaces)
