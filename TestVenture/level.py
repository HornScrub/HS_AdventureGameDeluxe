import pygame

class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = [
            pygame.Rect(300, 200, 100, 100),
            pygame.Rect(500, 300, 150, 50)
        ]
    
    def render(self, screen):
        for obstacle in self.obstacles:
            pygame.draw.rect(screen, (50, 102, 50), obstacle)

    def check_collision(self, rect):
        for obstacle in self.obstacles:
            if rect.colliderect(obstacle):
                return True
        
        # Check collision with UI area
        if rect.bottom > self.height:
            return True
        
        if rect.left < 0:
            return True
        
        if rect.right > self.width:
            return True
        
        return False