import pygame.display

# Create the window
class Window():
    def __init__(self, width, height, title):
        # super(Window, self).__init__()
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.title = pygame.display.set_caption(title)

    def setBackground(self,file_path):
        self.background = pygame.image.load(file_path).convert()
        self.screen.blit(self.background,(0,0))
        
        