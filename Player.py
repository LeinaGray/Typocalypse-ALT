import pygame

# DEFINITION OF TERMS
# Sprite: 2d object we draw on the screen


# inherits Sprite class 
class Player(pygame.sprite.Sprite):
    # create a constructor to create Player objects
    def __init__(self, file_path, x, y):
        # inherit the constructor from Sprite class
        super().__init__()

        # set the image for player
        self.image = pygame.image.load(file_path).convert_alpha()
        # set the default position of the player in x and y coordinates
        self.position = pygame.math.Vector2(x, y)
        
    