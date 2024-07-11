import pygame
import sys

# Initialize pygame modules


class Display:
    def __init__(self, settings):
        self.screen_width = settings['screen_width']
        self.screen_height = settings['screen_height']
        self.fullscreen = settings['fullscreen']

        if self.fullscreen:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        pygame.display.set_caption("AdventureGameDeluxe")

    def get_screen(self):
        return self.screen