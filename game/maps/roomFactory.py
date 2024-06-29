from .room import Room, room_types
import random


class RoomFactory:
    def __init__(self):
        return
    
    def newRoom(self, room_type) -> Room:
        return Room(room_type)

    def randomRoom(self) -> Room:
        return Room(random.choice(list(room_types.keys()[:-2]))) # Don't include boss or start rooms
    
    
    
