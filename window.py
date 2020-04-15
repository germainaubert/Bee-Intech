import pygame
from create_button import button

class window():

    def __init__(self):
        pygame.init()

        self._w, self._h = self.getSize()

        self._screen = pygame.display.set_mode((self._w, self._h), pygame.FULLSCREEN)

        title = "comet fall game"
        pygame.display.set_caption(title)

        self._background = pygame.image.load('./Images/fond.jpg')

        run = True

        #Créer un bouton
        green_button = button((0,255,0), 150, 225, 250, 100, 'Click Me')

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