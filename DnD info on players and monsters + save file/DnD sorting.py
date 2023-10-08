import json
import customtkinter as ctk

root = ctk.CTk()
root.title("DnD Info Storer and Acessor")
root.geometry("550x630")

players = {}
monsters = {}

def add_player():
    name = new_player_name.get()
    initiative = int(new_player_initiative.get())
    piece = new_player_initiative.get()
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


# 'first_line' now contains the content of the first line from the file
summaryFormat1 = ctk.CTkLabel(root, text="Player           Initiative          Piece\n--------------- ----------- ----------------")
summaryFormat1.place(x=250, y=10)
summaryFormat2 = ctk.CTkLabel(root, text="Monster          Initiative            Piece               Health\n--------------- ----------- ---------------- ---------")
summaryFormat2.place(x=220, y=300)

with open("savefile.txt", "r") as json_file:
    # Load the players and monsters dictionaries from the JSON data
    players = json.loads(json_file.readline().strip())
    monsters = json.loads(json_file.readline().strip())

def update_summary():
    dx = 280
    dy = 20
    for name in players:
        dy += 20
        initiative = players[name][0]
        piece = players[name][1]
        label = ctk.CTkLabel(root, text=f'{name:15} {initiative:11} {piece:>16}')
        label.place(x=dx, y=dy)
    dy = 310
    dx = 250
    for name in monsters:
        dy += 20
        initiative = monsters[name][0]
        piece = monsters[name][1]
        health = monsters[name][2]
        label = ctk.CTkLabel(root, text=f'{name:15} {initiative:11} {piece:>16} {health:15}')
        label.place(x=dx, y=dy)

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

reloadSummary = ctk.CTkButton(root, text="Relod Summary", command=update_summary)
reloadSummary.pack()





new_player_namelbl = ctk.CTkLabel(root, text="Enter Player Name", font=('Arial', 14))
new_player_namelbl.place(x=8, y=4)

new_player_name = ctk.CTkEntry(root, width=100, font=('Airal', 14))
new_player_name.place(x=8, y=32)

new_player_initiativelbl = ctk.CTkLabel(root, text="Enter Player Initiative", font=('Arial', 14))
new_player_initiativelbl.place(x=8, y=74)

new_player_initiative = ctk.CTkEntry(root, width=100, font=('Airal', 14))
new_player_initiative.place(x=8, y=102)

new_player_piecelbl = ctk.CTkLabel(root, text="Enter Player Piece", font=('Arial', 14))
new_player_piecelbl.place(x=8, y=144)

new_player_piece = ctk.CTkEntry(root, width=100, font=('Airal', 14))
new_player_piece.place(x=8, y=172)

new_player = ctk.CTkButton(root, text="Add New Player", command=add_player, width=100, font=('Airal', 15))
new_player.place(x=8, y=222)








new_monster_namelbl = ctk.CTkLabel(root, text="Enter Monster Name", font=('Arial', 14))
new_monster_namelbl.place(x=8, y=294)

new_player_name = ctk.CTkEntry(root, width=100, font=('Airal', 14))
new_player_name.place(x=8, y=322)

new_monster_initiativelbl = ctk.CTkLabel(root, text="Enter Monster Initiative", font=('Arial', 14))
new_monster_initiativelbl.place(x=8, y=364)

new_monster_initiative = ctk.CTkEntry(root, width=100, font=('Airal', 14))
new_monster_initiative.place(x=8, y=392)

new_monster_piecelbl = ctk.CTkLabel(root, text="Enter Monster Piece", font=('Arial', 14))
new_monster_piecelbl.place(x=8, y=434)

new_monster_piece = ctk.CTkEntry(root, width=100, font=('Airal', 14))
new_monster_piece.place(x=8, y=462)

new_monster_healthlbl = ctk.CTkLabel(root, text="Enter Monster Health", font=('Arial', 14))
new_monster_healthlbl.place(x=8, y=504)

new_monster_health = ctk.CTkEntry(root, width=100, font=('Airal', 14))
new_monster_health.place(x=8, y=532)

new_monster = ctk.CTkButton(root, text="Add New Monster", command=add_player, width=100, font=('Airal', 15))
new_monster.place(x=8, y=574)

update_summary()

root.mainloop()
