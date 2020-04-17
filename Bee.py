
class bee():

	# init une abeille
	def __init__(self, cost = 0, category = None, upgrade = []):

		self._cost = cost
		self._category = category
		self._upgrade = upgrade

	# retourne la categorie de l'abeille
	def category(self):
		return self._category