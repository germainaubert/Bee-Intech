import pygame
from create_button import button

class display():
    
    def __init__(self):
        button_list = []
        _background = None
    
    def display_menu(self, w, h):
        surface = pygame.Surface((1920,1080))
        self._background = pygame.image.load('./Images/fond.jpg')
        surface.blit(self._background, (0, 0))
        self._quit_button = button((212,180,0), 1720, 985, 180, 75, w, h,'Quitter', font='comicsans', sizeFont=50)
        self._quit_button.draw_button(surface)
        self._launch_game_button = button((255,180,255), 720, 100, 480, 100, w, h, 'Nouvelle Partie', sizeFont=60)
        self._launch_game_button.draw_button(surface)

        return surface
    
    def display_new_game(self, w, h):
        surface = pygame.Surface((1920,1080))
        # On désinitialise nos boutons quit et launch
        self._quit_button = None
        self._launch_game_button = None
        #On redessine le background
        # self._background.fill((255,255,255))
        surface.blit(self._background, (0, 0))
        #Bouton Bees
        self._bees_button = button((212,180,0), 720, 303, 480, 75, w, h, 'Gestion des Abeilles', sizeFont=50)
        self._bees_button.draw_button(surface)
        #Bouton Shop
        self._shop_button = button((212,180,0), 720, 503, 480, 75, w, h, 'Magasin', sizeFont=50)
        self._shop_button.draw_button(surface)
        #Bouton Fight
        self._fight_button = button((212,180,0), 720, 703, 480, 75, w, h, 'Combat!', sizeFont=50)
        self._fight_button.draw_button(surface)
        # Bouton Quitter
        self._quit_button = button((212,180,0), 1720, 985, 180, 75, w, h,'Quitter', font='comicsans', sizeFont=50)
        self._quit_button.draw_button(surface)
        return surface

    def display_management(self):
        surface = pygame.Surface((1920,1080))
        print("Gestion des Abeilles en developpement!")
        return surface
    
    def display_shop(self):
        surface = pygame.Surface((1920,1080))
        print("Magasin en developpement!")
        return surface
    
    def display_fight(self):
        surface = pygame.Surface((1920,1080))
        print("Guerre en préparation!")
        return surface
