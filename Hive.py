from Bee import bee
from Worker_Bee import worker_bee
from Territory import territory

class hive():

	#init de la ruche
	def __init__(self, level = 0, exp = 0, ressource = (0,0,0,0,0), prod = (0,0,0,0,0), bees = [], upgrades = [], territories = []):

		self._level = level
		self._exp = exp
		self._ressource = {"honey" : ressource[0], "water" : ressource[1], "metal" : ressource[2] ,"uranium" : ressource[3] ,"pollen" : ressource[4]}
		self._prod = {"honey" : prod[0], "water" : prod[1], "metal" : prod[2] ,"uranium" : prod[3] ,"pollen" : prod[4]}
		self._bees = bees
		self._upgrades = upgrades
		self._territories = territories

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
				if bee.category() == "worker":
					if bee.territory() == None:
						self._bees.remove(bee)
						break
					else:
						for territory in self._territories:
							if territory.name() == bee.territory():
								#print("test1")
								for bee_ter in territory.bees():
									if bee_ter.name() == name:
										territory._bees.remove(bee_ter)
										#print(f"nom de territoire: {territory.name()} nombre d'abeilles: {len(territory._bees)} ")
										self._bees.remove(bee)
										self.check_territories()
										self.calcul_prod()
										return bee
				else:
					self._bees.remove(bee)
					break
		self.check_territories()
		self.calcul_prod()
		return bee

	def calcul_prod(self):

		self._prod = {"honey" : 0, "water" : 0, "metal" : 0 ,"uranium" : 0,"pollen" : 0}
		for bee in self.bees():
			if bee.category() == "worker":
				print(bee.territory())
				if bee.territory() != None:
					#print(f" {self._prod[bee.ressource()]} + {bee.prod()} - {bee.cost()}")
					self._prod[bee.ressource()] = self._prod[bee.ressource()] + bee.prod() - bee.cost()
				else:
					self._prod[bee.ressource()] = self._prod[bee.ressource()] - bee.cost()
		self.track_bees()
		print(self._prod)


	def check_territories(self):
		
		for bee in self.bees():
			if bee.category() == "worker":
				if bee.territory() == None:
					for territory in self._territories:
						if territory.possession() == True:
							if territory.ressource() == bee.ressource():
								if len(territory.bees()) != territory.space():
									territory._bees.append(bee)
									bee.change_territory(territory.name())
									break				

	def track_bees(self):
		for bee in self.bees():
			if bee.category() == "worker":
				print(f"nom du territoire: {bee.territory()} - nom de l'abeille: {bee.name()} ")
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