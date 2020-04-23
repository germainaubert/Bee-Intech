import pygame
from create_button import button
from Shop import shop

class display():
    
    def __init__(self):
        self._button_dic = {}
        self._background = None
    
    def display_menu(self, w, h):
        surface = pygame.Surface((1920,1080))
        self._background = pygame.image.load('./Images/fond.jpg')
        surface.blit(self._background, (0, 0))
        self._button_dic = {
            "quit_button" : button((212,180,0), 1720, 985, 180, 75, w, h,'Quitter', font='comicsans', sizeFont=50),
            "launch_game_button" : button((255,180,255), 720, 100, 480, 100, w, h, 'Nouvelle Partie', sizeFont=60)
        }

        self._button_dic['quit_button'].draw_button(surface)
        self._button_dic['launch_game_button'].draw_button(surface)

        if "launch_game_button" in self._button_dic:
            print(self._button_dic)

        return surface
    
    def display_new_game(self, w, h):
        surface = pygame.Surface((1920,1080))
        # On désinitialise nos boutons quit et launch
        self._button_dic = {
            "bees_button" : button((212,180,0), 720, 303, 480, 75, w, h, 'Gestion des Abeilles', sizeFont=50),
            "shop_button" : button((212,180,0), 720, 503, 480, 75, w, h, 'Magasin', sizeFont=50),
            "fight_button" : button((212,180,0), 720, 703, 480, 75, w, h, 'Combat!', sizeFont=50),
            "quit_button" : button((212,180,0), 1720, 985, 180, 75, w, h,'Quitter', font='comicsans', sizeFont=50)
        }
        #On redessine le background
        #self._background.fill((255,255,255))
        surface.blit(self._background, (0, 0))
        #Bouton Bees
        self._button_dic['bees_button'].draw_button(surface)
        #Bouton Shop
        self._button_dic['shop_button'].draw_button(surface)
        #Bouton Fight
        self._button_dic['fight_button'].draw_button(surface)
        # Bouton Quitter
        self._button_dic['quit_button'].draw_button(surface)
        return surface

    def display_management(self):
        surface = pygame.Surface((1920,1080))
        self._button_dic = {}
        print("Gestion des Abeilles en developpement!")
        return surface
    
    def display_shop_bee(self, surface, bee, x, y, filename, w, h, button_id):
        font = pygame.font.SysFont('comicsans', 50)
        bee_shop = bee
        name = font.render("Nom :" + str(bee_shop.name()), 1, (0,0,0))
        price = font.render("prix :" + str(bee_shop.price()), 1, (0,0,0))
        if filename is not None:
            image = pygame.image.load(filename)
            surface.blit(image, (x, y + 50))
            y += image.get_height()
        surface.blit(name, (x, y + 100))
        surface.blit(price, (x, y + 150))
        
        self._button_dic = {
            "buy_bee_button" : button((212,180,0), x, y + 200, 180, 75, w, h,'Acheter','comicsans', 50, button_id)
        }
        print(self._button_dic)
        self._button_dic["buy_bee_button"].draw_button(surface)


    def display_shop(self, w, h, shop_bees):
        #on redessine la surface
        surface = pygame.Surface((1920,1080))
        surface.blit(self._background, (0, 0))
        #desac les buttons

        # création du texte du shop
        print("Magasin en developpement!")
        font = pygame.font.SysFont('comicsans', 50)
        welcome = font.render("Bienvenue dans le magasin", 1, (0,0,0))
        buy = font.render("Achetez des Abeilles!", 1, (0,0,0))
        surface.blit(welcome, (150, 120))
        surface.blit(buy, (150, 170))
        self._buy_bee_button = self.display_shop_bee(surface, shop_bees[0], 150, 220,"./Images/bak.jpg",w ,h, shop_bees[0]._name)
        # 
        return surface
    
    def display_fight(self):
        surface = pygame.Surface((1920,1080))
        self._button_dic = {}
        print("Guerre en préparation!")
        return surface