import pygame
from enum import Enum
from scenes.intro import IntroScene
from scenes.mainmenu import MainMenuScene
from scenes.map import MapScene
from scenes.room import RoomScene
from scenes.battle import BattleScene
from scenes.gameover import GameOver
from scenes.credits import CreditScene
from scenes.m import MScene
from common import Scene

class SceneManager:
    def __init__(self):
        self.scenes = {
            Scene.INTRO: IntroScene(),
            Scene.MAINMENU: MainMenuScene(),
            Scene.MAP: MapScene(),
            Scene.ROOM: RoomScene(),
            Scene.BATTLE: BattleScene(),
            Scene.GAMEOVER: GameOver(),
            Scene.CREDITS: CreditScene(),
            Scene.M: MScene()
        }
        self.current_scene = Scene.INTRO
    
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHTBRACKET:
                scenelist = list(Scene)
                self.current_scene = scenelist[(scenelist.index(self.current_scene) + 1) % len(scenelist)]
            if event.key == pygame.K_LEFTBRACKET:
                scenelist = list(Scene)
                self.current_scene = scenelist[(scenelist.index(self.current_scene) - 1) % len(scenelist)]
        next_scene_name = self.scenes[self.current_scene].handle_input(event)
        if next_scene_name != 'quit' and next_scene_name in self.scenes:
            self.current_scene = next_scene_name
        return next_scene_name

    def update(self):
        next_scene_name = self.scenes[self.current_scene].update()
        if next_scene_name != 'quit' and next_scene_name in self.scenes:
            self.current_scene = next_scene_name

    def render(self, screen):
        self.scenes[self.current_scene].render(screen)
