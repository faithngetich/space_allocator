import random
import os.path
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper, sessionmaker
from models.rooms import Office, LivingSpace
from models.persons import Fellow, Staff
from models.model import (Base, Room, Person, DatabaseCreator)
from models.model import Base

class Amity(object):
    all_staff = []
    all_fellows = []
    all_rooms = []
    office_allocations = {'None':[]}
    living_space_allocations = {'None':[]}
    all_people = []
    living_spaces_waiting_list = []
    office_spaces_waiting_list = []
    
    def create_room(self, room_type, list_of_rooms):
        """creates a specified room"""
        for name in  list_of_rooms:
            if name.upper() in [room.room_name.upper() for room in self.all_rooms]:
                print("sorry,{} Room already exist.".format(name.upper()))
            else:
                if room_type.upper() == 'O':
                    office = Office(name)
                    self.all_rooms.append(office)
                    self.office_allocations[office] = []
                    print("Office {} successfully created.".format(office.room_name))
                elif room_type.upper() == 'L':
                    living_space = LivingSpace(name)
                    self.all_rooms.append(living_space)
                    self.living_space_allocations[living_space] = []
                    print("Living space {} successfully created.".format(living_space.room_name))

    def generate_random_office_spaces(self):
        """Generates random office"""
        offices = [room for room in self.all_rooms if room.room_type == "OFFICE"]
        available_offices = []
        for office in offices:
            if len(self.office_allocations[office]) < 6:
                available_offices.append(office)
        if available_offices:
            selected_room = random.choice(available_offices)
        else:
            selected_room = None
        return selected_room

    def generate_random_living_spaces(self):
        """Generates random living spaces"""
        living_spaces = [room for room in self.all_rooms if room.room_type == "LIVING_SPACE"]
        available_living_space = []
        for living_space in living_spaces:
            if len(self.living_space_allocations[living_space]) < 6:
                available_living_space.append(living_space)
        if available_living_space:
            selected_room = random.choice(available_living_space)
        else:
            selected_room = None
        return selected_room

    def add_person(self, first_name, last_name, category, wants_accomodation='N'):
        """Adds person to self and randomly allocates the person"""
        # check if category is FELLOW
        if wants_accomodation == "N":
            if category is "F":
                # create fellow object and adds them to fellow list
                fellow = Fellow(first_name, last_name)
                Amity.all_fellows.append(fellow)
                allocated_office = self.generate_random_office_spaces()
                if allocated_office:
                    # if random room selected
                    Amity.office_allocations[allocated_office].append(fellow)
                    print("You have allocated {} successfully ".format(fellow.first_name))
                else:
                    Amity.office_spaces_waiting_list.append(fellow)
                    print("Sorry, no space available {} has been added to the waiting list".format(fellow.first_name))
            else:
                # create staff object and adds them to list
                staff = Staff(first_name, last_name)
                Amity.all_staff.append(staff)
                allocated_office = self.generate_random_office_spaces()
                if allocated_office:
                    # if random room selected
                    Amity.office_allocations[allocated_office].append(staff)
                    print("You have allocated {} successfully ".format(staff.first_name))
                else:
                    Amity.office_spaces_waiting_list.append(staff)
                    print("Sorry, no space available {} has been added to the waiting list".format(staff.first_name))
        else:
            # if wants accomodation
            if category is "F":
                # create fellow object
                fellow = Fellow(first_name, last_name)
                Amity.all_fellows.append(fellow)
                allocated_office = self.generate_random_office_spaces()
                if allocated_office:
                    # if random room selected
                    Amity.office_allocations[allocated_office].append(fellow)
                    print("You have allocated {} successfully ".format(fellow.first_name))
                else:
                    Amity.office_spaces_waiting_list.append(fellow)
                    print("Sorry, no space available {} has been added to the waiting list".format(fellow.first_name))
                
                # add living space
                allocated_living_space = self.generate_random_living_spaces()
                if allocated_living_space:
                    Amity.living_space_allocations[allocated_living_space].append(fellow)
                    print("You have allocated {} successfully to living space {} ".format(fellow.first_name, allocated_living_space.room_name))
                else:
                    Amity.living_spaces_waiting_list.append(fellow)
                    print("Sorry, no space available {} has been added to the waiting list".format(fellow.first_name))
            else:
                staff = Staff(first_name, last_name)
                Amity.all_staff.append(staff)
                allocated_office = self.generate_random_office_spaces()
                if allocated_office:
                    # if random room selected
                    Amity.office_allocations[allocated_office].append(staff)
                    print("You have allocated {} successfully ".format(staff.first_name))
                    # reject adding staff to living space
                else:
                    Amity.office_spaces_waiting_list.append(staff)
                    print("Sorry, no space available {} has been added to the waiting list".format(staff.first_name))

                
                print("Staff not entitled to living space")

    def get_person(self, person_id):
        """To return person object given person id."""
        person_object = None

        if self.all_people:
            for person in self.all_people:
                if person_id == person.person_id:
                    person_object = person
            if person_object:
                return person_object
            else:
                return "Invalid person id"
        else:
            # if all_people has no object
            return "There are no people in the system."

    def get_room(self, room_name):
        """To return room object given room name"""
        room_object = None
        if self.all_rooms:
            for room in self.all_rooms:
                if room_name == room.room_name:
                    room_object = room
            
            if room_object:
                return room_object
            else:
                return "Room name does not exist"
        else:
            return "There are no rooms available"

    def get_person_room(self, person_id, room_type):
        """To return currently allocated room."""
        result = None
        if room_type is "O":
            for room in list(self.office_allocations.keys()):
                if (person_id in [person.person_id for person in self.office_allocations[room]]):
                    # returns room object if person_id match is found
                    result = room
        elif room_type is "L":
            for room in list(self.living_space_allocations.keys()):
                if (person_id in [person.person_id for person in self.living_space_allocations[room]]):
                    result = room

        if result:
            return result
        else:
            return "Person not allocated to room"
                
    def reallocate_person(self, person_id, new_room_name):
        """ moves person from one room to another room"""
        person_object = self.get_person(person_id)
        if person_object == "Invalid person id":
            # prints id does not exist
            print(person_object)
            return person_object
        elif person_object == "There are no people in the system.":
            print("There are no people in the system. Add person(s) first, then reallocate")
            return person_object
        else:
            new_room_object = self.get_room(new_room_name)
            if new_room_object == "Room name does not exist":
                return "Room name does not exist"
            elif new_room_object == "There are no rooms available":
                return "There are no rooms available"
            # else:
            #     if new_room_object.room_type == "LIVING_SPACE":
                    
            #     current_room = 


        # full_name = first_name.upper() + " " + last_name.upper()
        # fellows = [person.full_name for person in self.all_people if person.category == "FELLOW"]
        # staff = [person.full_name for person in self.all_people if person.category == "STAFF"]
        # available_living_spaces = ([room.room_name for room in self.all_rooms if room.room_type == "LIVING_SPACE" and len(self.living_space_allocations[room.room_name]) < LivingSpace.room_capacity])
        # available_offices = [room.room_name for room in self.all_rooms
        #                     if room.room_type == "OFFICE"
        #                     and len(self.office_allocations[room.room_name]) < Office.room_capacity]
        # if full_name not in fellows and full_name not in staff:
        #     print("Sorry, the person doesn't exist.")

        # elif new_room.upper() not in available_living_spaces and new_room.upper() not in available_offices:
        #     print("The room requested does not exist or is not available")
        #     print("Available office \n", available_offices)
        #     print("Available living space \n", available_living_spaces)
        # else:
        #     if room_type.upper() == "L":
        #         if new_room in available_offices and new_room not in available_living_spaces:
        #             print("The room selected is not a living space")
        #         elif full_name not in fellows:
        #             return "The person has to exist and be a fellow!"
        #         else:
        #             for room in self.living_space_allocations.keys():
        #                 if full_name in self.living_space_allocations[room]:
        #                     lspace = self.living_space_allocations[room]
        #                     lspace.remove(full_name)
        #                     self.office_allocations[new_room.upper()].append(full_name)
        #                     print("successfully reallocated")

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
        for room in Amity.office_allocations.keys():
            if room != "None":
                print ("room" + "\n" + "+" * 30)
                for person in Amity.office_allocations[room]:
                    print(person)
        print("=" * 30 + "\n" + "Living spaces Allocations\n" + "=" *30)
        for room in Amity.living_space_allocations.keys():
            if room != "None":
                print ("room" + "\n" + "+" * 30)
                for person in Amity.living_space_allocations[room]:
                    print(person)
        if file_name:
            nfile = open(file_name + ".txt", "a")
            nfile.write("=" * 30 + "\n" + "Office Allocations\n" + "=" *30)
            for room in Amity.office_allocations[room]:
                if room != "None":
                    nfile.write(room + "\n" + "+" * 30)
                    for person in Amity.office_allocations[room]:
                        nfile.write(person)
            nfile.write("=" *30 + "\n" + "Living space Allocations\n" + "=" * 30 )
            for room in Amity.living_space_allocations[room]:
                if room != "None":
                    nfile.write(room + "\n" + "+" * 30)
                    for person in Amity.living_space_allocations[room]:
                        nfile.write(person)
            print("%s.txt written" % file)
    
    @staticmethod
    def print_unallocated(file_name=None):
        """Prints all people not allocated"""
        unallocated_offices = Amity.office_allocations["None"]
        unallocated_living_spaces = Amity.living_space_allocations["None"]
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
            print("{}.txt written succesfully".format(file_name))

    @staticmethod
    def print_room(room_name):
        """ Prints the names of all the people in room_name on the
             screen."""
        offices = [room for room in Amity.office_allocations if room != "None"]
        living_spaces = [room for room in Amity.living_space_allocations if room != "None"]
        if room_name.upper() not in offices and room_name.upper() not in living_spaces:
            print("sorry! the room does not exist")
        else:
            print("=" * 30 + "\n Members \n" + "=" * 30)
            if room_name.upper() in offices:
                for person in Amity.office_allocations[room_name.upper()]:
                    print(person)
            elif room_name.upper() in living_spaces:
                for person in Amity.living_space_allocations[room_name.upper()]:
                    print(person)
    @staticmethod
    def load_state(dbname=None):
        # connect to the db provided
        # query all rooms and people
        # save them to the current Amity instance.
       pass

    def save_state(self, db_name):
        # create a db called db_name
        self.db_name = db_name + '.db'
        self.engine = create_engine('sqlite:///' + self.db_name)
        Base.metadata.bind = self.engine
         
        # create people and rooms tables.
        Base.metadata.create_all()
        # create session
        SessionMaker = sessionmaker(bind=self.engine)
        self.session = SessionMaker()

        # save rooms 
        rooms = []
        for room in self.all_rooms:
            current_occupants = ''
            print('There are {}'.format(room.members))

            for member in room.members:
                current_occupants += member.full_name
            new_room = Room(id=room.room_id, name=room.room_name.upper(), room_type=room.room_type, room_capacity=room.room_capacity, occupants=current_occupants)
            rooms.append(new_room)
        self.session.add_all(rooms)
        self.session.commit()
        # save people's data
        people = []
        for person in self.all_people:
            new_person = Person(id=person.person_id, name=person.full_name, category=person.category, wants_accomodation=person.wants_accomodation)
            people.append(new_person)
        # self.session.update(new_person)
        self.session.add_all(people)
        self.session.commit()

space = Amity()
# # space.create_room('O', ["MyRoom"])
# space.create_room('O', ['VaLhAla'])
# space.create_room('O', ['valhala'])
# space.create_room('L', ['Ruby','Narnia'])

# space.add_person('faith', 'dede', 'F', 'Y')


# space.reallocate_person('faith', 'dede', 'L', 'valhala')
# print(Amity.living_spaces)
# print(Amity.office_spaces)
# print(space.reallocate_person('faith', 'dede', 'L', 'valhala'))
# print(Amity.living_spaces)
# print(Amity.all_rooms)
# space = Amity()
# space.add_person('faith', 'dede', 'F', 'Y')

# *******************

# space.load_people("people.txt")
space.save_state("faha")
# space.print_allocations()
# space.print_unallocated()
# space.print_room('elda')

# *******************

# print(Amity.living_spaces)

