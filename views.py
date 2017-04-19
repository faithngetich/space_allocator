import random
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper, sessionmaker
from models.rooms import Office, LivingSpace
from models.persons import Fellow, Staff
from models.model import (Base, Room, Person, OfficeSpaces, LivingSpaces, DatabaseCreator)



class Amity(object):
    all_staff = []
    all_fellows = []
    all_rooms = []
    office_allocations = {}
    living_space_allocations = {}
    all_people = []
    living_spaces_waiting_list = []
    office_spaces_waiting_list = []
    
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
                    print("Office {} successfully created.".format(office.room_name))
                elif room_type.upper() == 'L':
                    living_space = LivingSpace(room_name)
                    self.all_rooms.append(living_space)
                    self.living_space_allocations[living_space] = []
                    print("Living space {} successfully created.".format(living_space.room_name))

    def generate_random_office_spaces(self):
        """Generates random office"""
        offices = [room for room in self.all_rooms if room.room_type == "OFFICE"]
        available_offices = []
        for office in offices:
            if office.room_capacity < 6:
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
            if living_space.room_capacity < 4:
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
            if category is "FELLOW":
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
            else:
                # create fellow object
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
            if category is "FELLOW":
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


    