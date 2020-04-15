import pygame
class window():

    def __init__(self):
        title = "comet fall game"
        pygame.display.set_caption(title)

        self._w, self._h = self.getSize()

        self._screen = pygame.display.set_mode((self._w, self._h), pygame.FULLSCREEN)
        self._background = pygame.image.load('./Images/fond.jpg')

        run = True
        while run:
            self._screen.blit(self._background, (0, 0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
    
    def getSize(self):
        return pygame.display.Info().current_w, pygame.display.Info().current_h

        
pygame.init()
window()