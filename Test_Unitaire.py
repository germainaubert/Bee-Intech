from Bee import bee
from Worker_Bee import worker_bee 

def Test_Bee():
	bee1 = worker_bee(15,"chong",["a"],188,["chong"])
	print(f"bee 1 categorie: {bee1._category} prod: {bee1._prod}")
	
	bee2 = worker_bee()
	print(f"bee 2 categorie: {bee2._category} prod: {bee2._prod}")

	bee3 = bee(15,"chong",["a"])
	print(f"bee 3 categorie: {bee3._category}")

	bee4 = bee()
	print(f"bee 4 categorie: {bee4._category}")

Test_Bee()