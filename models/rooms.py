class Room(object):
    def __init__(self, room_name):
        self.room_id = id(self)
        self.room_name = room_name

class Office(Room):

    room_type = "office"
    room_capacity = 6 

    def __init__(self, room_name):
        """Override the init method of Person superclass."""
        super(Office, self).__init__(room_name)

    def __str__(self):
        """To make office class human readable."""
        return "{}".format(self.room_name)

class LivingSpace(Room):
    
    room_type = "living_space" 
    room_capacity = 4

    def __init__(self, room_name):
        """Override the init method of Person superclass."""
        super(LivingSpace, self).__init__(room_name)

    def __str__(self):
        """To make living space class human readable."""
        return "{}".format(self.room_name)

