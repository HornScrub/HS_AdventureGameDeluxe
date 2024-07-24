import pygame
import os
import sys

from display import Display
from player import Player
from level import Level
from ui import UI
from vision import Vision
## from camera import Camera

# Settings dictionary
settings = {
        'screen_width' : 800,
        'screen_height': 600,
        'fullscreen' : False
}

class Game:
    def __init__(self):
        self.display = Display(settings)
        self.screen = self.display.get_screen()
        self.screen_width = settings['screen_width']
        self.screen_height = settings['screen_height']
        self.level = Level(settings['screen_width'], settings['screen_height'])
        self.player = Player(self.level)
        self.ui = UI()
        self.vision = Vision()
        ## self.camera = Camera()
    
    def handle_event(self, event):
        # Events like mouse and keyboard events to control movement and orientation
        self.player.handle_event(event)
        # Events like mouse and keyboard events to control inventory or character stat menu navigation
        self.ui.handle_event(event)
        # Events like mouse movement to control change in level presentation
        ##self.camera.handle_event(event)

    def update(self):
        self.player.update(self.level)
        ##self.level.update(self.player, self.camera)
        self.ui.update(self.display, self.player)
        ##self.camera.update()

    def render(self, screen, display):
        self.screen.fill((0, 0, 0)) # Clear screen with black color

        self.vision.render(self.screen, self.player.rect.center, pygame.mouse.get_pos())
        
        self.level.render(self.screen)
        self.player.render(self.screen)
        self.ui.render(self.screen)
    
        pygame.display.flip() # Update the full display surface to the screen

def main():

    # Initialize pygame modules
    ''' pygame is made up of several submodules that handle different
            aspects of game development, such as:
            Display module: Manages the creation and updating of game window
            Event module: Handles user input events, like keyboard presses and
                mouse movements
            Image module: Loads and manipulates images.
            Time module: Manages time-related functions, like setting frame rate.
            Mixer module: Handles sound and music.
            Font module: Renders text on the screen.'''
    
    pygame.init()

    # Apply fullscreen setting if enabled
    flags = pygame.FULLSCREEN if settings['fullscreen'] else 0
    # Create a window object
    window = pygame.display.set_mode((settings['screen_width'], settings['screen_height']), flags)
    pygame.display.set_caption("Adventure Game Deluxe")

    # Create a clock object to manage the frame rate
    clock = pygame.time.Clock()
    fps = 60 # Caps the frame rate at 60 FPS

    game = Game()

    print("Starting Loop")
    # Main game loop
    running = True
    while running:
        # Poll for events (keyboard, mouse, etc.) every frame
        for event in pygame.event.get():
            # Event handling
            ### System events
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            ### Game events
            game.handle_event(event)

        # Update game state
        game.update()

        # Render game state
        game.render(game.screen, game.display)

        # Limit the frame rate to 60 FPS
        clock.tick(fps)

    # Quit pygame and close all windows
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

