import pygame
from create_button import button
class display():
    def init(self):
        button_list = []
    
    def display_menu(self):
        self._background = pygame.image.load('./Images/fond.jpg')
        self._window.blit(self._background, (0, 0))
        self._quit_button = button((212,180,0), 1720, 985, 180, 75, 'Quitter', sizeFont=50)
        self._quit_button.draw_button(self._window)