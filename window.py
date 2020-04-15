import pygame
from create_button import button

class window():

    def __init__(self):
        pygame.init()
        title = pygame.display.set_caption("comet fall game")
        self._window = pygame.display.set_mode((1080, 720))
        self._background = pygame.image.load('bak.png')

        run = True

        #Créer un bouton
        #green_button = button((0,255,0), 150, 225, 250, 100, 'Click Me')

        while run:
            self._window.blit(self._background, (500,550))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                #else:
                    #Affiche le boutton
                    #green_button.draw(self._window)

window()