import pygame
from create_button import button
from Shop import shop
from Hive import hive
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

    def display_management_bee_list(self, bee, x, y, surface):

        if bee is not None:
            font = pygame.font.SysFont('comicsans', 50)
            name = font.render("Nom :" + str(bee.name()), 1, (0,0,0))
            price = font.render("prix :" + str(bee.price()), 1, (0,0,0))
            sprite = bee.sprite()
            if sprite is not None:
                image = pygame.image.load(sprite)
                surface.blit(image, (x, y + 50))
                y += image.get_height()
            surface.blit(name, (x, y + 100))
            surface.blit(price, (x, y + 150))
        else:
            pass

    def display_management(self, w, h, hive, first_time, step):
        surface = pygame.Surface((1920,1080))
        self._button_dic = {
            "get_honey_button" : button((255,180,255), 1500, 300, 100, 100, w, h, 'Get MIEL', sizeFont=30),
            "back_button" : button((255,180,255), 1700, 300, 480, 100, w, h, 'back', sizeFont=60),
        }

        # Affichage basique
        surface.blit(self._background, (0, 0))
        font = pygame.font.SysFont('comicsans', 50)
        welcome = font.render("Bienvenue dans votre ruche !", 1, (0,0,0))
        surface.blit(welcome, (150, 120))

        #infos de la ruche
        honey = font.render("Miel disponible : " + str(hive._honey), 1, (0,0,0))
        bees_possessed = font.render("Abeilles posédées : " + str(len(hive._bees)), 1, (0,0,0))
        surface.blit(honey, (150, 170))
        surface.blit(bees_possessed, (150, 220))

        #infos sur les abeilles possédées
        if len((hive._bees)) > 0:
            beelist = font.render("Liste d'abeilles : ", 1, (0,0,0))
            surface.blit(beelist, (150, 270))
            if first_time is True:
                self.cpt = 0
                self.display_management_bee_list(hive._bees[self.cpt], 150, 290, surface)
                print('compteur : ' + str(self.cpt))
                print('taille : ' + str(len((hive._bees))))
                if self.cpt < len((hive._bees)) -1 :
                    self._button_dic["next_bee"] = button((255,0,0), 1300, 985, 180, 75, w, h,'Suivant', font='comicsans', sizeFont=50)
                    self._button_dic["next_bee"].draw_button(surface)
                else:
                    pass
            else: 
                if step is True:
                    self.cpt +=1
                    self.display_management_bee_list(hive._bees[self.cpt], 150, 290, surface)
                    if self.cpt < len((hive._bees)) -1 :
                        self._button_dic["next_bee"] = button((255,0,0), 1300, 985, 180, 75, w, h,'Suivant', font='comicsans', sizeFont=50)
                        self._button_dic["next_bee"].draw_button(surface)
                    if self.cpt > 0:
                        self._button_dic["back_bee"] = button((255,0,0), 1000, 985, 180, 75, w, h,'Précédent', font='comicsans', sizeFont=50)
                        self._button_dic["back_bee"].draw_button(surface)
                elif step is False:
                    self.cpt -=1
                    self.display_management_bee_list(hive._bees[self.cpt], 150, 290, surface)
                    if self.cpt < len((hive._bees)) -1 :
                        self._button_dic["next_bee"] = button((255,0,0), 1300, 985, 180, 75, w, h,'Suivant', font='comicsans', sizeFont=50)
                        self._button_dic["next_bee"].draw_button(surface)
                    if self.cpt > 0:
                        self._button_dic["back_bee"] = button((255,0,0), 1000, 985, 180, 75, w, h,'Précédent', font='comicsans', sizeFont=50)
                        self._button_dic["back_bee"].draw_button(surface)

        #boutons de tests
        print("Gestion des Abeilles en developpement!")
        self._button_dic['get_honey_button'].draw_button(surface)
        self._button_dic['back_button'].draw_button(surface)
        return surface
    
    def display_shop_bee(self, surface, bee, x, y, w, h, button_id):
        #on créé nos objets abeilles spécifiques au magasin
        font = pygame.font.SysFont('comicsans', 50)
        bee_shop = bee
        name = font.render("Nom :" + str(bee_shop.name()), 1, (0,0,0))
        price = font.render("prix :" + str(bee_shop.price()), 1, (0,0,0))
        sprite = bee_shop.sprite()
        if sprite is not None:
            image = pygame.image.load(sprite)
            surface.blit(image, (x, y + 50))
            y += image.get_height()
        surface.blit(name, (x, y + 100))
        surface.blit(price, (x, y + 150))
        test = button((212,180,0), x, y + 200, 180, 75, w, h,'Acheter','comicsans', 50, button_id)
        test.draw_button(surface)

        return test

    def display_shop(self, w, h, shop_bees,hive):
        #on redessine la surface
        surface = pygame.Surface((1920,1080))
        surface.blit(self._background, (0, 0))

        # création du texte du shop
        font = pygame.font.SysFont('comicsans', 50)
        print("Magasin en developpement!")
        welcome = font.render("Bienvenue dans le magasin", 1, (0,0,0))
        buy = font.render("Achetez des Abeilles!", 1, (0,0,0))
        surface.blit(welcome, (150, 120))
        surface.blit(buy, (150, 170))

        #Init des botuons
        self._button_dic = {
            "buy_bee_button" : [],
            "quit_button" : button((212,180,0), 1720, 985, 180, 75, w, h,'Quitter', font='comicsans', sizeFont=50),
            "back_button" : button((255,180,255), 1700, 300, 480, 100, w, h, 'back', sizeFont=60)
        }

        #affichage des abeilles, le x sert a positionner nos objects
        x = 150
        for bees in shop_bees:
            self._button_dic["buy_bee_button"].append(self.display_shop_bee(surface, bees, x, 220,w ,h, bees._name))
            x += 450
        print(self._button_dic["buy_bee_button"])
        # Bouton Quitter

        self._button_dic["quit_button"].draw_button(surface)
        self._button_dic["back_button"].draw_button(surface)
        # 
        return surface
    
    def display_fight(self):
        surface = pygame.Surface((1920,1080))
        self._button_dic = {}
        print("Guerre en préparation!")
        return surface