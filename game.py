import pygame
from player import Player

class Game:
    def __init__(self, display):
        self.display = display
        self.screen = display.get_screen()
        self.player = Player()

    def handle_event(self, event):
        self.player.handle_event(event)

    def update(self):
        self.player.update()

    def render(self):
        self.screen.fill((0,0,0))
        self.player.render(self.screen)
