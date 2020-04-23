import pygame

class live_display():
    nbr = 1

    def give_display(self, live, surface): # permet d'appeler la méthode de live_display correspondant à l'affichage en cours, grâce à live
        if live == "new_game":
            surface = self.live_new_game(surface)

        return surface

    def live_new_game(self, surface):
        texte = self.text_rendering("comicsans", 50, str(self.nbr))
        surface.blit(texte, (20,20))
        
        self.nbr += 1
        return surface

    def text_rendering(self, font, sizeFont, text):
        font = pygame.font.SysFont(font, sizeFont)
        text = font.render(text, 1, (0,0,0))
        return text

