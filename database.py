import sqlite3
from Hive import *

class database():
    def __init__(self, bees = [], upgrades = [], players = [], ressources = [], hive = [], territories = []):
        self._conn = sqlite3.connect('./bdd/ruche.db')
        self._bees = bees
        self._upgrades = upgrades
        self._players = players
        self._ressources = ressources
        self._hive = hive
        self._territories = territories
        self._save_count = 1

    def hive_save_bee(self, tasks):
        print(tasks)
        conn = self._conn
        cur = conn.cursor()

        sql = "INSERT INTO  abeilles(id,Nom,Cout,Categorie,Prix,Ressource_Prix,Niveau_Requis,Sprite) VALUES (?,?,?,?,?,?,?,?)"
        cur.execute(sql,tasks)


        conn.commit()
        
