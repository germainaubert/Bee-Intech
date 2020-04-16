import pygame
from pygame.locals import *
from Create_button import button

class window():

    def __init__(self):
        pygame.init()
        
        self._w, self._h = self.getSize()

        self._window = pygame.display.set_mode((self._w, self._h), pygame.FULLSCREEN)

        self._title = "comet fall game"
        pygame.display.set_caption(self._title)
        self.display_menu()

    def display_menu(self):
        self._background = pygame.image.load('./Images/fond.jpg')
        self._window.blit(self._background, (0, 0))
        self._quit_button = button((212,180,0), 1720, 985, 180, 75, 'Quitter')
        self._quit_button.draw_button(self._window)
        
    def main_loop(self):
        run = True
        while run:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    if self._quit_button.is_over(event.pos):
                        run = False
                        pygame.quit()
            
        
                
    def getSize(self):
        return pygame.display.Info().current_w, pygame.display.Info().current_h

window = window()
window.main_loop()