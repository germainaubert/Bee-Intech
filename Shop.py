from Hive import hive
from Worker_Bee import worker_bee

class shop():

	# Créer le shop
	def __init__(self):

		# liste des abeilles dans le shop
		self._bees = [worker_bee('hervé2', 'Ah il est cher sa mère', 'worker', 'Le roi, jean jass et caballero', [10,"honey"], '140', "./Images/bak.jpg", 15, "honey"),
		worker_bee('hervé3', 'Ah il est cher sa mère', 'worker', 'Le roi, jean jass et caballero', [1000,"honey"], '140', "./Images/merveille.jpg",  10 , "honey")]
		# liste des upgrades dans le shop
		upgrades = []

	def bee(self,i):
		return self._bees[i]

	def bees(self):
		return self._bees
	# Methode d'achat d'un abeille 
	def buy_bee(self, hive, bee):

		# Fonctionne uniquement si on a assez de miel pour acheter l'abeille sinon retourne False
		# Ajoute l'abeille a la ruche et soustrait le cout de l'abeille du total de miel
		if bee.price()[0] <= hive.ressource()[bee.price()[1]]:
			hive.add_bee(bee)
			hive.ressource_loose(bee.price()[1], bee.price()[0])
			hive.increase_prod(bee)
			#print(hive.bees())
			return "Buy", True
		else:
			
			return "CantBuy", True

		