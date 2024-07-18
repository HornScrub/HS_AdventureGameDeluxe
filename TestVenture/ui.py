import pygame

class UI:
    def __init__(self):
        self.font = pygame.font.Font(None, 24)
        self.ui_info = {
            'x_y_pos' : (0, 0),
            'x_y_player_pos' : (0, 0),
        }

    def render(self, screen):
        y = 1
        for key in self.ui_info.keys():
            value = self.ui_info[key]
            text = self.font.render(f"{key}: {value}", True, (255, 255, 255))
            screen.blit(text, (1, y))
            y += y + 24

    def handle_event(self, event):
        pass

    def update(self, display, player):
        self.ui_info['x_y_pos'] = display.get_mouse_position()
        self.ui_info['x_y_player_pos'] = player.get_position()

    
