class Room(object):
    def __init__(self, room_name):
        self.room_id = id(self)
        self.room_name = room_name