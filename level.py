import pygame

class Level:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.obstacles = [
            pygame.Rect(300, 200, 100, 100),
            pygame.Rect(500, 300, 150, 50)
        ]

    def render(self, screen):
        for obstacle in self.obstacles:
            pygame.draw.rect(screen, (255, 0, 0), obstacle)

    def check_collision(self, rect):
        for obstacle in self.obstacles:
            if rect.colliderect(obstacle):
                return True
        return False
