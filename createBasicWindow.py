import pygame
import sys

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

# Set up the window

''' set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface
        This function will create a display Surface. The arguments passed in are requests for a display type. The actual created display will be the best possible match supported by the system.

            Note that calling this function implicitly initializes pygame.display, if it was not initialized before.

            The size argument is a pair of numbers representing the width and height. The flags argument is a collection of additional options. The depth argument represents the number of bits to use for color.

            The Surface that gets returned can be drawn to like a regular Surface but changes will eventually be seen on the monitor.

            If no size is passed or is set to (0, 0) and pygame uses SDL version 1.2.10 or above, the created Surface will have the same size as the current screen resolution. If only the width or height are set to 0, the Surface will have the same width or height as the screen resolution. Using a SDL version prior to 1.2.10 will raise an exception.

            It is usually best to not pass the depth argument. It will default to the best and fastest color depth for the system. If your game requires a specific color format you can control the depth with this argument. Pygame will emulate an unavailable color depth which can be slow.

            When requesting fullscreen display modes, sometimes an exact match for the requested size cannot be made. In these situations pygame will select the closest compatible match. The returned surface will still always match the requested size.

            On high resolution displays(4k, 1080p) and tiny graphics games (640x480) show up very small so that they are unplayable. SCALED scales up the window for you. The game thinks it's a 640x480 window, but really it can be bigger. Mouse events are scaled for you, so your game doesn't need to do it. Note that SCALED is considered an experimental API and may change in future releases.

            The flags argument controls which type of display you want. There are several to choose from, and you can even combine multiple types using the bitwise or operator, (the pipe "|" character). Here are the display flags you will want to choose from:

            pygame.FULLSCREEN    create a fullscreen display
            pygame.DOUBLEBUF     only applicable with OPENGL
            pygame.HWSURFACE     (obsolete in pygame 2) hardware accelerated, only in FULLSCREEN
            pygame.OPENGL        create an OpenGL-renderable display
            pygame.RESIZABLE     display window should be sizeable
            pygame.NOFRAME       display window will have no border or controls
            pygame.SCALED        resolution depends on desktop size and scale graphics
            pygame.SHOWN         window is opened in visible mode (default)
            pygame.HIDDEN        window is opened in hidden mode    '''

#WINDOWED: window_size = (800, 600)
#window = pygame.display.set_mode(window_size)

#FULLSCREEN:
#   Set screen width and height relative to user display height and width
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

window = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("AdventureGameDeluxe")

'''https://www.rapidtables.com/web/color/RGB_Color.html'''

# Define button properties (relative to screen size)
### (//) is rounded down division, so the button width is a tenth of the screen width, etc.
###    These are the dimensions of the button'''
button_width, button_height = screen_width // 10, screen_height // 20
### This is the position of the button '''
button_x, button_y = screen_width // 20, screen_height // 20
### The button is not implicitly being pressed '''
button_pressed = False
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
button_color = (255, 0, 0)
button_hover_color = (200, 0, 0)
button_text_color = (255, 255, 255)
button_font = pygame.font.Font(None, button_height // 2)

# Function to draw button
def draw_button(screen, rect, color, text):
    pygame.draw.rect(screen, color, rect)
    text_surface = button_font.render(text, True, button_text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

### Our window is a surface. We will paint the surface with things like buttons.

# Main game loop
running = True
while running:
    # Poll for events (keyboard, mouse, etc.) every frame
    ### There are lots of events that we can initialize and tie them to user input
    for event in pygame.event.get():
        # End the program if user hits the x 
        if event.type == pygame.QUIT:
            running = False
        # End the program if user hits the escape key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        # End the program if user clicks the button on screen. 
        ### Once the user clicks the button, the button is being pressed'''
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                button_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if button_rect.collidepoint(event.pos) and button_pressed:
                running = False
    
    # Fill the screen with a color (e.g., black)
    window.fill((0, 0, 0))

    # Change button color on hover
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        current_button_color = button_hover_color
    else:
        current_button_color = button_color

    draw_button(window, button_rect, current_button_color, "Quit")

    # Update the display
    pygame.display.flip()




pygame.quit()
sys.exit()

