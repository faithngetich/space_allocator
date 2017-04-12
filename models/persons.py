class Person(object):
    def __init__(self,name):
        self.name = name
        self.assigned_office = ""

    def __repr__(self):
        return self.__class__.__name__

class Staff(Person):
    def __init__(self, person):
        super(Staff, self).__init__(person)
        self.accomodation = "None"
        self.assigned_liningSpace = "None"

class Fellow(Person):
    def __init__(self, person):
        super(Fellow, self).__init__(person)
        self.accomodation = ""
        self.assigned_liningSpace = ""

    


       

   
        