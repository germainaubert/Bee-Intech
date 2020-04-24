import pygame
import math

class live_display():

    def give_display(self, live, surface, hive): # permet d'appeler la méthode de live_display correspondant à l'affichage en cours, grâce à live
        if live == "new_game":
            surface = self.live_new_game(surface, hive)

        return surface

    def live_new_game(self, surface, hive):
        hive.honey_gain()
        texte = "Miel: " + str(math.ceil(hive.honey()))
        texte = self.text_rendering("comicsans", 100, texte)
        surface.blit(texte, (0,0))

        return surface

    def text_rendering(self, font, sizeFont, text):
        font = pygame.font.SysFont(font, sizeFont)
        text = font.render(text, 1, (0,0,0))
        return text

