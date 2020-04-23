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
        self._buy_bee_button = None
        
        self._w, self._h = self.getSize()
        self._window = pygame.display.set_mode((self._w, self._h), pygame.FULLSCREEN)
        self._title = "BEETTHEFUCKOUTOFMYWIFE"
        self._display = display()
        pygame.display.set_caption(self._title)
        self._surface = self._display.display_menu(self._w, self._h) # _surface est la surface qui doit contenir tout ce qui concerne l'affichage, à bien différencier avec _window
        
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
                #print(self._display._button_dic)
                self._last_button = event.type
                if "quit_button" in self._display._button_dic:
                    if self._display._button_dic["quit_button"].is_over(event.pos):
                        run = False
                        pygame.quit()
                        break
                if "launch_game_button" in self._display._button_dic:
                    if self._display._button_dic["launch_game_button"].is_over(event.pos):
                        self.game_init()
                        self._surface = self._display.display_new_game(self._w, self._h)
                if "bees_button" in self._display._button_dic:
                    if self._display._button_dic["bees_button"].is_over(event.pos):
                        self._surface = self._display.display_management()
                if "shop_button" in self._display._button_dic:
                    if self._display._button_dic["shop_button"].is_over(event.pos):
                        self._surface = self._display.display_shop(self._w, self._h, self.shop.bees())
                if "fight_button" in self._display._button_dic:
                    if self._display._button_dic["fight_button"].is_over(event.pos):
                        self._surface = self._display.display_fight()
                if "buy_bee_button" in self._display._button_dic:
                    if self._display._button_dic["buy_bee_button"].is_over(event.pos):
                        self.test_bee()

        return run
                
    def getSize(self):
        return pygame.display.Info().current_w, pygame.display.Info().current_h

    def game_init(self):
        self.hive = hive()
        self.shop = shop()

    def test_bee(self):
        for bee in self.shop._bees:
            if self._display._button_dic["buy_bee_button"]._get == bee._name:
                shop.buy_bee(self, self.hive, bee)

window = window()
window.main_loop()