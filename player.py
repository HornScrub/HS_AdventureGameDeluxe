import pygame

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 100, 50, 50)
        self.color = (0, 128, 255)
        self.speed = 5
        self.velocity = pygame.Vector2(0, 0)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:

            # Player Movement
            if event.key == pygame.K_LEFT:
                self.velocity.x = -self.speed
            elif event.key == pygame.K_RIGHT:
                self.velocity.x = self.speed
            elif event.key == pygame.K_UP:
                self.velocity.y = -self.speed
            elif event.key == pygame.K_DOWN:
                self.velocity.y = self.speed
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.velocity.x = 0
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                self.velocity.y = 0
    
    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    