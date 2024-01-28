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

# create the game loop
running = True
while running:
    # iterate through all events such as keyboard press or mouse clicks
    for event in pygame.event.get():
        # close program if user clicks exit button on window
        if event.type == pygame.QUIT:
            running = False
            
    # show player on window
    window.show(player.image, player.position)
            

    # Update game elements and draw on the window here

    pygame.display.update()  # Update the display
