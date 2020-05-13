import pygame
from create_button import button
from Shop import shop
from Hive import hive
from math import floor

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

    def display_management_bee_list(self, bee, x, y, surface, bee_number):

        if bee is not None:
            font = pygame.font.SysFont('comicsans', 50)
            name = font.render("Nom : " + str(bee.name()), 1, (0,0,0))
            number = font.render("Nombre possédé : " + str(bee_number), 1, (0,0,0))
            category = font.render("Catégorie : " + bee._category, 1, (0,0,0))
            prod = font.render("Capacité de production : " + str(bee._prod), 1, (0,0,0))
            
            sprite = bee.sprite()
            if sprite is not None:
                image = pygame.image.load(sprite)
                surface.blit(image, (x, y + 50))
                y += image.get_height()
            surface.blit(name, (x, y + 100))
            surface.blit(number, (x, y + 150))
            surface.blit(category, (x, y + 200))
            surface.blit(prod, (x, y + 250))
        else:
            pass

    def display_management(self, w, h, hive, first_time, step):
        surface = pygame.Surface((1920,1080))
        self._button_dic = {
            "get_honey_button" : button((255,180,255), 1700, 20, 180, 75, w, h, 'Get MIEL', sizeFont=30),
            "back_button" : button((255,180,255), 1700, 130, 180, 75, w, h, 'back', sizeFont=60),
        }
        
            
            
        # Affichage basique
        surface.blit(self._background, (0, 0))
        font = pygame.font.SysFont('comicsans', 50)
        welcome = font.render("Bienvenue dans votre ruche !", 1, (0,0,0))
        surface.blit(welcome, (150, 120))

        #infos de la ruche
        # honey = font.render("Miel disponible : " + str(hive._honey), 1, (0,0,0))
        bees_possessed = font.render("Abeilles posédées : " + str(len(hive._bees)), 1, (0,0,0))
        # surface.blit(honey, (150, 170))
        surface.blit(bees_possessed, (150, 220))

        #infos sur les abeilles possédées
        if len((hive._bees)) > 0:
            #ON FAIT DE LA MAGIE CIANTE
            list_bee = {}
            
            for bee in hive._bees:
                print(bee._name)
                if bee._name not in list_bee:
                    list_bee[bee._name] = [bee, 1]
                else:
                    list_bee[bee._name][1] += 1 
            list_bee.items()
            list_bee = list_bee.values()
            list_bee = list(list_bee)
            print(list_bee)
            #AFFICHAGE DEUSPI
            beelist = font.render("Liste d'abeilles : ", 1, (0,0,0))
            surface.blit(beelist, (150, 270))
            #INTERFACE QUI AFFICHE LES ABEILLES PAR GROUPE
            if first_time is True:
                self.cpt = 0
                self.display_management_bee_list(list_bee[self.cpt][0], 150, 290, surface, list_bee[self.cpt][1])
                print('compteur : ' + str(self.cpt))
                print('taille : ' + str(len((list_bee))))
                if self.cpt < len((list_bee)) -1 :
                    self._button_dic["next_bee"] = button((255,0,0), 1300, 985, 180, 75, w, h,'Suivant', font='comicsans', sizeFont=50)
                    self._button_dic["next_bee"].draw_button(surface)
                else:
                    pass
            else: 
                if step is True:
                    self.cpt +=1
                    self.display_management_bee_list(list_bee[self.cpt][0],150, 290, surface, list_bee[self.cpt][1])
                    if self.cpt < len((list_bee)) -1 :
                        self._button_dic["next_bee"] = button((255,0,0), 1300, 985, 180, 75, w, h,'Suivant', font='comicsans', sizeFont=50)
                        self._button_dic["next_bee"].draw_button(surface)
                    if self.cpt > 0:
                        self._button_dic["back_bee"] = button((255,0,0), 1000, 985, 180, 75, w, h,'Précédent', font='comicsans', sizeFont=50)
                        self._button_dic["back_bee"].draw_button(surface)
                elif step is False:
                    self.cpt -=1
                    self.display_management_bee_list(list_bee[self.cpt][0], 150, 290, surface, list_bee[self.cpt][1])
                    if self.cpt < len((list_bee)) -1 :
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
    
    def display_shop_bee(self, bees, w, h):
        
        font = pygame.font.SysFont('comicsans', 50)
        
        i = 0
        
        surface_dic = {}
        surface_dic['surface'] = []
        surface_dic['buttons'] = []
        height = 450
        width = 1500
        total_height = 0
        for i in range (0, len(bees)):
            
            indice = floor(i / 2) # Pour accéder à la bonne surface
           
            if i % 2 == 0:
                x = 100
                surface_dic['surface'].append(pygame.Surface((width, height), pygame.SRCALPHA)) # pygame.SRCALPHA créé une surface transparente dans laquelle on peut ajouter des éléments qui eux s'afficheront 
                total_height += height

            # nom abeille
            nom_abeille = font.render(bees[i]._name, 1, (0,0,0))
            surface_dic['surface'][indice].blit(nom_abeille, (x, 0))
            # image abeille
            image = pygame.image.load(bees[i]._sprite)
            surface_dic['surface'][indice].blit(image, (x, 50))
            # prix
            prix = font.render(str(bees[i]._price), 1, (0,0,0))
            surface_dic['surface'][indice].blit(prix, (x, 250))
            # boutons
            bouton = button((212,180,0), x, 300, 180, 75, w, h,'Acheter', font='comicsans', sizeFont=50, get=bees[i]._name)
            surface_dic['buttons'].append(bouton)
            bouton.draw_button(surface_dic['surface'][indice])

            x += 600 

        for i in range (0, len(surface_dic['buttons'])):
            surface_dic['buttons'][i]._x += 400
            surface_dic['buttons'][i]._y += 250

        for i in range (2, len(surface_dic['buttons'])):
            value = 450
            if i % 2 == 0 and i != 2:
                value += 450
            surface_dic['buttons'][i]._y += value


        final_surface = pygame.Surface((width, total_height), pygame.SRCALPHA)
        y = 0
        for surface in surface_dic['surface']:
            final_surface.blit(surface, (0, y))
            y += height
        
        surface_dic['surface'] = final_surface
        

        return surface_dic

    def display_shop(self, w, h, shop_bees, hive):
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

        #Init des boutons
        self._button_dic = {
            "buy_bee_button" : [],
            "quit_button" : button((212,180,0), 1700, 20, 180, 75, w, h,'Quitter', font='comicsans', sizeFont=50),
            "back_button" : button((255,180,255), 1700, 130, 180, 75, w, h, 'back', sizeFont=60)
        }

        #affichage des abeilles, le x sert a positionner nos objects
        # x = 150
        # for bees in shop_bees:
        #     self._button_dic["buy_bee_button"].append(self.display_shop_bee(surface, bees, x, 220,w ,h, bees._name))
        #     x += 450

        # liste des surfaces
        bees_surfaces = self.display_shop_bee(shop_bees, w, h)

        # Bouton Quitter

        self._button_dic["quit_button"].draw_button(surface)
        self._button_dic["back_button"].draw_button(surface)
        # 
        return surface, bees_surfaces
    
    def display_fight(self):
        surface = pygame.Surface((1920,1080))
        self._button_dic = {}
        print("Guerre en préparation!")
        return surface