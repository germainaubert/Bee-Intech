import sqlite3
from Bee import bee
from Hive import hive
from Worker_Bee import worker_bee
from Upgrade import upgrade
from Territory import territory

class database():
    def __init__(self, level = 0, exp = 0, ressource = [],  prod = [], bees = [], upgrades = [], territories = []):
        self._conn = sqlite3.connect('./bdd/ruche.db')
        self._bees = bees
        self._level = level
        self._exp = exp
        self._upgrades = upgrades
        self._ressource = ressource
        self._territories = territories
        self._prod = prod
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
            print(row)
            name = row[0]
            cost = row[1]
            category = row[2]
            price = row[3]
            ressource_price = row[4]
            required_level = row[5]
            sprite = row[6]
            prod = row[7]
            ressource = row[8]
            self._bees.append(worker_bee(name, cost, category, [ressource_price,price], required_level, sprite, prod, ressource))

        cur.execute("SELECT Experience, Niveau FROM ruche")
        rows = cur.fetchall()
        for row in rows:
            print('fesses')
            self._exp = row[0]
            self._level = row[1]
        
        cur.execute("SELECT Quantite, Production FROM ressources WHERE ruche_id = 1")
        rows = cur.fetchall()
        for row in rows:
            self._ressource.append(row[0])
            self._prod.append(row[1])
        self._ressource = tuple(self._ressource)
        self._prod = tuple(self._prod)

        cur.execute("SELECT Nom, Niveau, Niveau_Requis, Cout, Ressource_Prix, Categorie, Possession FROM amelioration WHERE ruche_id = 1")
        rows = cur.fetchall()
        print("upgrades :")
        for row in rows:
            print(row)
            name = row[0]
            lvl = row[1]
            required_level = row[2]
            price = row[3]
            ressource_price = row[4]
            category = row[5]
            possession = row[6]
            if possession == 0:
                possession = False
            else:
                possession = True
            self._upgrades.append(upgrade(name, lvl, required_level, price, category, possession, (0,0)))

        cur.execute("SELECT Nom, Niveau_Requis, Numero, Ressource, Espace, Possession FROM territoires")
        rows = cur.fetchall()
        print("territoires :")
        for row in rows:
            print(row)
            name = row[0]
            lvl = row[1]
            numero = row[2]
            ressource = row[3]
            space = row[4]
            possession = row[5]
            if possession == 0:
                possession = False
            else:
                possession = True
        self._territories.append(territory(name, lvl, numero, ressource, space, bees = [], possession = possession))

        return self._level, self._exp, self._ressource, self._prod, self._bees, self._upgrades, self._territories
        