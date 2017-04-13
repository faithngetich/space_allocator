class Room(object):
    def __init__(self, room_name):
        self.room_id = id(self)
        self.room_name = room_name

class Office(Room):

    room_type = "office" 

    def __init__(self, room_name):
        """Override the init method of Person superclass."""
        super(Office, self).__init__(room_name)

    def __str__(self):
        """To make office class human readable."""
        return "{}".format(self.room_name)

class Living_space(Room):
    
    room_type = "living_space" 

    def __init__(self, room_name):
        """Override the init method of Person superclass."""
        super(Living_space, self).__init__(room_name)

    def __str__(self):
        """To make living space class human readable."""
        return "{}".format(self.room_name)

space = Living_space("Ruby")
print(space.room_id, space.room_name, space.room_type) 