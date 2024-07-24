import pygame
import math

class Vision:
    def __init__(self):
        self.color = (255, 100, 0 , 128) 

    def render(self, screen, player_position, cursor_position):
        # Calculate the points of the vision cone
        cone_points = self.calculate_cone_points(player_position, cursor_position)
        # Draw the vision circle

        pygame.draw.circle(screen, self.color, player_position, 60)
        # Draw the vision cone
        pygame.draw.polygon(screen, self.color, cone_points)

    def calculate_cone_points(self, player_position, cursor_position):
        # Player position
        px, py = player_position
        # Cursor position
        cx, cy = cursor_position

        # Angle between player and cursor
        angle = math.atan2(cy - py, cx - px)

        # Length of the cone (from the player)
        cone_length = 400

        # Angle spread of the cone
        spread_angle = math.radians(80) # 80 degrees spread

        # Calculate the two other points of the triangle
        left_angle = angle - spread_angle / 2
        right_angle = angle + spread_angle / 2

        left_point = (px + cone_length * math.cos(left_angle), py + cone_length * math.sin(left_angle))
        right_point = (px + cone_length * math.cos(right_angle), py + cone_length * math.sin(right_angle))

        cone_points = [player_position, left_point, right_point]

        return cone_points




    
