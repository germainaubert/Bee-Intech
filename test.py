import pygame
class window():

    def __init__(self):
        title = pygame.display.set_caption("comet fall game")
        self._screen = pygame.display.set_mode((1080, 720))
        self._background = pygame.image.load('bak.png')

        run = True
        while run:
            self._screen.blit(self._background, (500,550))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
pygame.init()
window()