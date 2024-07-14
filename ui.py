import pygame

class UI:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ui_height = screen_height // 5 # Screen height is bottom third of the screen
        self.bezel_thickness = 10 # Thickness of the bezels
        self.font = pygame.font.Font(None, 36)

    def render(self, screen, player):
        # Fill the UI area with a background color
        pygame.draw.rect(screen, (50, 50, 50), (0, self.screen_height - self.ui_height, self.screen_width, self.ui_height))

        # Render bezels
        # Bottom bezel
        pygame.draw.rect(screen, (200, 200, 200), (0, self.screen_height - self.ui_height, self.screen_width, self.bezel_thickness))
        #Left bezel
        pygame.draw.rect(screen, (200, 200, 200), (0, 0, self.bezel_thickness, self.screen_height - self.ui_height))
        # Right bezel
        pygame.draw.rect(screen, (200, 200, 200), (self.screen_width - self.bezel_thickness, 0, self.bezel_thickness, self.screen_height - self.ui_height))
        # Render player information
        health_text = self.font.render(f"Health: {player.health}", True, (255, 255, 255))
        screen.blit(health_text, (20, self.screen_height - self.ui_height + 20))

        # vvv Additional UI elements vvv