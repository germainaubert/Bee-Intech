import pygame
from create_button import button
from Shop import shop

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
        #self._background.fill((255,255,255))
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
        self._bees_button = None
        self._shop_button = None
        self._fight_button = None
        print("Gestion des Abeilles en developpement!")
        return surface
    
    def display_shop_bee(self, bee, x, y, filename, w, h):
        font = pygame.font.SysFont('comicsans', 50)
        bee_shop = bee
        name = font.render("Nom :" + str(bee_shop._name), 1, (0,0,0))
        price = font.render("prix :" + str(bee_shop._price), 1, (0,0,0))
        if filename is not None:
            image = pygame.image.load(filename)
            self.blit(image, (x, y + 50))
            y += image.get_height()
        self.blit(name, (x, y + 100))
        self.blit(price, (x, y + 150))
        buy_bee_button = button((212,180,0), x, y + 200, 180, 75, w, h,'Acheter', font='comicsans', sizeFont=50)
        buy_bee_button.draw_button(self)


    def display_shop(self, w, h):
        #on redessine la surface
        surface = pygame.Surface((1920,1080))
        surface.blit(self._background, (0, 0))
        #desac les buttons
        self._bees_button = None
        self._shop_button = None
        self._fight_button = None
        # création du texte du shop
        print("Magasin en developpement!")
        font = pygame.font.SysFont('comicsans', 50)
        welcome = font.render("Bienvenue dans le magasin", 1, (0,0,0))
        buy = font.render("Achetez des Abeilles!", 1, (0,0,0))
        surface.blit(welcome, (150, 120))
        surface.blit(buy, (150, 170))
        display.display_shop_bee(surface, self.shop._bees[0], 150, 220,"./Images/bak.jpg",w ,h)
        # 
        return surface
    
    def display_fight(self):
        surface = pygame.Surface((1920,1080))
        self._bees_button = None
        self._shop_button = None
        self._fight_button = None
        print("Guerre en préparation!")
        return surface