import json

players = {}
monsters = {}

def add_player(name, initiative, piece):
    if name in players:
        raise ValueError("Player exists")
    players[name] = [initiative, piece]

def delete_player(name):
    if name not in players:
        raise ValueError("Player doesn't exist")


def add_monster(name, initiative, piece, health):
    if name in monsters:
        raise ValueError("Monster exists")
    monsters[name] = [initiative, piece, health]

def delete_monster(name):
    if name not in monsters:
        raise ValueError("Monster doesn't exist")


def change_monster_health(name, new_amount):
    if name not in monsters:
        raise ValueError("Monster does not exist")
    old_amount = monsters[name][2]
    if new_amount > old_amount:
        raise ValueError("Monster killed, please get rid of monster")
    monsters[name][2] = new_amount

def saveAndExit():
    global players, monsters
    with open("savefile.txt", "w") as fp:
        json.dump(players, fp)  # encode dict into JSON
        fp.write("\n")
        json.dump(monsters, fp)  # encode dict into JSON
    quit()

def load():
    global players, monsters
    with open("savefile.txt", "r") as json_file:
        # Load the players and monsters dictionaries from the JSON data
        players = json.loads(json_file.readline().strip())
        monsters = json.loads(json_file.readline().strip())


# 'first_line' now contains the content of the first line from the file

def print_summary():
    print("Player           Initiative            Piece")
    print("--------------- ----------- ----------------")
    for name in players:
        initiative = players[name][0]
        piece = players[name][1]
        print(f'{name:15} {initiative:11} {piece:>16}')
    print("Monster          Initiative            Piece  Health")
    print("--------------- ----------- ---------------- -------")
    for name in monsters:
        initiative = monsters[name][0]
        piece = monsters[name][1]
        health = monsters[name][2]
        print(f'{name:15} {initiative:11} {piece:>16} {health:15}')