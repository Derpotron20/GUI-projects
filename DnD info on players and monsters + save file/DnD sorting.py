import json
import customtkinter as ctk

root = ctk.CTk()
root.title("DnD Info Storer and Acessor")
root.geometry("550x400")

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
summaryFormat1 = ctk.CTkLabel(root, text="Player           Initiative            Piece\n--------------- ----------- ----------------")
summaryFormat1.place(x=250, y=10)
summaryFormat2 = ctk.CTkLabel(root, text="Monster          Initiative            Piece               Health\n--------------- ----------- ---------------- ---------")
summaryFormat2.place(x=220, y=190)
summary = ctk.CTkLabel(root, text="im here")
summary.place(x=220, y=30)

def update_summary():
    global summary
    for name in players:
        initiative = players[name][0]
        piece = players[name][1]
        summary.configure(text=f'{name:15} {initiative:11} {piece:>16}')
    root

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

update_summary()

root.mainloop()