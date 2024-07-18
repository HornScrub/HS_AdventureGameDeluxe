import pygame
class Player:
    def __init__(self, level):
        self.level_width = level.width
        self.level_height = level.height
        self.rect = pygame.Rect(1, 1, 50, 50)
        self.color = (0, 132, 199)
        self.speed = 5
        self.velocity = pygame.Vector2(0, 0)
        self.x_y_upleft_pos = (self.rect.x, self.rect.y)



    def handle_event(self, event):
        keys = pygame.key.get_pressed()
        self.update_velocity(keys)

    def update_velocity(self, keys):
            # Reset velocities
            self.velocity.x = 0
            self.velocity.y = 0

            # Update based on current key states
            if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
                self.velocity.x = 0  # Zero out velocity if both left and right are pressed
            elif keys[pygame.K_LEFT]:
                self.velocity.x = -self.speed
            elif keys[pygame.K_RIGHT]:
                self.velocity.x = self.speed

            if keys[pygame.K_UP] and keys[pygame.K_DOWN]:
                self.velocity.y = 0  # Zero out velocity if both up and down are pressed
            elif keys[pygame.K_UP]:
                self.velocity.y = -self.speed
            elif keys[pygame.K_DOWN]:
                self.velocity.y = self.speed

    def update(self, level):
        # Create new Rects representing potential new positions
        new_rect_x = self.rect.move(self.velocity.x, 0)  # Move horizontally
        new_rect_y = self.rect.move(0, self.velocity.y)  # Move vertically

        # Backup velocities before collision detection
        backup_velocity_x = self.velocity.x
        backup_velocity_y = self.velocity.y

        # Check for horizontal collisions
        if not level.check_collision(new_rect_x):
            self.rect.x += self.velocity.x
            x_change = self.speed
        else:
            self.velocity.x = 0  # Stop horizontal movement

        # Check for vertical collisions
        if not level.check_collision(new_rect_y):
            self.rect.y += self.velocity.y
            y_change = self.speed
        else:
            self.velocity.y = 0  # Stop vertical movement

        # Boundary checking as before
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.level_width:
            self.rect.right = self.level_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.level_height:
            self.rect.bottom = self.level_height

        # Restore velocities if no collision
        if self.velocity.x == 0:
            self.velocity.x = backup_velocity_x
        if self.velocity.y == 0:
            self.velocity.y = backup_velocity_y

        self.x_y_upleft_pos = self.rect.x, self.rect.y


        # Update velocity again based on current keys to ensure continuous movement
        keys = pygame.key.get_pressed()
        self.update_velocity(keys)

        

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def get_position(self):
        return self.x_y_upleft_pos


