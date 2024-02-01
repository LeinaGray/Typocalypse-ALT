import pygame.display

# Create the window
class Window():
    def __init__(self, width, height, title):
        # super(Window, self).__init__()
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.title = pygame.display.set_caption(title)

    # set background using a full background image
    def setBackground(self,file_path):
        self.background = pygame.image.load(file_path).convert()
        self.screen.blit(self.background,(0,0))
    
    # set background using a single tile
    def setBackground(self,tile_img):
        # convert tile image to a tile surface 
        self.tile = pygame.image.load(tile_img).convert_alpha()

        # get tile dimensions
        TILE_WIDTH, TILE_HEIGHT = self.tile.get_size()

        # create a surface bigger than the window
        bigger_surface = pygame.Surface((self.width + TILE_WIDTH, self.height + TILE_HEIGHT))

        # fill the bigger surface with tiles
        for y in range(bigger_surface.get_height()//TILE_HEIGHT):
            for x in range(bigger_surface.get_width()//TILE_WIDTH):
                bigger_surface.blit(self.tile, (x * TILE_WIDTH, y * TILE_HEIGHT))
        
        # clip the bigger surface to fit the window
        bigger_surface.set_clip((0, 0, self.width, self.height))

        #show background on window
        self.screen.blit(bigger_surface, (0,0))
    
    def setFrameRate(self, FPS):
        self.clock = pygame.time.Clock()
        self.clock.tick()
    
    def show(self, sprite, position):
        self.screen.blit(sprite, position)
    
    def drawScreen(self, FONT_FILE_PATH, level):
        # bottom panel
        pygame.draw.rect(self.screen, "black", [0, self.height-100, self.width, 100], 0)
        # short vertical border line to separate user input from level
        pygame.draw.line(self.screen, (100,100,100), (250, self.height-100), (250, self.height), 2)
        # horizontal border line above panel
        pygame.draw.line(self.screen, (100,100,100), (0, self.height-100), (self.width, self.height-100), 2)

        # draw text on screen
        font = pygame.font.Font(FONT_FILE_PATH, 50)
        self.screen.blit(font.render(f"Level: {level}", True, "white"), (20, self.height-85))
        self.screen.blit(font.render(f"{user_typed_text}", True, "white"), (270, self.height-85))
    
    # def showStats(self, FONT_FILE_PATH, best_score, score, lives):
    #     font = pygame.font.Font(FONT_FILE_PATH, 50)
        
    #     self.screen.blit(font.render(f"Best Score: {best_score}", True, "white"), (10, 10))
    #     self.screen.blit(font.render(f"Score: {score}", True, "white"), (self.width-50, 10))
    #     self.screen.blit(font.render(f"Lives: {lives}", True, "white"), (self.width-100, 10))
        