from Hive import hive
from Worker_Bee import worker_bee
from Fighter_Bee import fighter_bee
import copy

class shop():

	# Créer le shop
	def __init__(self):

		# liste des abeilles dans le shop
		self._bees = [worker_bee('Abeille basique', 5, 'worker', [10,"honey"], 1, "./Images/bees/basic_bee.png", 15, "honey", None),
		fighter_bee('Combattante basique', 10, 'fighter', [10,"honey"], 1, "./Images/bees/punch.png",  10),
		fighter_bee('Epéiste', 20, 'fighter', [10,"honey"], 1, "./Images/bees/sword.png",  30),
		worker_bee('Aquabeille', 20, 'worker', [10,"water"], 1, "./Images/bees/water.png",  40 , "water", None),
		]
#fighter_bee('fighter', 20, 'fighter', [20,"honey"], 1, "./Images/diobrando.jpg", 20)
		# liste des upgrades dans le shop
		upgrades = []

		self.bee_name = None # Sert à garder en mémoire le nom de l'abeille dont on a besoin, pour final_purchase

	def bee(self,i):
		return self._bees[i]

	def bees(self):
		return self._bees
	
	# Test initial pour l'achat d'AU MOINS UNE ABEILLE
	def test_purchase(self, hive, bee):
		if bee.price()[0] <= hive.ressource()[bee.price()[1]]:
			return "Buy", True
		else:
			return "CantBuy", True

	def test_bee(self, button_id, hive): # Pour chopper la bonne abeille suite à click du bouton
		for bee in self._bees:
			if button_id == bee._name:
				self.bee_name = bee._name 
				return self.test_purchase(hive, bee)

	# L'ultime test pour l'achat d'une abeille, prend en compte le nombre d'abeille souhaités
	# Retourne None si l'achat est ok, retourne nope si l'achat n'est pas possible, 
	# on affecte à self._alert (dans window) cette valeur qui nous permet de faire pop une alerte
	def final_purchase(self, hive, bee_quantity): 
		for bee in self._bees:
			if self.bee_name == bee._name:
				if bee.price()[0] * bee_quantity <= hive.ressource()[bee.price()[1]]:
					for i in range(bee_quantity): # On procède à l'achat d'une abeille * l'input du poto
						hive.add_bee(copy.deepcopy(bee))
						hive.check_territories()
						hive.calcul_prod()
						hive.ressource_loose(bee.price()[1], bee.price()[0])
					
					return None
				else:
					return "nope" # achat pas possible, pas assez de ressource
