
def who_won(hive, territory, territories): # retourne true si victoire, false si défaite
    print(hive._bees)
    for terr in territories:
        if terr._name == territory:
            territory = terr
            break
    if territory._possession == False:
        bees = hive._bees
        tot_strength = 0
        for bee in bees:
            if bee._category == "fighter":
                tot_strength += bee._strength
        if tot_strength > territory._strength:
            return "good"
        else:
            return "notgood"
    else:
        return "mine"