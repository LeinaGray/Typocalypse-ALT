import pygame 
from settings import *
from Window import *

window = Window(WIDTH, HEIGHT, "Typocalypse")
window.setBackground(BACKGROUND_FILE_PATH)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    # Update game elements and draw on the window here

    pygame.display.update()  # Update the display
