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

class Room:
    
    class Battle:
        def __init__(self):
            pass
        
        def get_event(self):
            # Return a pygame event representing the battle room
            return pygame.event.Event(pygame.USEREVENT, {'room_type': 'battle'})
    
    class Recipe:
        def __init__(self):
            pass
        
        def get_event(self):
            # Return a pygame event representing the recipe room
            return pygame.event.Event(pygame.USEREVENT, {'room_type': 'recipe'})
        
    class Random:
        def __init__(self):
            pass
        
        def get_event(self):
            # Return a random pygame event representing one of the other room types
            room_type = random.choice(['battle', 'recipe', 'boss', 'start'])
            return pygame.event.Event(pygame.USEREVENT, {'room_type': room_type})
        
    class Boss:
        def __init__(self):
            pass
        
        def get_event(self):
            # Return a pygame event representing the boss room
            return pygame.event.Event(pygame.USEREVENT, {'room_type': 'boss'})

    class Start:
        def __init__(self):
            pass
        
        def get_event(self):
            # Return a pygame event representing the start room
            return pygame.event.Event(pygame.USEREVENT, {'room_type': 'start'})
        
        
class RoomFactory:
    def __init__(self):
        return
    
    def newRoom(self, room_type: str) -> Room:
        room_class = getattr(Room, room_type.title())
        if room_class is None:
            room_class = Room.Random
        return room_class()

    def randomRoom(self) -> Room:
        return Room.Random()