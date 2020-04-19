import pygame
from pygame.locals import *
from Create_button import button
from Display import display
from math import *

class window():

    def __init__(self):
        pygame.init()
        
        self._w, self._h = self.getSize()
        self._window = pygame.display.set_mode((self._w, self._h), pygame.FULLSCREEN)
        self._title = "comet fall game"
        pygame.display.set_caption(self._title)
        
        self._surface = display.display_menu(self, self._w, self._h) # _surface est la surface qui doit contenir tout ce qui concerne l'affichage, à bien différencier avec _window
        
        
    def main_loop(self):
        run = True
        while run:
            self._window.blit(pygame.transform.scale(self._surface, (self._w, self._h)), (0,0)) # transforme l'image selon la résolution de l'image
            pygame.display.flip()
            run = self.event_handler(pygame.event.get())      
            
    def event_handler(self, event_list, run = True):
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