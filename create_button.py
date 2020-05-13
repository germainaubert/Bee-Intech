import pygame

class button():

	#Prend en argument la couleur, la position x, y, la taille hauteur, largeur, le texte, la police et la taille de la police
	def __init__(self, color, x, y, width, height, screen_w, screen_h, text = '', font = 'comicsans', sizeFont = 50, get = None):
		
		self._x = x
		self._y = y
		self._color = color
		self._width = width
		self._height = height
		self._text = text
		self._font = font
		self._sizeFont = sizeFont
		# Les attributs suivants correspondent à la résolution réelle de l'écran, sert à la méthode get_real_pos
		self._screen_w = screen_w
		self._screen_h = screen_h
		self._get = get

	#Prend en argument la fenetre et si oui ou non le boutton a une bordure
	def draw_button(self, surface, outline = None):

		#Créer la bordure
		if outline:
			pygame.draw.rect(surface, outline, (self._x-2, self._y-2, self._width + 4, self._height + 4), 0)

		# Créer la bordure
		pygame.draw.rect(surface, self._color, (self._x-2, self._y-2, self._width + 4, self._height + 4), 0)

		# choisi la police du texte et le centre au milieur du boutton
		if self._text != '':
			font = pygame.font.SysFont(self._font, self._sizeFont)
			text = font.render(self._text, 1, (0,0,0))
			surface.blit(text, (self._x + (self._width/2 - text.get_width()/2), self._y + (self._height/2 - text.get_height()/2)))

		 # Change la taille des attributs du bouton pour s'adapter à l'affichage
		self.get_real_pos()
	#Permet de savoir si l'utilisateur a le curseur sur le bouton
	#Retourne True si oui sinon retourne False
	def is_over(self,pos):
		
		if pos[0] > self._x and pos[0] < self._x + self._width:
			if pos[1] > self._y and pos[1] < self._y + self._height:
				return True

		return False

	def get_real_pos(self):
    	# Calcule le rapport entre la résolution dont le jeu est crée (1920*1080) avec la résolution réelle de l'écran

		self._rap_w = self._screen_w / 1920 # rapport de la largeur / hauteur
		self._rap_h = self._screen_h / 1080
		
		self._width *= self._rap_w
		self._height *= self._rap_h
		
		self._x *= self._rap_w
		self._y *= self._rap_h
		
	def get(self):
		return self._get
		
		
