import pygame
from pygame.locals import *
from create_button import button
from Shop import shop
from Hive import hive
from math import floor

class display():
    
    def __init__(self):
        self._button_dic = {}
        self._background = None
    
    def display_new_game(self, w, h, first_time):
        surface = pygame.Surface((1920,1080))
        self._background = pygame.image.load('./Images/greywp.jpg')
        surface.blit(self._background, (0, 0))
        if first_time is True:
            self._button_dic = {
                "quit_button" : button((212,180,0), 1720, 985, 180, 75, w, h,'Quitter', font='comicsans', sizeFont=50),
                "launch_game_button" : button((255,180,255), 720, 100, 480, 100, w, h, 'Nouvelle Partie', sizeFont=60)
            }
        else:
             self._button_dic = {
                "quit_button" : button((212,180,0), 1720, 985, 180, 75, w, h,'Quitter', font='comicsans', sizeFont=50),
                "launch_game_button" : button((255,180,255), 720, 100, 480, 100, w, h, 'Continuer Partie', sizeFont=60)
            }

        self._button_dic['quit_button'].draw_button(surface)
        self._button_dic['launch_game_button'].draw_button(surface)

        return surface
    
    def display_menu(self, w, h):
        surface = pygame.Surface((1920,1080))
        # On désinitialise nos boutons quit et launch
        self._button_dic = {
            "bees_button" : button((212,180,0), 720, 203, 480, 75, w, h, 'Gestion des Abeilles', sizeFont=50),
            "upgrade_button" : button((212,180,0), 720, 403, 480, 75, w, h, 'Améliorations', sizeFont=50),
            "shop_button" : button((212,180,0), 720, 603, 480, 75, w, h, 'Magasin', sizeFont=50),
            "fight_menu_button" : button((212,180,0), 720, 803, 480, 75, w, h, 'Combat!', sizeFont=50),
            "quit_button" : button((212,180,0), 1720, 985, 180, 75, w, h,'Quitter', font='comicsans', sizeFont=50)
        }
        #On redessine le background
        #self._background.fill((255,255,255))
        surface.blit(self._background, (0, 0))
        #Bouton Bees
        self._button_dic['bees_button'].draw_button(surface)
        #Boutons upgrade
        self._button_dic['upgrade_button'].draw_button(surface)
        #Bouton Shop
        self._button_dic['shop_button'].draw_button(surface)
        #Bouton Fight
        self._button_dic['fight_menu_button'].draw_button(surface)
        # Bouton Quitter
        self._button_dic['quit_button'].draw_button(surface)
        
        return surface

    # def display_fight_upgrades(self, w, h, hive):
    #     surface = pygame.Surface((1920,1080))
    #     surface.blit(self._background, (0, 0))
        

    #     self._button_dic = {
    #         "back_button" : button((212,180,0), 1720, 985, 180, 75, w, h,'Retour', font='comicsans', sizeFont=50)
    #     }
    #     self._button_dic["back_button"].draw_button(surface)
        
    #     return surface
    
    def display_upgrades(self, w, h, hive, upgrade_type):
        # name, lvl, required_level , price, category, possession, placement = (0,0)

        # mettre les bonnes upgrades
        upgrades = []
        for row in hive._upgrades:
            if row._category == upgrade_type:
                upgrades.append(row)
        print(upgrades)
        # upgrades = hive._upgrades
        surface = pygame.Surface((1920,1080))
        surface.blit(self._background, (0, 0))

        # Déterminer la taille de la matrice
        #print(range (0, len(upgrades) - 1))
        max_x = 0
        max_y = 0
        for i in range (0, len(upgrades) - 1): 
            #print(f"upgrade i: {upgrades[i]._placement[0]}  upgrade i+1: {upgrades[i + 1]._placement[0]}")
            if upgrades[i]._placement[0] > upgrades[i + 1]._placement[0]:
                max_x = upgrades[i]._placement[0]
            elif upgrades[i]._placement[0] < upgrades[i + 1]._placement[0]:
                max_x = upgrades[i + 1]._placement[0]
            if upgrades[i]._placement[1] > upgrades[i + 1]._placement[1]:
                max_y = upgrades[i]._placement[1]
            elif upgrades[i]._placement[1] < upgrades[i + 1]._placement[1]:
                max_y = upgrades[i + 1]._placement[1]
        
        # Création de la matrice des upgrades
        print(max_x)
        list_up = [[0 for i in range(max_y + 1)] for j in range(max_x + 1)]

        for upgrade in upgrades:
            list_up[upgrade._placement[0]][upgrade._placement[1]] = upgrade

        # print(list_up)

        # taille de la surface
        width = 1200 
        height = 600
        total_height = 0
        font = pygame.font.SysFont('comicsans', 50)
        surface_dic = {}
        surface_dic['surface'] = []
        surface_dic['buttons'] = []
        cpt = -1

        for row in list_up:
            surface_dic['surface'].append(pygame.Surface((width, height), pygame.SRCALPHA))
            cpt += 1
            total_height += height
            x = 0
            for upgrade in row:
                if upgrade != 0:
                    image = pygame.image.load(upgrade.sprite())
                    surface_dic['surface'][cpt].blit(image, (x, 55))
                    prod = font.render(upgrade.name() + " lvl" + str(upgrade.lvl()) , 1, (0,0,0))
                    surface_dic['surface'][cpt].blit(prod, (x, 0))

                    print(f"test {upgrade.name()} {upgrade.possession()}")

                    prix = font.render( "Prix: " + str(upgrade.price()[1]), 1, (0,0,0))
                    surface_dic['surface'][cpt].blit(prix, (x, 300))

                    if upgrade.price()[0] == "honey":
                        image = pygame.image.load("./Images/honey.png")
                        surface_dic['surface'][cpt].blit(pygame.transform.scale(image, (45, 45)), ( x + 80 + 20*len(str(upgrade.price()[1])), 293 ))
                    elif upgrade.price()[0] == "water":
                        image = pygame.image.load("./Images/water.png")
                        surface_dic['surface'][cpt].blit(pygame.transform.scale(image, (30, 30)), ( x + 90 + 20*len(str(upgrade.price()[1])), 300 ))
                    elif upgrade.price()[0] == "metal":
                        image = pygame.image.load("./Images/metal.png")
                        surface_dic['surface'][cpt].blit(pygame.transform.scale(image, (30, 30)), ( x + 90 + 20*len(str(upgrade.price()[1])), 300 ))
                    elif upgrade.price()[0] == "uranium":
                        image = pygame.image.load("./Images/uranium.png")
                        surface_dic['surface'][cpt].blit(pygame.transform.scale(image, (30, 30)), ( x + 90 + 20*len(str(upgrade.price()[1])), 300 ))
                    elif upgrade.price()[0] == "pollen":
                        image = pygame.image.load("./Images/pollen.png")
                        surface_dic['surface'][cpt].blit(pygame.transform.scale(image, (30, 30)), ( x + 90 + 20*len(str(upgrade.price()[1])), 300 ))
                    
                    if upgrade.required_level() > hive.level():
                        button_temp = button((169, 169, 169), x, 450, 300, 75, w, h,"Niveau " + str(upgrade.required_level()) + " requis" , font='comicsans', sizeFont=50, get=None)
                        surface_dic["buttons"].append(button_temp)
                        button_temp.draw_button(surface_dic["surface"][cpt])
                    elif upgrade.possession() == True:
                        button_temp = button((169, 169, 169), x, 450, 300, 75, w, h,"Possédé" , font='comicsans', sizeFont=50, get=None)
                        surface_dic["buttons"].append(button_temp)
                        button_temp.draw_button(surface_dic["surface"][cpt])
                    else:
                        button_temp = button((212,180,0), x, 450, 300, 75, w, h, "Acheter", font='comicsans', sizeFont=50, get = [upgrade.name(),upgrade.lvl()])
                        surface_dic["buttons"].append(button_temp)
                        button_temp.draw_button(surface_dic["surface"][cpt])

                    button_temp = button((212,180,0), x, 350, 300, 75, w, h, "Description", font='comicsans', sizeFont=50, get = "Test 1: chong")#[upgrade.name(),upgrade.lvl()])
                    surface_dic["buttons"].append(button_temp)
                    button_temp.draw_button(surface_dic["surface"][cpt])

                x += 400

        final_surface = pygame.Surface((width, total_height), pygame.SRCALPHA)
        y = 0
        for surface_temp in surface_dic['surface']:
            final_surface.blit(surface_temp, (0, y))
            y += height

        surface_dic['surface'] = final_surface  

        
        # Détermine le nombre d'amélioration par ligne (utile pour déterminer la position des boutons)
        cpt_list = [0 for y in range(len(list_up))]
        for i in range(0, len(list_up)):
            for thing in list_up[i]:
                if thing != 0:
                    cpt_list[i] += 1

        
        for i in range (0, len(surface_dic["buttons"])):
            surface_dic["buttons"][i]._x += 400
            surface_dic["buttons"][i]._y += 200

        decal = 600
        total_height = 375
        but_id = -1
        for value in cpt_list:
            for i in range(value):
                but_id += 1
                surface_dic["buttons"][but_id]._y = total_height
            total_height += decal

        # for i in range (3, len(surface_dic['buttons'])):
            
        #     if i % 3 == 0 and i != 3:
        #         value += height
        #     surface_dic['buttons'][i]._y += value

        
        # for butts in surface_dic["buttons"]:
            

        self._button_dic["back_button"] = button((212,180,0), 1720, 985, 180, 75, w, h,'Retour', font='comicsans', sizeFont=50)
        
        self._button_dic["back_button"].draw_button(surface)
        return surface, surface_dic

    def display_map(self, w, h):
        surface = pygame.Surface((1920,1080))

        map_pic = pygame.image.load('./Images/last.jpg')
        surface.blit(map_pic, (0, 0))

        self._button_dic = {
            "ennemy_ter" : [
                button((0,0,0), 328, 42, 270, 118, w, h,'hauteurs', font='comicsans', sizeFont=50),
                button((0,0,0), 497, 205, 186, 131, w, h,'urbaines', font='comicsans', sizeFont=50),
                button((0,0,0), 770, 16, 236, 100, w, h,'profondeurs', font='comicsans', sizeFont=50),
                button((0,0,0), 1218, 135, 183, 118, w, h,'mutantes', font='comicsans', sizeFont=50),
                button((0,0,0), 714, 277, 184, 75, w, h,'plaines', font='comicsans', sizeFont=50),
                button((0,0,0), 694, 436, 203, 86, w, h,'solitaires', font='comicsans', sizeFont=50),
                button((0,0,0), 628, 628, 208, 176, w, h,'arboricoles', font='comicsans', sizeFont=50),
                button((0,0,0), 1155, 591, 178, 205, w, h,'ruines', font='comicsans', sizeFont=50),
                button((0,0,0), 1049, 799, 180, 78, w, h,'eau douce', font='comicsans', sizeFont=50),
                button((0,0,0), 1088, 938, 84, 113, w, h,'tour', font='comicsans', sizeFont=50),
                button((0,0,0), 1442, 377, 217, 241, w, h,'macabres', font='comicsans', sizeFont=50),
                button((0,0,0), 317, 876, 79, 111, w, h,'RUSSIA', font='comicsans', sizeFont=50),
                button((0,0,0), 252, 356, 193, 313, w, h,'rurales', font='comicsans', sizeFont=50)
            ],
            "back_button" : button((212,180,0), 1720, 985, 180, 75, w, h,'Retour', font='comicsans', sizeFont=50)
        }
        self._button_dic["back_button"].draw_button(surface)
    
        return surface

    def display_management_bee(self, bees, w, h, scroll_y):
        
        font = pygame.font.SysFont('comicsans', 50)
        
        i = 0
        
        surface_dic = {}
        surface_dic['surface'] = []
        surface_dic['buttons'] = []
        height = 450
        width = 1500
        total_height = 0
        
        for i in range (0, len(bees)):
            
            indice = floor(i / 3) # Pour accéder à la bonne surface
           
            if i % 3 == 0:
                x = 100
                surface_dic['surface'].append(pygame.Surface((width, height), pygame.SRCALPHA)) # pygame.SRCALPHA créé une surface transparente dans laquelle on peut ajouter des éléments qui eux s'afficheront 
                total_height += height

            # nom abeille 
            nom_abeille = font.render(bees[i][0]._name, 1, (0,0,0))
            surface_dic['surface'][indice].blit(nom_abeille, (x, 0))
            # prix
            prix = font.render(str(bees[i][1]), 1, (0,0,0))
            surface_dic['surface'][indice].blit(prix, (x, 50))
            # image abeille
            image = pygame.image.load(bees[i][0]._sprite)
            surface_dic['surface'][indice].blit(image, (x, 100))
            # boutons
            bouton = button((212,180,0), x, 300, 180, 75, w, h,'Supprimer', font='comicsans', sizeFont=50, get=bees[i][0]._name)
            surface_dic['buttons'].append(bouton)
            bouton.draw_button(surface_dic['surface'][indice])

            x += 350 

        for i in range (0, len(surface_dic['buttons'])):
            surface_dic['buttons'][i]._x += 400
            surface_dic['buttons'][i]._y += 250 + scroll_y

        value = 450
        for i in range (3, len(surface_dic['buttons'])):
            
            if i % 3 == 0 and i != 3:
                value += 450
            surface_dic['buttons'][i]._y += value


        final_surface = pygame.Surface((width, total_height), pygame.SRCALPHA)
        y = 0
        for surface in surface_dic['surface']:
            final_surface.blit(surface, (0, y))
            y += height
        
        surface_dic['surface'] = final_surface
        
        return surface_dic

    def display_management(self, w, h, hive, scroll_y):
        surface = pygame.Surface((1920,1080))
        self._button_dic = {
            "back_button" : button((255,180,255), 1700, 130, 180, 75, w, h, 'back', sizeFont=60),
            "quit_button" : button((212,180,0), 1700, 20, 180, 75, w, h,'Quitter', font='comicsans', sizeFont=50),
        }
        
            
        # Affichage basique
        surface.blit(self._background, (0, 0))
          
        font = pygame.font.SysFont('comicsans', 50)
        welcome = font.render("Bienvenue dans votre ruche !", 1, (0,0,0))
        surface.blit(welcome, (150, 120))

        #infos de la ruche
        bees_possessed = font.render("Abeilles posédées : " + str(len(hive._bees)), 1, (0,0,0))
        surface.blit(bees_possessed, (150, 160))

        #infos sur les abeilles possédées
        list_bee = {}
        if len((hive._bees)) > 0:
            #ON FAIT DE LA MAGIE CIANTE
            list_bee = {}
            
            for bee in hive._bees:
                if bee._name not in list_bee:
                    list_bee[bee._name] = [bee, 1]
                else:
                    list_bee[bee._name][1] += 1 
            list_bee.items()
            list_bee = list_bee.values()
            list_bee = list(list_bee)

        bees_surface = self.display_management_bee(list_bee, w, h, scroll_y)
        self._button_dic["quit_button"].draw_button(surface)
        self._button_dic["back_button"].draw_button(surface)
             
        return surface, bees_surface
    
    def display_shop_bee(self, bees, hive, w, h):
        
        font = pygame.font.SysFont('comicsans', 50)
        
        i = 0
        
        surface_dic = {}
        surface_dic['surface'] = []
        surface_dic['buttons'] = []
        height = 550
        width = 1800
        total_height = 0
        for i in range (0, len(bees)):
            
            indice = floor(i / 3) # Pour accéder à la bonne surface
            
           
            if i % 3 == 0:
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

            if bees[i].category() == "worker":
                prod = font.render("Production: " + str(bees[i].prod()) + "    /s" , 1, (0,0,0))
                surface_dic['surface'][indice].blit(prod, (x, 300))

                if bees[i].ressource() == "honey":
                    image = pygame.image.load("./Images/honey.png")
                    surface_dic['surface'][indice].blit(pygame.transform.scale(image, (45, 45)), ( x + 200 + 20*len(str(bees[i].prod())), 293 ))
                elif bees[i].ressource() == "water":
                    image = pygame.image.load("./Images/water.png")
                    surface_dic['surface'][indice].blit(pygame.transform.scale(image, (30, 30)), ( x + 210 + 20*len(str(bees[i].prod())), 300 ))
                elif bees[i].ressource() == "metal":
                    image = pygame.image.load("./Images/metal.png")
                    surface_dic['surface'][indice].blit(pygame.transform.scale(image, (30, 30)), ( x + 210 + 20*len(str(bees[i].prod())), 300 ))
                elif bees[i].ressource() == "uranium":
                    image = pygame.image.load("./Images/uranium.png")
                    surface_dic['surface'][indice].blit(pygame.transform.scale(image, (30, 30)), ( x + 210 + 20*len(str(bees[i].prod())), 300 ))
                elif bees[i].ressource() == "pollen":
                    image = pygame.image.load("./Images/pollen.png")
                    surface_dic['surface'][indice].blit(pygame.transform.scale(image, (30, 30)), ( x + 210 + 20*len(str(bees[i].prod())), 300 ))


                if bees[i]._price[1] == "honey":
                    image = pygame.image.load("./Images/honey.png")
                    surface_dic['surface'][indice].blit(pygame.transform.scale(image, (45, 45)), ( x + 80 + 20*len(str(bees[i]._price[0])), 393 ))
                elif bees[i].ressource() == "water":
                    image = pygame.image.load("./Images/water.png")
                    surface_dic['surface'][indice].blit(pygame.transform.scale(image, (30, 30)), ( x + 90 + 20*len(str(bees[i]._price[0])), 400 ))
                elif bees[i].ressource() == "metal":
                    image = pygame.image.load("./Images/metal.png")
                    surface_dic['surface'][indice].blit(pygame.transform.scale(image, (30, 30)), ( x + 90 + 20*len(str(bees[i]._price[0])), 400 ))
                elif bees[i].ressource() == "uranium":
                    image = pygame.image.load("./Images/uranium.png")
                    surface_dic['surface'][indice].blit(pygame.transform.scale(image, (30, 30)), ( x + 90 + 20*len(str(bees[i]._price[0])), 400 ))
                elif bees[i].ressource() == "pollen":
                    image = pygame.image.load("./Images/pollen.png")
                    surface_dic['surface'][indice].blit(pygame.transform.scale(image, (30, 30)), ( x + 90 + 20*len(str(bees[i]._price[0])), 400 ))

                cost = font.render("Coût d'entretien: " + str(bees[i].cost()) , 1, (0,0,0))
                surface_dic['surface'][indice].blit(cost, (x, 350))

                prix = font.render( "Prix: " + str(bees[i]._price[0]), 1, (0,0,0))
                surface_dic['surface'][indice].blit(prix, (x, 400))
            
            # boutons
            if bees[i].required_level() <= hive.level():
                bouton = button((212,180,0), x, 450, 300, 75, w, h,'Acheter', font='comicsans', sizeFont=50, get=bees[i]._name)
                surface_dic['buttons'].append(bouton)
                bouton.draw_button(surface_dic['surface'][indice])
            else:
                bouton = button((169, 169, 169), x, 450, 300, 75, w, h,"Niveau " + str(bees[i].required_level()) + " requis" , font='comicsans', sizeFont=50, get=None)
                bouton.draw_button(surface_dic['surface'][indice])

            x += 450 

        for i in range (0, len(surface_dic['buttons'])):
            surface_dic['buttons'][i]._x += 200
            surface_dic['buttons'][i]._y += 250

        value = 550
        for i in range (3, len(surface_dic['buttons'])):
            
            if i % 3 == 0 and i != 3:
                value += 550
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

        # liste des surfaces
        bees_surfaces = self.display_shop_bee(shop_bees, hive, w, h)

        # Bouton Quitter

        self._button_dic["quit_button"].draw_button(surface)
        self._button_dic["back_button"].draw_button(surface)
        # 
        return surface, bees_surfaces
    
    