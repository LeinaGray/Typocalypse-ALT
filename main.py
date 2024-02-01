import pygame 
from settings import *

# import window
from Window import *
# create and set window
window = Window(WIDTH, HEIGHT, "Typocalypse")
window.setBackground(TILE_IMG)
window.setFrameRate(FPS)

# import player
from Player import *
# create and set player 
player = Player(PLAYER_IMG, SIZE, PLAYER_DEFAULT_X, PLAYER_DEFAULT_Y)

# create the game loop
running = True
while running:
    # iterate through all events such as keyboard press or mouse clicks
    for event in pygame.event.get():
        # close program if user clicks exit button on window
        if event.type == pygame.QUIT:
            running = False

    # show player on window and use the player's rectangle as position
    window.show(player.image, player.rect)
    player.setRotatable(True)
    pygame.draw.rect(window.screen, "red", player.hitbox_rectangle, width=2)
    
    # show rectangle of player (optional and glitchy)
    # pygame.draw.rect(window.screen, "yellow", player.rect, width=1)
            

    # Update game elements and draw on the window here

    pygame.display.update()  # Update the display
