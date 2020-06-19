import pygame
from pygame.locals import *
from create_button import button
from display import display
from live_display import live_display
from Hive import hive
from Shop import shop
from tick_update import tick_update
from Territory import *
from database import database
from Upgrade import upgrade
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
        self._surface = self._display.display_new_game(self._w, self._h) # _surface est la surface qui doit contenir tout ce qui concerne l'affichage, à bien différencier avec _window
        
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
                elif self._live == "fight_menu":
                    live_surface, self._display._button_dic = self._live_display.give_display(self._live, self._alert, jaj, events, self._display._button_dic, self._first_call, self._bees_surfaces, self._scroll_y)
                elif self._live == "menu":
                    live_surface, self._display._button_dic = self._live_display.give_display(self._live, self._alert, jaj, events, self._display._button_dic, self._first_call, self._bees_surfaces, self._scroll_y)
                elif self._live == "up":
                    live_surface, self._scroll_y, self._display._button_dic = self._live_display.give_display(self._live, self._alert, jaj, events, self._display._button_dic, self._first_call, self._bees_surfaces, self._scroll_y)
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
            
            # Affichage curseur
            flag = False
            if event.type == MOUSEMOTION:
                
                for button in self._display._button_dic:
                    if type(self._display._button_dic[button]) == list:
                        for button_list in self._display._button_dic[button]:
                            
                            if button_list.is_over(event.pos):
                                pygame.mouse.set_cursor(*pygame.cursors.diamond)
                                flag = True
                                break
                            
                    else:
                        if self._display._button_dic[button].is_over(event.pos):
                            pygame.mouse.set_cursor(*pygame.cursors.diamond)
                            flag = True
                            break
            if (not flag):
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
                        
                    
                        
            # Input souris
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 3: # # Pour qu'on puisse cliquer juste avec les clics gauche et droit
                    self._last_button = event.type
                    # Navigation
                    if "quit_button" in self._display._button_dic:
                        if self._display._button_dic["quit_button"].is_over(event.pos):
                            # for bee in self._hive.bees():
                            #     save = self._database.hive_save_bee((self._database._save_count, bee._name, bee._cost, bee._category, bee._price[0], bee._price[1], bee._required_level, bee._sprite ))
                            run = False
                            pygame.quit()
                            break
                    if "launch_game_button" in self._display._button_dic:
                        if self._display._button_dic["launch_game_button"].is_over(event.pos):
                            self.game_init()
                            saved_bees = self._database.load_data()
                            for bee in saved_bees:
                                self._hive.add_bee(bee)
                            self._surface = self._display.display_menu(self._w, self._h)
                            self._live = "menu"
                            break
                    if "back_button" in self._display._button_dic:
                        if self._display._button_dic["back_button"].is_over(event.pos):
                            self._surface = self._display.display_menu(self._w, self._h)
                            self._live = "menu"
                            break
                    if "bees_button" in self._display._button_dic:
                        if self._display._button_dic["bees_button"].is_over(event.pos):
                            self._live = "management"
                            self._scroll_y = 0 # Valeur de scroll initial, pour ne pas que le scroll soit dans l'état ou il a été laissé
                            self._surface, self._bees_surfaces = self._display.display_management(self._w, self._h, self._hive, self._scroll_y)
                            break
                    if "upgrade_button" in self._display._button_dic:
                        if self._display._button_dic["upgrade_button"].is_over(event.pos):
                            self._alert = "upgrade_choice"
                            break
                    if "shop_button" in self._display._button_dic:
                        if self._display._button_dic["shop_button"].is_over(event.pos):
                            self._surface, self._bees_surfaces = self._display.display_shop(self._w, self._h, self._shop.bees(), self._hive)
                            self._live = "shop"
                            self._scroll_y = 0 # Valeur de scroll initial, pour ne pas que le scroll soit dans l'état ou il a été laissé
                            break
                    if "fight_menu_button" in self._display._button_dic:
                        if self._display._button_dic["fight_menu_button"].is_over(event.pos):
                            self._surface = self._display.display_fight(self._w, self._h)
                            self._live = "fight_menu"
                            break
                    
                    # TEST
                    if "get_honey_button" in self._display._button_dic:
                        if self._display._button_dic["get_honey_button"].is_over(event.pos):
                            self._hive.ressource_click("honey", 100)
                    # Management
                    if "delete_bee_button" in self._display._button_dic:
                        for targetted_button in self._display._button_dic["delete_bee_button"]:
                            if targetted_button.is_over(event.pos):
                                # print("event.pos:", event.pos, "....... targetted_buttton:", targetted_button._x, targetted_button._y)
                                # print("get:", targetted_button.get())
                                self._hive.del_bee(targetted_button.get())
                                #self._hive.decrease_prod(delete)
                                self._surface, self._bees_surfaces = self._display.display_management(self._w, self._h, self._hive, self._scroll_y)
                                break
                    # Shop
                    if "buy_bee_button" in self._display._button_dic:
                        for button in self._display._button_dic["buy_bee_button"]:
                            if button.is_over(event.pos):
                                self._alert, self._first_call = self._shop.test_bee(button._get, self._hive)
                    # Upgrade
                    if "upgrade_purchase" in self._display._button_dic:
                        for button in self._display._button_dic["upgrade_purchase"]:
                            if button.is_over(event.pos):
                                print("c cool")
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
                    # Menu_ALERT (ugpgrades)
                    if "fight_upgrades" in self._display._button_dic:
                        if self._display._button_dic["fight_upgrades"].is_over(event.pos):
                            self._alert = None
                            self._live = "up"
                            self._scroll_y = 0
                            self._display._button_dic = {}
                            self._surface, self._bees_surfaces = self._display.display_upgrades(self._w, self._h, self._hive, "fight")
                    if "hive_upgrades" in self._display._button_dic:
                        if self._display._button_dic["hive_upgrades"].is_over(event.pos):
                            self._alert = None
                            self._live = "up"
                            self._scroll_y = 0
                            self._display._button_dic = {}
                            self._surface, self._bees_surfaces = self._display.display_upgrades(self._w, self._h, self._hive, "hive")
                    if "cancel" in self._display._button_dic:
                        if self._display._button_dic["cancel"].is_over(event.pos):
                            self._alert = None
                            self._surface = self._display.display_menu(self._w, self._h)
                    # map alert
                    if "ennemy_ter" in self._display._button_dic:
                        for button in self._display._button_dic["ennemy_ter"]:
                            if button.is_over(event.pos):
                                self._alert = button._text

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
        self._hive = hive(
            ressource = (100,0,0,0,0),
            prod = (0,0,0,0,0),
            
            # Commencer avec les upgrades concernant la ruche, puis le combat
            # name, lvl, required_level , price, category, possession, placement = (0,0)
            upgrades = [
            upgrade("boost production", 0, 10, [10,"honey"], "hive", False, (0,0),"chong","./Images/bak.jpg"),
            upgrade("saucisse", 0, 12, [10,"honey"], "hive", False, (1,1),"chong","./Images/bak.jpg"),
            upgrade("jajomobile", 0, 0, [10,"honey"], "hive", False, (1,2),"chong","./Images/bak.jpg"),
            upgrade("jajomobile", 0, 0, [10,"honey"], "hive", False, (2,2),"chong","./Images/bak.jpg"),
            upgrade("jajomobile", 0, 0, [10,"honey"], "hive", False, (3,2),"chong","./Images/bak.jpg"),
            upgrade("BONJOUR OLIVIER DE CHEZ CARGLASS", 0, 0, [10,"honey"], "fight", False, (0,0),"chong","./Images/bak.jpg"),
            upgrade("BLACK LIVES MATTER", 0, 0, [10,"honey"], "fight", False, (0,1),"chong","./Images/bak.jpg"),
            upgrade("BLACK LIVES MATTER", 0, 0, [10,"honey"], "fight", False, (1,1),"chong","./Images/bak.jpg")
            ],
            
            territories = [ territory("base", 0, 0, "honey", 5, [], True), 
            territory("base2", 0, 1, "honey", 7, [], True),
            displayed_territory("hauteurs", 0, 0, "honey", 5, [], False, "Abeilles des hauteurs", "Des abeilles qui font le truc oui") 
            ]

            )

        self._database = database()
        self._shop = shop()
        self._tick_update = tick_update(self._hive, self._tick)
        self._live_display = live_display(self._w, self._h, self._hive)


window = window()
window.main_loop()