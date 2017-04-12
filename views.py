# from models.migrate import eng
# from sqlalchemy.orm import sessionmaker
from models.persons import Fellow
from models.persons import Staff
from models.rooms import LivingSpace
from models.rooms import OfficeSpace
from models.rooms import Room


class Amity(object):
    def __init__(self):
        self.all_staff = []
        self.all_fellows = [{"person_type" : "fellow", "person_name" : "Tetio"}]
        self.living_spaces = [{"room_type" : "living_space", "room_name" : "Vazlhala"}]
        self.offices = []
        self.accomodation_list = []
        self.allocated_rooms = {}

    def create_room(self, room):        
        if room["room_type"] == "office":
            for rooms in self.offices:
                if room["room_name"] == rooms["room_name"]:
                    print( "\n" + rooms.room_name.upper()+"already exists. \n")
                    return
                else:
                    new_office = OfficeSpace(room["room_name"])
                    self.offices.append(new_office)
                    text = ("\n You have successfully added " + new_office.room_name.upper() + " to offices in amity")
                    print(text)
        else:
            if self.living_spaces:
                for rooms in self.living_spaces:
                    if room["room_name"] == rooms["room_name"]:
                        print( "\n" + rooms["room_name"].upper()+"already exists. \n")
                        return
                    else:
                        new_livingSpace = room["room_name"]
                        self.living_spaces.append(new_livingSpace)
                        text = ("\n You have successfully added" + new_livingSpace.upper() + "to living space in amity")
                        print(text)
                        return
# amity = Amity()
# amity.create_room({"room_type" : "living_space", "room_name" : "Valhala"})

    def add_person(self, person):
        if person["person_type"] == "fellow":
            for people in self.all_fellows:
                if person["person_name"] == people["person_name"]:
                    print("\n"+person["person_name"].upper()+"already exists.\n")
                    return
                else:
                    new_person = person["person_name"]
                    # new_person.accomodation = person["wants_accomodation"]
                    self.all_fellows.append(new_person)
                    print("you have added"+new_person.upper()+"as a staff to the list")
                    return
        else:
            if self.staff:
                for people in self.all_staff:
                    if person["person_name"] == people["person_name"]:
                        print("\n"+person["person_name"].upper()+"already exists.\n")
                        return
                    else:      
                        new_person = person["staff_name"]
                        new_person.accomodation = person["wants_accomodation"]
                        self.all_fellows.append(new_person)
                        print("you have added"+new_person.person.upper()+"as a fellow to the list")
                        return

# amity = Amity()
# amity.add_person({"person_type" : "fellow", "person_name" : "Ebrahim"})

    # def reallocate_person(self, name, newroom):
    #     pass

    # def load_people():
    #     pass

    # def print_allocations(self):
    #     session.query(Person).all()

    # def print_unallocated(self, name):
    #     pass

    # def print_room(self, rname):
    #     rs = ses.query(room).all()
    #     for room in rs:
    #         print(room.Name)

    # def get_list_of_fellows(self):
    #     return self.all_fellows

    # def get_list_of_offices(self):
    #     return self.offices

    # def get_list_of_living_spaces(self):
    #     return self.living_spaces

    # def get_list_of_staff(self):
    #     return self.all_staff

