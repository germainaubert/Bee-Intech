from Bee import bee
from Worker_Bee import worker_bee
from Territory import territory
from Upgrade import upgrade

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

	# permet d'ajouter au miel la production/s
	def bees(self):
		return self._bees
	
	def upgrades(self):
		return self._upgrades
	
	def territories(self):
		return self._territories

	def prod(self):
		return self._prod

	def ressource(self):
		return self._ressource
		
	def ressource_gain(self, ressource, tick):
		self._ressource[ressource] += self._prod[ressource] / tick

	# def ressource
	def ressource(self):
		return self._ressource

	def level(self):
		return self._level

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

	def calcul_territory_space(self):

		space = {"honey" : [0,0], "water" : [0,0], "metal" : [0,0],"uranium" : [0,0],"pollen" : [0,0]}

		for territory in self.territories():
			if territory.possession():
				space[territory.ressource()][1] += territory.space()
		for bee in self.bees():
			if bee.category() == "worker":
				space[bee.ressource()][0] += 1

		return space


	def calcul_prod(self):

		self._prod = {"honey" : 0, "water" : 0, "metal" : 0 ,"uranium" : 0,"pollen" : 0}
		for bee in self.bees():
			if bee.category() == "worker":
				#print(bee.territory())
				if bee.territory() != None:
					#print(f" {self._prod[bee.ressource()]} + {bee.prod()} - {bee.cost()}")
					self._prod[bee.ressource()] = self._prod[bee.ressource()] + bee.prod() - bee.cost()
				else:
					self._prod[bee.ressource()] = self._prod[bee.ressource()] - bee.cost()
			if bee.category() == "fighter":
				self._prod[bee.price()[1]] = self._prod[bee.price()[1]] - bee.cost()

		self.track_bees()
		self.calcul_upgrades()
		print(self._prod)

	def calcul_upgrades(self):

		upgrades = {
		"honey" : "Pluie de miel",
		"water" : "Amphibien",
		"metal" : "Forgeron" ,
		"uranium" : "Radioactif"
		}

		for key in upgrades:
			upgrade = self.max_lvl_upgrade(upgrades[key])
			print(f"result: {upgrade}")
			if upgrade != None:
				if upgrade.lvl() == 1:
					self._prod[key]= self._prod[key]*1.1
				elif upgrade.lvl() == 2:
					self._prod[key]= self._prod[key]*1.2					
				elif upgrade.lvl() == 3:
					self._prod[key]= self._prod[key]*1.3

	def calcul_upgrade_fight(self,bee):
		
		upgrades = {
		"Combattante basique" : "Combattant",
		"Epéiste" : "Epéiste"
		#"" : "",
		#"" : "" ,
		#"" : ""
		}

		for key in upgrades:
			if key == bee.name():
				upgrade = self.max_lvl_upgrade(upgrades[key])
				print(f"result: {upgrade}")
				if upgrade != None:
					if upgrade.lvl() == 1:
						return 1.1
					elif upgrade.lvl() == 2:
						return 1.2					
					elif upgrade.lvl() == 3:
						return 1.3
				else:
					return 1


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

	def exp(self):
		return self._exp


	def check_level_upfrade(self,upgrade):
		if self._level < upgrade.required_level():
			return False
		else:
			return True

	def check_purchase_upgrade(self,upgrade):
		if self._ressource[upgrade.price()[0]] < upgrade.price()[1]:
			return False
		else:
			return True

	def buy_upgrade(self,upgrade):
		self._ressource[upgrade.price()[0]] -= upgrade.price()[1]

	def max_lvl_upgrade(self,name):
		result = None
		for upgrade in self._upgrades:
			if upgrade.name() == name:
				if upgrade.possession() == True:
					if result == None:
						result = upgrade
					else:
						if result.lvl() < upgrade.lvl():
							result = upgrade
		return result

	def get_territory(self, given_territory):
		for territory in self._territories:
			if territory._name == given_territory:
				territory._possession = True
				break