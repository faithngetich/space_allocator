class Person(object):
    def __init__(self, first_name, last_name):
        self.person_id = id(self)
        self.first_name = first_name
        self.last_name = last_name
        self.wants_accomodation = 'N'

class Staff(Person):

    wants_accomodation = "N"
    category = "staff"

    def __init__(self, first_name, last_name):
        """Override the init method of Person superclass."""
        super(Staff, self).__init__(first_name, last_name)

    def __str__(self):
        """To make Staff class human readable."""
        return "{} {}".format(self.first_name, self.last_name)

class Fellow(Person):
    
    wants_accomodation = "N"
    category = "fellow"

    def __init__(self, first_name, last_name):
        """Override the init method of Person superclass."""
        super(Fellow, self).__init__(first_name, last_name)

    def __str__(self):
        """To make fellow class human readable."""
        return "{} {}".format(self.first_name, self.last_name)

