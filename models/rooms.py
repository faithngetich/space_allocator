class Room(object):
    def __init__(self, room_name):
        self.room_id = id(self)
        self.room_name = room_name

    def __str__(self):
        """To make the class human readable."""
        return "{}".format(self.room_name.upper())

class Office(Room):

    room_type = "OFFICE"
    room_capacity = 6

    def __init__(self, room_name):
        """Override the init method of Person superclass."""
        super(Office, self).__init__(room_name)
        
        self.members = []

class LivingSpace(Room):
    
    room_type = "LIVING_SPACE" 
    room_capacity = 4

    def __init__(self, room_name):
        """Override the init method of Person superclass."""
        super(LivingSpace, self).__init__(room_name)

        self.members = []

    
