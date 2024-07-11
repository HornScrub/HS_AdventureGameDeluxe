import pygame
from player import Player
from level import Level

class Game:
    def __init__(self, display):
        self.display = display
        self.screen = display.get_screen()
        self.screen_width = display.screen_width
        self.screen_height = display.screen_height
        self.player = Player(self.screen_width, self.screen_height)
        self.level = Level(self.screen_width, self.screen_height)

    def handle_event(self, event):
        self.player.handle_event(event)

    def update(self):
        self.player.update(self.level)

    def render(self):
        # Clear the screen with a background color
        self.screen.fill((0,0,0))

        # Draw the level
        self.level.render(self.screen)

        # Draw the player
        self.player.render(self.screen)

        # Update all our new renders
        pygame.display.flip()
