import sqlite3
from Bee import bee
from Hive import hive
from Worker_Bee import worker_bee

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

    def hive_save(self, bees):
        print(tasks)
        conn = self._conn
        cur = conn.cursor()
        #del_sql = "DELETE from abeilles where id = 1"
        #cur.execute(del_sql)
        # conn.commit()
        add_sql = "INSERT INTO  abeilles(id,Nom,Cout,Categorie,Prix,Ressource_Prix,Niveau_Requis,Sprite) VALUES (?,?,?,?,?,?,?,?)"
        cur.execute(add_sql,bees)
        conn.commit()
    
        
    def load_data(self):

        conn = self._conn
        cur = conn.cursor()
        cur.execute("SELECT Nom, Cout, Categorie, Prix, Ressource_Prix, Niveau_Requis, Sprite, Production, Ressource FROM abeilles")
        rows = cur.fetchall()
        for row in rows:
            name = row[0]
            cost = row[1]
            category = row[2]
            price = row[3]
            ressource_price = row[4]
            required_level = row[5]
            sprite = row[6]
            prod = row[7]
            ressource = row[8]
            self._bees.append(worker_bee(name, cost, category, None, [ressource_price,price], required_level, sprite, prod, ressource))
        
        return self._bees
        