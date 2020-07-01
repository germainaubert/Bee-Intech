import sqlite3
from Bee import bee
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

    def init_hive():
        conn = self._conn
        cur = conn.cursor()
        cur.execute("UPDATE ruche SET Experience = 0, Niveau = 0, Verification = 1 WHERE id = 1")
        conn.commit()

        cur.execute("DELETE from abeilles")
        conn.commit()
            
        cur.execute("UPDATE ressources SET Quantite = ?, Production = ? WHERE nom = 'honey'")
        conn.commit()
        cur.execute("UPDATE ressources SET Quantite = ?, Production = ? WHERE nom = 'water'")
        conn.commit()
        cur.execute("UPDATE ressources SET Quantite = ?, Production = ? WHERE nom = 'metal'")
        conn.commit()
        cur.execute("UPDATE ressources SET Quantite = ?, Production = ? WHERE nom = 'uranium'")
        conn.commit()
        cur.execute("UPDATE ressources SET Quantite = ?, Production = ? WHERE nom = 'pollen'")
        conn.commit()

        cur.execute("UPDATE territoires SET Possession = 0")
        conn.commit()
        
        cur.execute("UPDATE amelioration SET Possession = 0")
        conn.commit()

        
    def check_first_time(self):
        conn = self._conn
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM ruche")
        row = cur.fetchall()
        print(row)
        check = row[0][3]
        if check == 0:
            check = True
        else:
            check = False
        return check

    def load_data(self):

        conn = self._conn
        cur = conn.cursor()
        
        cur.execute("SELECT Experience, Niveau FROM ruche")
        rows = cur.fetchall()
        print("sel :")
        print(len(rows))
        if len(rows) == 0:
            return None
        else:
            for row in rows:
                print('fesses')
                self._exp = row[0]
                self._level = row[1]

            cur.execute("SELECT Nom, Cout, Categorie, Prix, Ressource_Prix, Niveau_Requis, Sprite, Production, Ressource, territoire_nom FROM abeilles")
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
                territorygrospddetesmorts = row[9]
                self._bees.append(worker_bee(name, cost, category, [ressource_price,price], required_level, sprite, prod, ressource, territorygrospddetesmorts))

        
            cur.execute("SELECT Quantite, Production FROM ressources WHERE ruche_id = 1")
            rows = cur.fetchall()
            for row in rows:
                self._ressource.append(row[0])
                self._prod.append(row[1])
            self._ressource = tuple(self._ressource)
            self._prod = tuple(self._prod)

            cur.execute("SELECT Nom, Niveau, Niveau_Requis, Cout, Ressource_Prix, Categorie, Possession, x, y FROM amelioration WHERE ruche_id = 1")
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
                x = row[7]
                y = row [8]
                if possession == 0:
                    possession = False
                else:
                    possession = True
                print(possession)
                self._upgrades.append(upgrade(name, lvl, required_level, [ressource_price,price], category, possession, (x,y),"chong","./Images/bak.jpg"))
                print(self._upgrades)
            cur.execute("SELECT Nom, Niveau_Requis, Numero, Ressource, Espace, Possession, Nom_Affichage, Description, Force FROM territoires")
            rows = cur.fetchall()
            print("territoires :")
            for row in rows:
                #name = None, lvl_require = 0 , number = 0, ressource = None, space = 0, bees = [], strength = 10, possession = False, display_name = '', description = ''
                list_bee = []
                print(row)
                name = row[0]
                lvl = row[1]
                numero = row[2]
                ressource = row[3]
                space = row[4]
                possession = row[5]
                display_name = row[6]
                description = row[7]
                force = row[8]
                if possession == 0:
                    possession = False
                else:
                    possession = True
                for bee in self._bees:
                    if bee.category() == "worker":
                        if bee._territory == name:
                            list_bee.append(bee)
                self._territories.append(territory(name, lvl, numero, ressource, space, list_bee, 10, possession, display_name, description, force))

            return self._level, self._exp, self._ressource, self._prod, self._bees, self._upgrades, self._territories
        
    def save_data(self, hive):
        print("sa mère")
        conn = self._conn
        cur = conn.cursor()
        cur.execute("UPDATE ruche SET Experience = ?, Niveau = ?, Verification = 1 WHERE id = 1", (hive.exp(), hive.level()))
        conn.commit()

        cur.execute("DELETE from abeilles")
        conn.commit()
        for bee in hive.bees():
            if bee.category() == 'worker':
                name = bee.name()
                cost = bee.cost()
                category = bee.category()
                price = bee.price()
                required_level = bee.required_level()
                sprite = bee.sprite()
                prod = bee.prod()
                ressource = bee.ressource()
                ruche_id = 1
                territory_name = bee.territory()
                cur.execute("INSERT INTO abeilles(Nom, Cout, Categorie, Prix, Ressource_Prix, Niveau_Requis, Sprite, Production, Ressource, ruche_id, territoire_nom) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(name, cost, category, price[1], price[0],required_level, sprite, prod, ressource, ruche_id,territory_name))
                conn.commit()
        hive_prod = hive.prod()
        hive_quantity = hive.ressource()
            
        cur.execute("UPDATE ressources SET Quantite = ?, Production = ? WHERE nom = 'honey'", (hive_quantity["honey"], hive_prod["honey"]))
        conn.commit()
        cur.execute("UPDATE ressources SET Quantite = ?, Production = ? WHERE nom = 'water'", (hive_quantity["water"], hive_prod["water"]))
        conn.commit()
        cur.execute("UPDATE ressources SET Quantite = ?, Production = ? WHERE nom = 'metal'", (hive_quantity["metal"], hive_prod["metal"]))
        conn.commit()
        cur.execute("UPDATE ressources SET Quantite = ?, Production = ? WHERE nom = 'uranium'", (hive_quantity["uranium"], hive_prod["uranium"]))
        conn.commit()
        cur.execute("UPDATE ressources SET Quantite = ?, Production = ? WHERE nom = 'pollen'", (hive_quantity["pollen"], hive_prod["pollen"]))
        conn.commit()

        for ter in hive.territories():
            if ter.possession() == False:
                ter_possess = 0
            else:
                ter_possess = 1
            cur.execute("UPDATE territoires SET Possession = ? WHERE Nom = ?", (ter_possess, ter.name()))
            conn.commit()
            print(ter.name())

        for up in hive.upgrades():
            #print up.possession
            if up.possession() == False:
                up_possess = 0
            else:
                up_possess = 1
            print(up_possess)
            cur.execute("UPDATE amelioration SET Possession = ? WHERE Nom = ?", (up_possess, up.name()))
            conn.commit()
            print(up.name())