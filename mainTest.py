import pygame
import sys

from display import Display
from game import Game

def main():

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

    settings = {
        'screen_width' : pygame.display.Info().current_w,
        'screen_height': pygame.display.Info().current_h,
        'fullscreen' : True
    }

    display = Display(settings)
    game = Game(display)

    # Create a clock object to manage the frame rate
    clock = pygame.time.Clock()
    fps = 60 # Cap the frame rate at 60 FPS

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            game.handle_event(event)

        game.update()
        game.render()
        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        clock.tick(fps)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

