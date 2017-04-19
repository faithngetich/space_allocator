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
    office_allocations = {}
    living_space_allocations = {}
    all_people = []
    living_spaces = {'None' : []}
    office_spaces = {'None' : []}
    accomodation_list = []
    allocated_rooms = {}

    def create_room(self, room_type, list_of_rooms):
        """creates a specified room"""
        for room_name in  list_of_rooms:
            if room_name.upper() in [room.room_name for room in self.all_rooms]:
                print("sorry, Room already exist.")
            else:
                if room_type.upper() == 'O':
                    office = Office(room_name)
                    self.all_rooms.append(office)
                    self.office_allocations[office] = []
                    self.office_spaces[room_name.upper()] = []
                    print("Office {} successfully created.".format(office.room_name))
                elif room_type.upper() == 'L':
                    self.living_spaces[room_name.upper()] = []
                    living_space = LivingSpace(room_name)
                    self.all_rooms.append(living_space)
                    self.living_space_allocations[living_space] = []
                    print("Living space {} successfully created.".format(living_space.room_name))

    def generate_random_office_spaces(self):
        """Generates random office"""
        offices = [room for room in self.all_rooms if room.room_type == "OFFICE"]
        available_offices = []
        for office in offices:
            if office.room_capacity > len(self.office_spaces[office.room_name.upper()]):
                available_offices.append(office.room_name)
        if len(available_offices):
            selected_room = random.choice(available_offices)
        else:
            selected_room = None
        return selected_room

    def generate_random_living_spaces(self):
        """Generates random living spaces"""
        livingSpaces = [room for room in self.all_rooms if room.room_type == "LIVING_SPACE"]
        available_living_space = []
        for living_space in livingSpaces:
            if living_space.room_capacity > len(self.living_spaces[living_space.room_name.upper()]):
                available_living_space.append(living_space.room_name)
        if len(available_living_space):
            selected_room = random.choice(available_living_space)
        else:
            selected_room = None
        return selected_room

    def add_person(self, first_name, last_name, category, wants_accomodation='N'):
        """Adds person to self and randomly allocates the person"""
        mapping = {"F": Fellow, "S":Staff}
        new_person = mapping[category.upper()](first_name.upper(), last_name.upper())
        print("NEW {}".format(new_person))
        self.all_people.append(new_person)
        print(self.all_people)
        allocated_office = self.generate_random_office_spaces()
        if allocated_office:
            self.office_spaces[allocated_office.upper()].append(new_person.full_name)
            print(new_person.full_name + " added successfully to " + allocated_office)
        else:
            print("No office space available")
        if wants_accomodation.upper() == 'Y' and category == 'F':
            allocated_living_space = self.generate_random_living_spaces()
            if allocated_living_space is None:
                print("No available living spaces")
            else:
                self.living_spaces[allocated_living_space.upper()].append(new_person.full_name)
                print(new_person.full_name + " added successfully to " + allocated_living_space)
        print("Adding process completed succesfully")

    def reallocate_person(self, first_name, last_name, room_type, new_room):
        """ moves person from one room to another room"""
        full_name = first_name.upper() + " " + last_name.upper()
        fellows = [person.full_name for person in self.all_people if person.category == "FELLOW"]
        staff = [person.full_name for person in self.all_people if person.category == "STAFF"]
        available_lspaces = [room.room_name for room in self.all_rooms 
                            if room.room_type == "LIVING_SPACE" 
                            and len(self.living_spaces[room.room_name]) < LivingSpace.room_capacity]
        available_offices = [room.room_name for room in self.all_rooms
                            if room.room_type == "OFFICE"
                            and len(self.office_spaces[room.room_name]) < Office.room_capacity]
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
                    for room in self.living_spaces.keys():
                        if full_name in self.living_spaces[room]:
                            lspace = self.living_spaces[room]
                            lspace.remove(full_name)
                            self.office_spaces[new_room.upper()].append(full_name)
                            print("successfully reallocated")

    def load_people(self, filename):
        """loads people from a txt file to the app"""
        with open (filename, 'r') as people_file:
            for person_details in people_file:
                details = person_details.rstrip().split()
                accomodate = details[3] if len(details) == 4 else "N"
                self.add_person(details[0], details[1], details[2], accomodate)
                print("Successfully loaded people")

    @staticmethod
    def print_allocations(file_name=None):
        """Prints a list of allocations onto the screen"""
        print("=" * 30 + "\n" + "Office Allocations\n" + "=" *30)
        for room in Amity.office_spaces.keys():
            if room != "None":
                print (room + "\n" + "+" * 30)
                for person in Amity.office_spaces[room]:
                    print(person)
        print("=" * 30 + "\n" + "Living spaces Allocations\n" + "=" *30)
        for room in Amity.living_spaces.keys():
            if room != "None":
                print (room + "\n" + "+" * 30)
                for person in Amity.living_spaces[room]:
                    print(person)
        if file_name:
            nfile = open(file_name + ".txt", "a")
            nfile.write("=" * 30 + "\n" + "Office Allocations\n" + "=" *30)
            for room in Amity.office_spaces[room]:
                if room != "None":
                    nfile.write(room + "\n" + "+" * 30)
                    for person in Amity.office_spaces[room]:
                        nfile.write(person)
            nfile.write("=" *30 + "\n" + "Living space Allocations\n" + "=" * 30 )
            for room in Amity.living_spaces[room]:
                if room != "None":
                    nfile.write(room + "\n" + "+" * 30)
                    for person in Amity.living_spaces[room]:
                        nfile.write(person)
            print("%s.txt written" % file)
    
    @staticmethod
    def print_unallocated(file_name=None):
        """Prints all people not allocated"""
        unallocated_offices = Amity.office_spaces["None"]
        unallocated_living_spaces = Amity.living_spaces["None"]
        print("=" * 30 + "\n" + "No offices\n" + "=" * 30)
        for person in unallocated_offices:
            print(person or "None")
        print("=" * 30 + "\n" + "Living Spaces\n" + "=" * 30)
        for person in unallocated_living_spaces:
            print(person or "None")

        if file_name:
            file = open(file_name + ".txt", "a")
            file.write("=" * 30 + "\n" + "No offices\n" + "=" * 30)
            for person in unallocated_offices:
                file.write("\n" + person or "None")
            file.write("=" * 30 + "\n" + "No living spaces\n" + "=" * 30)
            for person in unallocated_living_spaces:
                file.write("\n" + person or "None")
            print("%s.txt written succesfully", file_name)

    @staticmethod
    def print_room(room_name):
        """ Prints the names of all the people in room_name on the
             screen."""
        offices = [room for room in Amity.office_spaces if room != "None"]
        living_spaces = [room for room in Amity.living_spaces if room != "None"]
        if room_name.upper() not in offices and room_name.upper() not in living_spaces:
            print("sorry! the room does not exist")
        else:
            print("=" * 30 + "\n Members \n" + "=" * 30)
            if room_name.upper() in offices:
                for person in Amity.office_spaces[room_name.upper()]:
                    print(person)
            elif room_name.upper() in living_spaces:
                for person in Amity.living_spaces[room_name.upper()]:
                    print(person)
            
    
   