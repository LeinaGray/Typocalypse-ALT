import pygame 
from settings import *

# import game
from Game import *
game = Game()
current_text = "Enter to start"
entered_text = ""

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
    window.drawScreen(TYPE_FONT, game.level)
    window.showTyping(current_text)
    # iterate through all events such as keyboard press or mouse clicks
    for event in pygame.event.get():
        # close program if user clicks exit button on window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.unicode.lower() in LETTERS:
                current_text += event.unicode.lower()
            if event.key == pygame.K_BACKSPACE and len(current_text) > 0:
                current_text = current_text[:-1]
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                entered_text = current_text
                current_text = ''

    
    
    # window.showStats(TYPE_FONT, game.level, game.best_score, game.score, game.lives)

    # show player on window and use the player's rectangle as position
    window.show(player.image, player.rect)
    player.setRotatable(True)
    pygame.draw.rect(window.screen, "red", player.hitbox_rectangle, width=2)
    
    # show rectangle of player (optional and glitchy)
    # pygame.draw.rect(window.screen, "yellow", player.rect, width=1)

    pygame.display.update()  # Update the display

pygame.quit()
