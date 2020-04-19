import pygame
from Create_button import button

class display():
    
    def __init__(self):
        button_list = []
    
    def display_menu(self, w, h):

        surface = pygame.Surface((1920,1080))
        background = pygame.image.load('./Images/fond.jpg')
        surface.blit(background, (0, 0))
        self._quit_button = button((212,180,0), 1720, 985, 180, 75, w, h,'Quitter', font='comicsans', sizeFont=50)
        self._quit_button.draw_button(surface)
        self._launch_game_button = button((255,180,255), 100, 500, 180, 75, 'Nouvelle Partie', sizeFont=50)
        self._launch_game_button.draw_button(surface)

        return surface
    
    def display_new_game(self):
        # On désinitialise nos boutons quit et launch
        self._quit_button = None
        self._launch_game_button = None
        #On redessine le background
        self._background.fill((255,255,255))
        self._window.blit(self._background, (0, 0))
        #Bouton Bees
        self._bees_button = button((212,180,0), 0, 0, 480, 75, 'Gestion des Abeilles', sizeFont=50)
        self._bees_button.draw_button(self._window)
        #Bouton Shop
        self._shop_button = button((212,180,0), 0, 100, 480, 75, 'Magasin', sizeFont=50)
        self._shop_button.draw_button(self._window)
        #Bouton Fight
        self._fight_button = button((212,180,0), 0, 200, 480, 75, 'Combat!', sizeFont=50)
        self._fight_button.draw_button(self._window)

    def display_management(self):
        print("Gestion des Abeilles en developpement!")
    
    def display_shop(self):
        print("Magasin en developpement!")
    
    def display_fight(self):
        print("Guerre en préparation!")
