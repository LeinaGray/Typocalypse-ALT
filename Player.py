import pygame
import math

# DEFINITION OF TERMS
# Sprite: 2d object we draw on the screen


# inherits Sprite class 
class Player(pygame.sprite.Sprite):
    # create a constructor to create Player objects
    def __init__(self, file_path, size, x, y):
        # inherit the constructor from Sprite class
        super().__init__()
        # set the default position of the player in x and y coordinates
        self.position = pygame.math.Vector2(x, y)
        # set the image for player
        self.image = pygame.transform.rotozoom(pygame.image.load(file_path).convert_alpha(), 0, size)
        # set a surface that shows the player image so it doesn't glitch later on
        self.base_player_img = self.image
        # set the rectangle that checks for collisions or hits 
        self.hitbox_rectangle = self.base_player_img.get_rect(center = self.position)
        # set the rectangle of player
        self.rect = self.hitbox_rectangle.copy();
        
    
    def setRotatable(self, bool):
        if bool == True:
            self.mouse_position = pygame.mouse.get_pos()
            # get difference between coordinates of player and mouse position
            self.x_difference_mousePlayer = (self.mouse_position[0] - self.hitbox_rectangle.centerx)
            self.y_difference_mousePlayer = (self.mouse_position[1] - self.hitbox_rectangle.centery)
            self.rotated_angle = math.degrees(math.atan2(self.y_difference_mousePlayer, self.x_difference_mousePlayer))
            # rotate the image
            self.image = pygame.transform.rotate(self.base_player_img, -self.rotated_angle)
            self.rect = self.image.get_rect(center = self.hitbox_rectangle.center)
     
    def allowHits(self):
        self.hitbox_rectangle = self.base_player_img.get_rect(center = self.position)
        self.rect = self.hitbox_rectangle.copy()
    

        
    