import pygame

class button():

	#Prend en argument la couleur, la position x, y, la taille hauteur, largeur et le text
	def __init__(self, color, x, y, width, height, text = ''):
		
		self._x = x
		self._y = y
		self._color = color
		self._width = width
		self._height = height
		self._text = text

	#Prend en argument la fenetre et si oui ou non le boutton a une bordure
	def draw_button(self, window, outline = None):

		#Créer la bordure
		if outline:
			pygame.draw.rect(window, outline, (self._x-2, self._y-2, self._width + 4, self._height + 4), 0)

		# Créer la bordure
		pygame.draw.rect(window, self._color, (self._x-2, self._y-2, self._width + 4, self._height + 4), 0)

		# choisi la police du texte et le centre au milieur du boutton
		if self._text != '':
			font = pygame.font.SysFont('comicsans',60)
			text = font.render(self._text, 1, (0,0,0))
			window.blit(text, (self._x + (self._width/2 - text.get_width()/2), self._y + (self._height/2 - text.get_height()/2)))

	#Permet de savoir si l'utilisateur a le curseur sur le bouton
	#Retourne True si oui sinon retourne False
	def is_over(self,pos):
		if pos[0] >self._x and pos[0] < self._x + self._width:
			if pos[1] > self._y and pos[1] < self._y + self._height:
				return True

		return False
