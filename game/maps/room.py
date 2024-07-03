import random
import pygame

room_types = {
    'battle': 'Fight some monsters',
    'recipe': 'Find a recipe',
    'random': 'Random other room type'
}

unique_rooms = {
    'start': 'Start',
    'boss': 'Boss'
}

valid_rooms = room_types | unique_rooms

random_room_types = ['battle', 'recipe']

class Room:
    
    class Battle:
        def __init__(self):
            pass
        
        def raise_event(self):
            # Return a pygame event representing the battle room
            return pygame.event.Event(pygame.USEREVENT, {'room_type': 'battle'})
    
    class Recipe:
        def __init__(self):
            pass
        
        def raise_event(self):
            # Return a pygame event representing the recipe room
            return pygame.event.Event(pygame.USEREVENT, {'room_type': 'recipe'})
        
    class Random:
        def __init__(self):
            self.room = random.choice(random_room_types)()
            pass
        
        def raise_event(self):
            # Return a random pygame event representing one of the other room types
            return self.room.raise_event()
        
    class Boss:
        def __init__(self):
            pass
        
        def raise_event(self):
            # Return a pygame event representing the boss room
            return pygame.event.Event(pygame.USEREVENT, {'room_type': 'boss'})

    class Start:
        def __init__(self):
            pass
        
        def raise_event(self):
            # Return a pygame event representing the start room
            return pygame.event.Event(pygame.USEREVENT, {'room_type': 'start'})
        
        
class RoomFactory:
    def __init__(self):
        return
    
    def createRoom(self, room_type:str='random') -> Room:
        room_type = room_type.lower()
        if room_type not in (valid_rooms):
            raise ValueError(f'Invalid room type: {room_type}, must be one of {valid_rooms.keys()}')
        room_class = getattr(Room, room_type.title())
        return room_class()

    def randomizeRoom(self) -> Room:
        return self.createRoom(random.choice(random_room_types))