import pygame
from pygame.locals import *
from create_button import button
from display import display
from live_display import live_display
from Hive import hive
from Shop import shop
from tick_update import tick_update
from Territory import territory
from database import database
 
 

from Shop import shop

class window():

    def __init__(self):
        pygame.init()

        self._clock = pygame.time.Clock()
        
        self._call_same = True # Pour savoir si l'appel d'affichage est le même

        self._hive = None

        # Initialisation des boutons
        self._quit_button = None
        self._launch_game_button = None
        self._bees_button = None
        self._shop_button = None
        self._fight_button = None
        self._buy_bee_button = None
        self._get_honey_button = None
        
        self._w, self._h = self.getSize()
        self._window = pygame.display.set_mode((self._w, self._h), pygame.FULLSCREEN)
        self._title = "BEETTHEFUCKOUTOFMYWIFE"
        self._display = display()
        pygame.display.set_caption(self._title)
        self._surface = self._display.display_menu(self._w, self._h) # _surface est la surface qui doit contenir tout ce qui concerne l'affichage, à bien différencier avec _window
        
        self._live = None # attribut pour déterminer si un affichage doit se faire à chaque itération de la boucle principales
        self._alert = None # Pareil que live mais pour les alertes
        self._first_call = None # Sert à déterminer quand les boutons doivent être stockés pour alerte de live display

        # valeur pour le scroll
        self._scroll_y = 0

        self._live_display = None

        self._tick_update = None

        self._bee_quantity = None

        self._bees_surfaces = None

        self._tick = 60

        
        
        
    def main_loop(self):
        
        run = True
        while run:
            
            events = pygame.event.get() # Stocké dans la variable events car lorsqu'on appelle event.get la liste d'event se vide

            if self._tick_update != None:
                self._tick_update.caller()

            # ------------------------ Afficher des données à chaque tick
            
            if self._live_display != None:
                jaj = pygame.Surface.copy(self._surface) # pour éviter la shadow copie de l'enfer
                
                if self._live == "management":
                    live_surface, self._bee_quantity, self._display._button_dic, self._alert, self._scroll_y = self._live_display.give_display(self._live, self._alert, jaj, events, self._display._button_dic, self._first_call, self._bees_surfaces, self._scroll_y)
                elif self._live == "shop":
                    live_surface, self._bee_quantity, self._display._button_dic, self._first_call, self._alert, self._scroll_y = self._live_display.give_display(self._live, self._alert, jaj, events, self._display._button_dic, self._first_call, self._bees_surfaces, self._scroll_y) # prend event en parametre pour permettre l'input
                else: 
                    live_surface = self._live_display.give_display(self._live, self._alert, jaj, events, self._display._button_dic, self._first_call, self._bees_surfaces, self._scroll_y)
                
                self._window.blit(pygame.transform.scale(live_surface, (self._w, self._h)), (0,0)) # transforme l'image selon la résolution de l'image

            else:
                self._window.blit(pygame.transform.scale(self._surface, (self._w, self._h)), (0,0)) # transforme l'image selon la résolution de l'image

            
            if self._bee_quantity != None and self._bee_quantity != "":
                self._bee_quantity = int(self._bee_quantity)
            
            # ------------------------
            
            
            
            pygame.display.flip()
            run = self.event_handler(events)
            self._clock.tick(self._tick)

            
    def event_handler(self, event_list, run = True):
        
        for event in event_list:
            #print(event)
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
            # Input souris
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 3: # # Pour qu'on puisse cliquer juste avec les clics gauche et droit
                    self._last_button = event.type
                    # Navigation
                    if "quit_button" in self._display._button_dic:
                        if self._display._button_dic["quit_button"].is_over(event.pos):
                            run = False
                            pygame.quit()
                            break
                    if "launch_game_button" in self._display._button_dic:
                        if self._display._button_dic["launch_game_button"].is_over(event.pos):
                            self.game_init()
                            self._surface = self._display.display_new_game(self._w, self._h)
                            self._live = "new_game"
                            break
                    if "back_button" in self._display._button_dic:
                        if self._display._button_dic["back_button"].is_over(event.pos):
                            self._surface = self._display.display_new_game(self._w, self._h)
                            self._live = "new_game"
                            break
                    if "bees_button" in self._display._button_dic:
                        if self._display._button_dic["bees_button"].is_over(event.pos):
                            self._live = "management"
                            self._scroll_y = 0 # Valeur de scroll initial, pour ne pas que le scroll soit dans l'état ou il a été laissé
                            self._surface, self._bees_surfaces = self._display.display_management(self._w, self._h, self._hive, self._scroll_y)
                            break
                    if "shop_button" in self._display._button_dic:
                        if self._display._button_dic["shop_button"].is_over(event.pos):
                            self._surface, self._bees_surfaces = self._display.display_shop(self._w, self._h, self._shop.bees(), self._hive)
                            self._live = "shop"
                            self._scroll_y = 0 # Valeur de scroll initial, pour ne pas que le scroll soit dans l'état ou il a été laissé
                            break
                    if "fight_button" in self._display._button_dic:
                        if self._display._button_dic["fight_button"].is_over(event.pos):
                            self._surface = self._display.display_fight()
                            self._live = "fight"
                            break
                    # TEST
                    if "get_honey_button" in self._display._button_dic:
                        if self._display._button_dic["get_honey_button"].is_over(event.pos):
                            self._hive.ressource_click("honey", 100)
                    # Management
                    if "delete_bee_button" in self._display._button_dic:
                        for targetted_button in self._display._button_dic["delete_bee_button"]:
                            if targetted_button.is_over(event.pos):
                                print("event.pos:", event.pos, "....... targetted_buttton:", targetted_button._x, targetted_button._y)
                                print("get:", targetted_button.get())
                                delete = self._hive.del_bee(targetted_button.get())
                                self._hive.decrease_prod(delete)
                                self._surface, self._bees_surfaces = self._display.display_management(self._w, self._h, self._hive, self._scroll_y)
                                break
                    # Shop
                    if "buy_bee_button" in self._display._button_dic:
                        for button in self._display._button_dic["buy_bee_button"]:
                            if button.is_over(event.pos):
                                self._alert, self._first_call = self._shop.test_bee(button._get, self._hive)
                    # Shop_ALERT
                    if "cant_buy_alert" in self._display._button_dic:
                        if self._display._button_dic["cant_buy_alert"].is_over(event.pos):
                            self._alert = "GetRideOfThisShit" # oui
                    if "cancel_buy" in self._display._button_dic:
                        if self._display._button_dic["cancel_buy"].is_over(event.pos):
                            self._alert = "GetRideOfThisShit" # re oui
                    if "purchase_confirmation" in self._display._button_dic:
                        if self._display._button_dic["purchase_confirmation"].is_over(event.pos):
                            self._alert = "GetRideOfThisShit"
            # Input clavier
            if event.type == KEYDOWN:
                
                if (event.key == K_RETURN or event.key == K_KP_ENTER) and self._alert == "Buy" and self._bee_quantity != 0 and self._bee_quantity != "":
                    isOK = self._shop.final_purchase(self._hive, self._bee_quantity)
                    if isOK == "nope":
                        self._alert = "CantBuy"
                    else:
                        self._alert = "confirm_purchase"
                       
        return run

    def getSize(self):
        return pygame.display.Info().current_w, pygame.display.Info().current_h

    def game_init(self):
        self._hive = hive(ressource = (100,0,0,0,0), prod = (0,0,0,0,0), territories = [ territory("base", 0, 0, "honey", 5, []), territory("base2", 0, 1, "honey", 7, []) ])
        self._database = database()
        save = self._database.hive_save((self._hive.exp(), self._hive.level()))
        self._shop = shop()
        self._tick_update = tick_update(self._hive, self._tick)
        self._live_display = live_display(self._w, self._h, self._hive)


window = window()
window.main_loop()