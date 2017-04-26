import random
import os.path
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper, sessionmaker
from models.rooms import Office, LivingSpace
from models.persons import Fellow, Staff
from models.model import (Base, Room, Person, DatabaseCreator)
from models.model import Base
from colorama import init
init(autoreset=True)
from termcolor import colored
from  colorama import Fore, Back, Style


class Amity(object):
    def __init__(self):
        self.all_staff = []
        self.all_fellows = []
        self.all_rooms = []
        self.office_allocations = {}
        self.living_space_allocations = {}
        self.all_people = []
        self.living_spaces_waiting_list = []
        self.office_spaces_waiting_list = []

    def create_room(self, room_type, list_of_rooms):
        
        """creates a specified room"""
        for name in  list_of_rooms:
            if name in [room.room_name.upper() for room in self.all_rooms]:
                print("sorry,{} room already exist.".format(name.upper()))
            else:
                if room_type.upper() == 'O':
                    office = Office(name)
                    self.all_rooms.append(office)
                    self.office_allocations[office.room_name] = []
                    print(Fore.GREEN + "Office {} successfully created.".format(office.room_name.upper()))
                elif room_type.upper() == 'L':
                    living_space = LivingSpace(name)
                    self.all_rooms.append(living_space)
                    self.living_space_allocations[living_space.room_name] = []
                    print(Fore.GREEN + "Living space {} successfully created.".format(living_space.room_name.upper()))
                else:
                    print("please specify the room_type you would like to create.")

    def generate_random_office_spaces(self):
        """Generates random office"""
        offices = [room for room in self.all_rooms if room.room_type == "OFFICE"]
        available_offices = []
        for office in offices:
            if len(self.office_allocations[office.room_name]) < 6:
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
            if len(self.living_space_allocations[living_space.room_name]) < 6:
                available_living_space.append(living_space)
        if available_living_space:
            selected_room = random.choice(available_living_space)
        else:
            selected_room = None
        return selected_room

    def add_person(self, first_name, last_name, category, wants_accomodation='N'):
        """Adds person to self and randomly allocates the person"""
        if wants_accomodation == "N" :
            if category is "F":
                # create fellow object and adds them to fellow list
                fellow = Fellow(first_name, last_name, wants_accomodation)
                self.all_people.append(fellow)
                self.all_fellows.append(fellow)
                allocated_office = self.generate_random_office_spaces()
                print(fellow.person_id)
                if allocated_office:
                    allocated_office.members.append(fellow)
                    # if random room selected
                    self.office_allocations[allocated_office.room_name] = allocated_office.members
                    print(Fore.GREEN +"You have allocated {} successfully to office {}".format(fellow.first_name,allocated_office.room_name))
                else:
                    self.office_spaces_waiting_list.append(fellow)
                    print("Sorry, no space available {} has been added to the office waiting list".format(fellow.first_name))
            else:
                # create staff object and adds them to list
                staff = Staff(first_name, last_name, wants_accomodation)
                self.all_staff.append(staff)
                self.all_people.append(staff)
                allocated_office = self.generate_random_office_spaces()
                print(staff.person_id)
                if allocated_office:
                    allocated_office.members.append(staff)
                    # if random room selected
                    self.office_allocations[allocated_office.room_name] = allocated_office.members
                    print(Fore.GREEN+"You have allocated {} successfully to office {}.".format(staff.first_name,allocated_office.room_name))
                else:
                    self.office_spaces_waiting_list.append(staff)
                    print(Fore.RED+"Sorry, no space available {} has been added to the living space waiting list".format(staff.first_name))
    
        # if wants accomodation
        elif category is "F":
            # create fellow object
            fellow = Fellow(first_name, last_name, wants_accomodation)
            self.all_people.append(fellow)
            self.all_fellows.append(fellow)
            allocated_office = self.generate_random_office_spaces()
            print(fellow.person_id)
            if allocated_office:
                # if random room selected
                allocated_office.members.append(fellow)
                self.office_allocations[allocated_office.room_name] = allocated_office.members
                print(Fore.GREEN+"You have allocated {} successfully to office {}".format(fellow.first_name,allocated_office.room_name))
            else:
                self.office_spaces_waiting_list.append(fellow)
                print(Fore.RED+"Sorry, no space available {} has been added to the waiting list".format(fellow.first_name))
            
            # add living space
            allocated_living_space = self.generate_random_living_spaces()
            if allocated_living_space:
                allocated_living_space.members.append(fellow)
                print(allocated_living_space)
                self.living_space_allocations[allocated_living_space.room_name] = allocated_living_space.members
                print(Fore.GREEN+"You have allocated {} successfully to living space {} ".format(fellow.first_name, allocated_living_space.room_name))
            else:
                self.living_spaces_waiting_list.append(fellow)
                print(Fore.RED+"Sorry, no space available {} has been added to the waiting list".format(fellow.first_name))
        else:
            if category == "S":
                print("Sorry! staff is not entitled to a living space")
                return "staff cannot be allocated to living space"
               
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
                    return room
        else:
            return "There are no rooms available"

    def get_person_room(self, person_id, room_type):
        """To return currently allocated room given a valid person id"""
        result = None
        if room_type is "O":
            for room in self.office_allocations.keys():
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
        # gets person object from person id
        person_object = self.get_person(person_id)
        if person_object == "Invalid person id":
            # prints id does not exist
            print(person_object)
            return person_object
        elif person_object == "There are no people in the system.":
            print("There are no people in the system. Add person(s) first to the system, then reallocate")
            return person_object
        else:
            new_room_object = self.get_room(new_room_name)
            print(new_room_object)
            if new_room_object == "Room name does not exist":
                return "Room name does not exist"
            elif new_room_object == "There are no rooms available":
                return "There are no rooms available"
            else:
                if person_object.category == "STAFF" and new_room_object.room_type == "LIVING_SPACE":
                    print(Fore.RED + "Cannot reallocate staff to living space.")
                    return "Cannot reallocate staff to living space."
                elif new_room_object.room_type == "OFFICE":
                    current_room = self.get_person_room(person_id, "O")
                    if current_room == "Person not allocated to room":
                        # if person has no office
                        cprint("{} has no current office space,hence you cannot reallocate".format(person_object.first_name))
                        return "person has no current office space, hence canot reallocate"
                    elif current_room == new_room_object:
                        print("Cannot reallocate a person to the same room.")
                        return "Cannot reallocate to same room."
                    else:
                        # remove from current office
                        self.office_allocations[current_room].remove(person_object)
                        # append to new room
                        self.office_allocations[new_room_object.room_name].append(person_object)
                        print(Fore.GREEN + "{} {} has been reallocated from office {} to {}".format(person_object.first_name,person_object.last_name, current_room,new_room_object))
                        return "Has been reallocated from  office"
                            
    def load_people(self, filename):
        """loads people from a txt file to the app"""
        with open (filename, 'r') as people_file:
            for person_details in people_file:
                details = person_details.rstrip().split()
                accomodate = details[3] if len(details) == 4 else "N"
                self.add_person(details[0], details[1], details[2], accomodate)
                print(Fore.GREEN + "Successfully loaded people to the app.")
                return "Successfully loaded people"


    def print_allocations(self,file_name=None):
        """Prints a list of allocations onto the screen"""
        print(Fore.MAGENTA + "=" * 30 + "\n" + "Office Allocations\n" + "=" *30)
        for room in self.office_allocations.keys():
            if room != "None":
                print ("\n" +Fore.BLUE + room.upper())
                for person in selfre.office_allocations[room]:
                    print(person)
                    
        print(Fore.MAGENTA + "=" * 30 + "\n" + "Living spaces Allocations\n" + "=" *30)
        for room in self.living_space_allocations.keys():
            if room != "None":
                print ("\n" + Fore.BLUE +room.upper() )
                for person in self.living_space_allocations[room]:
                    print(person)
                    
        if file_name:
            nfile = open(file_name + ".txt", "a")
            for room in self.office_allocations.keys():
                if room != "None":
                    nfile.write("\n"+ room.upper() + "\n"+ "-" *30+ "\n")
                    for person in self.office_allocations[room]:
                        nfile.write(person.full_name.upper()+"\n")
            for room in self.living_space_allocations.keys():
                if room != "None":
                    nfile.write("\n" + room.upper() + "\n" + "-" * 30+ "\n")
                    for person in self.living_space_allocations[room]:
                        nfile.write(person.full_name.upper()+"\n")
            print("{}.txt has been written".format(file_name))
            return "Successfully written the file"
    
    def print_unallocated(self, file_name=None):
        """Prints all people not allocated"""
        print(Fore.MAGENTA + "=" * 30 + "\n" + "People in office allocation waiting list\n" + "=" * 30)
        unallocated_offices = self.office_spaces_waiting_list
        unallocated_living_spaces = self.living_spaces_waiting_list
        for person in unallocated_offices:
            print(person or "None")
        print(Fore.MAGENTA + "=" * 30 + "\n" + "People in Living Space waiting list\n" + "=" * 30)
        for person in unallocated_living_spaces:
            print(person or "None")
            # return person or "None"

        if file_name:
            file = open(file_name + ".txt", "a")
            file.write("=" * 30 + "\n" + "Unallocated people\n" + "=" * 30)
            for person in unallocated_offices:
                file.write("\n" + person.full_name or "None")
            for person in unallocated_living_spaces:
                file.write("\n" + person.full_name or "None")
            print(Fore.GREEN + "{}.txt written succesfully".format(file_name))

    
    def print_room(self, room_name):
        """ Prints the names of all the people in room_name on the
             screen."""
        offices = [room for room in self.office_allocations if room != "None"]
        living_spaces = [room for room in self.living_space_allocations if room != "None"]
        if not offices or not living_spaces:
            print("There are no rooms existing in the system.")
        else:
            if room_name not in offices and room_name not in living_spaces:
                print(Fore.RED + "sorry! the room does not exist")
                return "sorry! the room does not exist"
            else:
                print(Fore.MAGENTA + "=" * 30 + "\n Members \n" + "=" * 30)
                if room_name in offices:
                    for person in self.office_allocations[room_name]:
                        print(person)
                elif room_name in living_spaces:
                    for person in self.living_space_allocations[room_name]:
                        print(person)
    
    def load_state(self, db_name):
        """loads people to the app"""
        # connect to the db provided
        if os.path.exists(db_name + ".db"):
            self.engine = create_engine('sqlite:///' + db_name + ".db")
            Base.metadata.bind = self.engine
            # query all rooms and people
            SessionMaker = sessionmaker(bind=self.engine)
            session = SessionMaker()
            people = session.query(Person).all()
            rooms = session.query(Room).all()
            # save them to the current Amity instance        
            for room in rooms:
                self.create_room(room.room_type[0],[room.name])
            for person in people:
                self.add_person(person.first_name, person.last_name, person.category, person.wants_accomodation)
            print(Fore.GREEN + "Data from {} loaded to the app.".format(db_name))
            return "Successfully loaded people to the app"
        else:
            print(Fore.RED + "sorry db does not exist")
            
        

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
            for member in room.members:
                current_occupants += member.full_name
            new_room = Room(id=room.room_id, name=room.room_name.upper(), room_type=room.room_type, room_capacity=room.room_capacity, occupants=current_occupants)
            rooms.append(new_room)
        self.session.add_all(rooms)
        self.session.commit()
        # save people's data
        people = []
        for person in self.all_people:
            wants_accomodation = True if person.wants_accomodation == "Y" else False
            print(person, person.wants_accomodation)
            new_person = Person(id=person.person_id, first_name=person.first_name, last_name=person.last_name, category=person.category, wants_accomodation=wants_accomodation)
            people.append(new_person)
        # self.session.update(new_person)
        self.session.add_all(people)
        self.session.commit()
        print(Fore.GREEN +"Successfully saved people")
        return("successfully saved people")

