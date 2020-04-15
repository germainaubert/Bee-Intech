import pygame
from create_button import button

class window():

    def __init__(self):
        pygame.init()

        self._w, self._h = self.getSize()

        self._window = pygame.display.set_mode((self._w, self._h), pygame.FULLSCREEN)

        self.title = "comet fall game"
        pygame.display.set_caption(self.title)

        self._background = pygame.image.load('./Images/fond.jpg')

        run = True

        #Créer un bouton
        quit_button = button((0,255,0), 150, 225, 250, 100, 'Quitter')

        while run:
            self._window.blit(self._background, (0, 0))
            quit_button.draw_button(self._window)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
    
    def getSize(self):
        return pygame.display.Info().current_w, pygame.display.Info().current_h

pygame.init()
window()