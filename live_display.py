import pygame
import math
from pygame_textinput import TextInput
from create_button import button
from pygame.locals import *

class live_display():
    tick = 60
    shop_input = TextInput()
    accepted_event1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    accepted_event2 = [K_BACKSPACE, K_DELETE, K_RETURN, K_RIGHT, K_LEFT, K_END, K_HOME, KEYUP]
    temp_buttons = None

    def __init__(self, w, h):
        self._w = w
        self._h = h

    def give_display(self, live, alert, surface, hive, events, buttons, first_call): # permet d'appeler la méthode de live_display correspondant à l'affichage en cours, grâce à live
        if live == "new_game":
            surface = self.live_new_game(surface, hive)
        elif live == "management":
            surface = self.live_management(surface, hive)
        elif live == "shop":
            surface = self.live_shop(surface, hive, events, buttons, alert, first_call)
            #buttons = {}
            #print(self.temp_buttons)
    
        return surface

    def live_new_game(self, surface, hive):
        hive.ressource_gain("honey", self.tick)
        texte = "Miel: " + str(math.ceil(hive._ressource["honey"]))
        texte = self.text_rendering("comicsans", 100, texte)
        surface.blit(texte, (0,0))

        return surface

    def live_management(self, surface, hive):
        hive.ressource_gain("honey", self.tick)
        texte = "Miel: " + str(math.ceil(hive._ressource["honey"]))
        texte = self.text_rendering("comicsans", 100, texte)
        surface.blit(texte, (0,0))

        return surface

    def live_shop(self, surface, hive, events, buttons, alert, first_call):

        hive.ressource_gain("honey", self.tick)
        texte = "Miel: " + str(math.ceil(hive._ressource["honey"]))
        texte = self.text_rendering("comicsans", 100, texte)
        surface.blit(texte, (0,0))
        
        delete = False
        give_event = []      
        for event in events:
            if event.type == KEYDOWN:
                for accepted_tchong in self.accepted_event1:
                    if event.unicode == accepted_tchong:
                        give_event.append(event)
                        #print(event)
                        break
                for accepted_tchang in self.accepted_event2:
                    if event.key == accepted_tchang:
                        give_event.append(event)
                        if event.key == K_BACKSPACE:
                            delete = True
                        #print(event)
                        break

        if alert == "Buy":
            if first_call == True:
                self.temp_buttons = buttons
                first_call = False
                buttons = {}
            elif first_call == False:
                black_surface = pygame.Surface((1920,1080), 255)
                black_surface.set_alpha(100)
                surface.blit(black_surface, (0,0))
                input_surface = pygame.Surface((400, 80))
                input_surface.fill(pygame.Color('White'))
                input_surface.blit(self.shop_input.get_surface(), (100,35))
                
                
                
                if len(self.shop_input.get_text()) < 10:
                    self.shop_input.update(give_event)
                elif delete == True:
                    self.shop_input.update(give_event)

                surface.blit(input_surface, (760, 480)) 

                buttons = {"cancel_buy" : button((255,180,255), 860, 615, 200, 80, self._w, self._h, 'Annuler Achat', font='comicsans', sizeFont=35)}
                buttons["cancel_buy"].draw_button(surface)

        elif alert == "GetRideOfThisShit":
            self.shop_input.clear_text()
            buttons = self.temp_buttons
            self.temp_buttons = None
            alert = None
        
        
            

        elif alert == "CantBuy":
            if first_call == True:
                self.temp_buttons = buttons
                first_call = False
                buttons = {}
            elif first_call == False:
                black_surface = pygame.Surface((1920,1080), 255)
                black_surface.set_alpha(100)
                surface.blit(black_surface, (0,0))
                buttons = {"cant_buy_alert" : button((255,50,0,0), 760, 480, 400, 60, self._w, self._h,'Ressource insuffisante', font='comicsans', sizeFont=50)}
                buttons["cant_buy_alert"].draw_button(surface)
        elif alert == "GetRideOfThisShit":
            buttons = self.temp_buttons
            self.temp_buttons = None
            alert = None

        

        return surface, self.shop_input.get_text(), buttons, first_call, alert



    def text_rendering(self, font, sizeFont, text):
        font = pygame.font.SysFont(font, sizeFont)
        text = font.render(text, 1, (0,0,0))
        return text

