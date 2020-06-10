import pygame
import math
from pygame_textinput import TextInput
from create_button import button
from pygame.locals import *

class live_display():
    _tick = 60
    _shop_input = TextInput()
    _accepted_event1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    _accepted_event2 = [K_BACKSPACE, K_DELETE, K_RETURN, K_RIGHT, K_LEFT, K_END, K_HOME, KEYUP]
    _temp_buttons = None
    _scroll_y = 0

    def __init__(self, w, h, hive):
        self._w = w
        self._h = h
        self._hive = hive

    def give_display(self, live, alert, surface, events, buttons, first_call, bees_surfaces, scroll_y): # permet d'appeler la méthode de live_display correspondant à l'affichage en cours, grâce à live
        if live == "new_game":
             return self.live_new_game(surface)
        elif live == "management":
            return self.live_management(surface, events, buttons, alert, bees_surfaces, scroll_y)  
        elif live == "shop":
            return self.live_shop(surface, events, buttons, alert, first_call, bees_surfaces, scroll_y)
        elif live == "fight_menu":
            return self.live_fight_menu(surface, buttons)
    
    def live_fight_menu(self, surface, buttons):
        return surface, buttons

    def live_new_game(self, surface):
        
        texte = "Miel: " + str(math.ceil(self._hive._ressource["honey"]))
        texte = self.text_rendering("comicsans", 100, texte)
        surface.blit(texte, (0,0))

        return surface

    def live_management(self, surface, events, buttons, alert, bees_surfaces, scroll_y):
        scroll_surface, delete_buttons, scroll_y = self.scroll(bees_surfaces, events, scroll_y)
        
        buttons['delete_bee_button'] = delete_buttons

        texte = "Miel: " + str(math.ceil(self._hive._ressource["honey"]))
        texte = self.text_rendering("comicsans", 100, texte)
        surface.blit(texte, (0,0))

        pos_x = 400
        pos_y = 250
        
        container_surface = pygame.Surface((1100, 850), pygame.SRCALPHA)
        
        container_surface.blit(scroll_surface, (0, scroll_y))

        surface.blit(container_surface, (pos_x, pos_y))

        alert = ""

       

        return surface, "", buttons, alert, scroll_y
       


    def live_shop(self, surface, events, buttons, alert, first_call, bees_surfaces, scroll_y):
        scroll_surface, purchase_buttons, scroll_y = self.scroll(bees_surfaces, events, scroll_y)
        #positionner correctement purchase buttons
    
        
        buttons['buy_bee_button'] = purchase_buttons

        pos_x = 200
        pos_y = 250 # valeurs liées aux boutons de display de la bee_surface
        
        container_surface = pygame.Surface((1500, 850), pygame.SRCALPHA)
        
        container_surface.blit(scroll_surface, (0, scroll_y))

        surface.blit(container_surface, (pos_x, pos_y))
        

        texte = "Miel: " + str(math.ceil(self._hive._ressource["honey"]))
        texte = self.text_rendering("comicsans", 100, texte)
        surface.blit(texte, (0,0))
        
        # print(bees_surfaces[0][1])
        
        delete = False
        give_event = []      
        for event in events:
            if event.type == KEYDOWN:
                for accepted_tchong in self._accepted_event1:
                    if event.unicode == accepted_tchong:
                        give_event.append(event)
                        #print(event)
                        break
                for accepted_tchang in self._accepted_event2:
                    if event.key == accepted_tchang:
                        give_event.append(event)
                        if event.key == K_BACKSPACE:
                            delete = True
                        #print(event)
                        break

        if alert == "Buy":
            if first_call == True:
                self._temp_buttons = buttons
                first_call = False
                buttons = {}
            elif first_call == False:
                black_surface = pygame.Surface((1920,1080), 255)
                black_surface.set_alpha(100)
                surface.blit(black_surface, (0,0))
                input_surface = pygame.Surface((400, 80))
                input_surface.fill(pygame.Color('White'))
                input_surface.blit(self._shop_input.get_surface(), (100,35))
                
                
                
                if len(self._shop_input.get_text()) < 10:
                    self._shop_input.update(give_event)
                elif delete == True:
                    self._shop_input.update(give_event)

                surface.blit(input_surface, (760, 480)) 

                buttons = {"cancel_buy" : button((255,180,255), 860, 615, 200, 80, self._w, self._h, 'Annuler Achat', font='comicsans', sizeFont=35)}
                buttons["cancel_buy"].draw_button(surface)

         

        elif alert == "CantBuy":
            if first_call == True:
                self._temp_buttons = buttons
                first_call = False
                buttons = {}
            elif first_call == False:
                black_surface = pygame.Surface((1920,1080), 255)
                black_surface.set_alpha(100)
                surface.blit(black_surface, (0,0))
                buttons = {"cant_buy_alert" : button((255,50,0,0), 760, 480, 400, 60, self._w, self._h,'Ressource insuffisante', font='comicsans', sizeFont=50)}
                buttons["cant_buy_alert"].draw_button(surface)
        elif alert == "GetRideOfThisShit":
            self._shop_input.clear_text()
            buttons = self._temp_buttons
            self._temp_buttons = None
            alert = None 

        elif alert == "confirm_purchase":
            black_surface = pygame.Surface((1920,1080), 255)
            black_surface.set_alpha(100)
            surface.blit(black_surface, (0,0))
            display_surface = pygame.Surface((400, 80))
            font = pygame.font.SysFont('comicsans', 50)
            msg = font.render("Achat effectué !", 1, (0,0,0))
            display_surface.fill(pygame.Color('White'))
            display_surface.blit(msg, (65,25))
                
            surface.blit(display_surface, (760, 480)) 

            buttons = {"purchase_confirmation" : button((255,180,255), 860, 615, 200, 80, self._w, self._h, 'Continuer', font='comicsans', sizeFont=35)}
            buttons["purchase_confirmation"].draw_button(surface)
       
        return surface, self._shop_input.get_text(), buttons, first_call, alert, scroll_y

    def scroll(self, surface, events, y):
        buttons = surface['buttons']
        surface = surface['surface']
        
        pixels = 40
        for event in events:
            if event.type == MOUSEBUTTONDOWN and event.button == 5: # vers le haut
                y -= pixels
                if y <= 0 and y > -(surface.get_height() - 830):
                    buttons = self.new_button_pos(buttons, pixels, "-")
                else:
                    y += pixels
            if event.type == MOUSEBUTTONDOWN and event.button == 4: # vers le bas
                y += pixels
                if y <= 0:
                    buttons = self.new_button_pos(buttons, pixels, "+")
                else:
                    y -= pixels


        return surface, buttons, y

    def new_button_pos(self, buttons, pixels, axe):
        for i in range (0, len(buttons)):
            if axe == "+":
                buttons[i]._y += pixels
            elif axe == "-":
                buttons[i]._y -= pixels
            
        return buttons

    def text_rendering(self, font, sizeFont, text):
        font = pygame.font.SysFont(font, sizeFont)
        text = font.render(text, 1, (0,0,0))
        return text

