class Person(object):
    def __init__(self, first_name, last_name, wants_accomodation):
        self.person_id = id(self)
        self.first_name = first_name
        self.last_name = last_name
        self.wants_accomodation = wants_accomodation

    @property
    def full_name(self):
       return self.first_name + " " + self.last_name

    def __str__(self):
        """To make Staff  human readable."""
        return "{} {}".format(self.first_name.upper(), self.last_name.upper())

    def __repr__(self):
        return 'first_name:{}, last_name:{}'.format(self.first_name.upper(),self.last_name.upper())
class Staff(Person):

    category = "STAFF"

    def __init__(self, first_name, last_name, wants_accomodation):
        """Override the init method of Person superclass."""
        super(Staff, self).__init__(first_name, last_name, wants_accomodation)
  

class Fellow(Person):
    
    category = "FELLOW"

    def __init__(self, first_name, last_name, wants_accomodation):
        """Override the init method of Person superclass."""
        super(Fellow, self).__init__(first_name, last_name, wants_accomodation)

