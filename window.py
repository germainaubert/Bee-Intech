import pygame
from pygame.locals import *
from create_button import button
from display import display
from math import *
from Hive import hive
from Shop import shop

class window():

    def __init__(self):
        pygame.init()

        # Initialisation des boutons
        self._quit_button = None
        self._launch_game_button = None
        self._bees_button = None
        self._shop_button = None
        self._fight_button = None
        
        self._w, self._h = self.getSize()
        self._window = pygame.display.set_mode((self._w, self._h), pygame.FULLSCREEN)
        self._title = "BEETTHEFUCKOUTOFMYWIFE"
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
            #print(event)
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
            if event.type == MOUSEBUTTONDOWN:
                self._last_button = event.type
                if self._quit_button is not None:
                    if self._quit_button.is_over(event.pos):
                        run = False
                        pygame.quit()
                        break
                if self._launch_game_button is not None:
                    if self._launch_game_button.is_over(event.pos):
                        self.game_init()
                        self._surface = display.display_new_game(self, self._w, self._h)
                if self._bees_button is not None:
                    if self._bees_button.is_over(event.pos):
                        self._surface = display.display_management(self)
                if self._shop_button is not None:
                    if self._shop_button.is_over(event.pos):
                        self._surface = display.display_shop(self, self._w, self._h)
                if self._fight_button is not None:
                    if self._fight_button.is_over(event.pos):
                        self._surface = display.display_fight(self)
        return run
                
    def getSize(self):
        return pygame.display.Info().current_w, pygame.display.Info().current_h

    def game_init(self):
        self.hive = hive()
        self.shop = shop()

window = window()
window.main_loop()