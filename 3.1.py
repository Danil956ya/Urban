player_stat = {
    "HP": 100,
    "Armor" : 10,
    "Damage" : 15,
    "PositionX" : 3.145,
    "PositionY" : 4.124
}

with open("PlayerSave.txt", "w") as file:
    for el in player_stat.items():
        file.write(el[0] + ":" + str(el[1]) + "\n")
