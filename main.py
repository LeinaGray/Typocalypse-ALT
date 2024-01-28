import pygame 
from settings import *

# import window
from Window import *
# create and set window
window = Window(WIDTH, HEIGHT, "Typocalypse")
window.setBackground(BACKGROUND_IMG)
window.setFrameRate(FPS)

# import player
from Player import *
# create and set player 
player = Player(PLAYER_IMG, PLAYER_DEFAULT_X, PLAYER_DEFAULT_Y)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    # Update game elements and draw on the window here

    pygame.display.update()  # Update the display
