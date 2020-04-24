from Bee import bee
from Worker_Bee import worker_bee

class hive():

	#init de la ruche
	def __init__(self, level = 0, exp = 0, ressource = (0,0,0,0,0), prod = (0,0,0,0,0), bees = [], upgrades = []):

		self._level = level
		self._exp = exp
		self._ressource = {"honey" : ressource[0], "wather" : ressource[1], "metal" : ressource[2] ,"uranium" : ressource[3] ,"pollen" : ressource[4]}
		self._prod = {"honey" : prod[0], "wather" : prod[1], "metal" : prod[2] ,"uranium" : prod[3] ,"pollen" : prod[4]}
		self._bees = bees
		self._upgrades = upgrades

	# permet d'ajouter au miel la production/s
	def bees(self):
		return self._bees

	def ressource_gain(self, ressource, tick):
		
		self._ressource[ressource] += self._prod[ressource] / tick

	def ressource(self):
		return self._ressource

	# ajoute une abeille a la ruche
	def add_bee(self,bee):
		self._bees.append(bee)

	# calcul la production de miel de la ruche
	def calcul_prod(self):
		calcul = 0
		for bee in self._bees:
			if bee.category() == "worker":
				calcul += bee._prod - bee._cost
		return calcul

	# soustrait un montant de miel defini a la ruche
	# utilse pour les achats par exemple
	def ressource_loose(self, ressource, amount):
		self._ressource[ressource] -= amount