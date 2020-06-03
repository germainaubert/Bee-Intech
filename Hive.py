from Bee import bee
from Worker_Bee import worker_bee
from Territory import territory

class hive():

	#init de la ruche
	def __init__(self, level = 1, exp = 0, ressource = (0,0,0,0,0), prod = (0,0,0,0,0), bees = [], upgrades = [], territories = []):

		self._level = level
		self._exp = exp
		self._ressource = {"honey" : ressource[0], "water" : ressource[1], "metal" : ressource[2] ,"uranium" : ressource[3] ,"pollen" : ressource[4]}
		self._prod = {"honey" : prod[0], "water" : prod[1], "metal" : prod[2] ,"uranium" : prod[3] ,"pollen" : prod[4]}
		self._bees = bees
		self._upgrades = upgrades
		self._territories = territories
		print(self.territories_space("honey"))

	# permet d'ajouter au miel la production/s
	def bees(self):
		return self._bees

	def ressource_gain(self, ressource, tick):
		self._ressource[ressource] += self._prod[ressource] / tick

	# def ressource
	def ressource(self):
		return self._ressource

	# ajoute une abeille a la ruche
	def add_bee(self,bee):
		self._bees.append(bee)

	def del_bee(self, name):
		for bee in self._bees:
			if name == bee._name:
				self._bees.remove(bee)
				return bee
		
	# met à jour la production des ressources suite à l'achat d'une abeille
	def increase_prod(self, bees): # bees est destiné à devenir un tableau contenant toutes les abeilles achetées, possibilité dans le futur d'acheter plusieurs abeilles
		if bees.category() == "worker":
			if self.check_territories(bees,"add"):
				self._prod[bees.ressource()] += bees.prod()-bees.cost()
			else:
				self._prod[bees.ressource()] -= bees.cost()
		else:
			self._prod[bees.ressource()] -= bees.cost()
		
		print(self.territories_space(bees.ressource()))
		print(len(self.bees()))
		print(self._prod[bees.ressource()])


	def decrease_prod(self, bees): # meme chose que pour increase_prod
			if bees.category() == "worker":
				if self.check_territories(bees,"suppr"):
					self._prod[bees.ressource()] -= bees.prod() - bees.cost()
				else:
					self._prod[bees.ressource()] += bees.cost()
			else:
				self._prod[bees.ressource()] += bees.cost()

			print(self.territories_space(bees.ressource()))
			print(len(self.bees()))
			print(self._prod[bees.ressource()])


	def check_territories(self,bees,action):
		space = self.territories_space(bees.ressource())
		check_space = 0
		for bee in self.bees():
			if bees.ressource() == bee.ressource():
				check_space += 1

			if action == "add" and check_space > space:
				return False
				break
			elif action == "suppr" and check_space >= space:
				return False
				break

		return True



	# soustrait un montant de miel defini a la ruche
	# utilse pour les achats par exemple
	def ressource_loose(self, ressource, amount):
		self._ressource[ressource] -= amount

	def ressource_click(self, ressource, amount):
		self._ressource[ressource] += amount

	def territories_space(self, ressource):
		space = 0
		for ter in self._territories:
			if ter.defense() == []:
				if ter.ressource() == ressource:
					space += ter.space()
		return space

	def exp(self):
		return self._exp

	def level(self):
		return self._level