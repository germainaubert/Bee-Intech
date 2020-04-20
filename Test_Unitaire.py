from Hive import hive
from Bee import bee
from Worker_Bee import worker_bee 

def test_Bee_init():
	bee1 = worker_bee("bee",15,"chong",["a"],188,["chong"])
	print(f"bee 1 categorie: {bee1._category} prod: {bee1._prod}")
	
	bee2 = worker_bee()
	print(f"bee 2 categorie: {bee2._category} prod: {bee2._prod}")

	bee3 = bee("bee",15,"chong",["a"])
	print(f"bee 3 categorie: {bee3._category}")

	bee4 = bee()
	print(f"bee 4 categorie: {bee4._category}")

def test_hive():

	# créer une ruche et vérifie qu'elle est bien créer avec les paramètres
	hive1 = hive(honey_prod = 15, honey = 125)
	print(f"la ruche 1 a pour  poduction de miel: {hive1._honey_prod} miel: {hive1._honey}")

	# créer une ruche, y ajoute une abeille et calcule sa production
	hive2 =  hive()
	bee1 = worker_bee("bee",15,"worker",["a"],37,["chong"])
	hive2.add_bee(bee1)
	print(f"la ruche 2 produit {hive2.calcul_prod()} miel")
	
	# ajoute une deuxième abeille et calcul a nouveau sa production
	bee2 = worker_bee("bee",20,"worker",["a"],130,["chong"])
	hive2.add_bee(bee2)
	print(f"la ruche 2 produit {hive2.calcul_prod()} miel")

	# ajoute une troisième abeille et calcul a nouveau sa production
	bee3 = worker_bee("bee",1000,"worker",["a"],130,["chong"])
	hive2.add_bee(bee3)
	print(f"la ruche 2 produit {hive2.calcul_prod()} miel")

#test_Bee_init()
test_hive()
