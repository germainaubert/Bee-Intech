import pygame
from pygame.locals import *
from create_button import button
from display import display
class window():

    def __init__(self):
        pygame.init()
        
        self._w, self._h = self.getSize()
        self._window = pygame.display.set_mode((self._w, self._h), pygame.FULLSCREEN)
        self._title = "comet fall game"
        pygame.display.set_caption(self._title)
        display.display_menu(self)
        
    def main_loop(self):
        run = True
        while run:
            pygame.display.flip()
            run = self.event_handler(pygame.event.get())      
            
    def event_handler(self, event_list, run = True): # suceptible de prendre beaucoup plus d'arguments, nottament pour la gestion des différents boutons 
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if self._quit_button.is_over(event.pos):
                    run = False
                    pygame.quit()
        return run
                
    def getSize(self):
        return pygame.display.Info().current_w, pygame.display.Info().current_h

window = window()
window.main_loop()