from Bee import bee
from Worker_Bee import worker_bee

class hive():

	#init de la ruche
	def __init__(self, level = 0, exp = 0, honey = 31, honey_prod = 10, pollen = 0,bees = [], upgrades = []):

		self._level = level
		self._exp = exp
		self._honey = honey
		self._honey_prod = honey_prod
		self._pollen = pollen
		self._bees = bees
		self._upgrades = upgrades

	# permet d'ajouter au miel la production/s
	def honey_gain(self):
		
		self._honey += self._honey_prod
		print(self._honey)
		return self._honey

	def honey(self):
		return self._honey

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
	def honey_loose(self, amount):
		self._honey -= amount