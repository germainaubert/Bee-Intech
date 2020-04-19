import pygame
from Create_button import button

class display():
    def init(self):
        button_list = []
    
    def display_menu(self, w, h):

        surface = pygame.Surface((1920,1080))
        background = pygame.image.load('./Images/fond.jpg')
        surface.blit(background, (0, 0))

        self._quit_button = button((212,180,0), 1720, 985, 180, 75, w, h,'Quitter', font='comicsans', sizeFont=50)
        self._quit_button.draw_button(surface)
        
        return surface