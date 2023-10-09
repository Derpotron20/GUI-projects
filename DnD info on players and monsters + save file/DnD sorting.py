import json
import customtkinter as ctk

root = ctk.CTk()
root.title("DnD Info Storer and Acessor")
root.geometry("750x630")

players = {}
monsters = {}

def add_player():
    global new_player_name, new_player_initiative, new_player_piece
    name = new_player_name.get()
    initiative = new_player_initiative.get()
    piece = new_player_piece.get()
    if name in players or len(name) == 0 or len(initiative) == 0 or len(piece) == 0:
        raise ValueError("Player exists")
    players[name] = [initiative, piece]

def delete_player():
    global dlt_player
    player = dlt_player.get()
    if player not in players or len(player) == 0:
        raise ValueError("Player doesn't exist")
    else:
        del players[player]



def add_monster():
    global new_monster_name, new_monster_initiative, new_monster_piece, new_monster_health
    name = new_monster_name.get()
    initiative = new_monster_initiative.get()
    piece = new_monster_piece.get()
    health = new_monster_health.get()
    if name in monsters or len(name) == 0 or len(initiative) == 0 or len(piece) == 0 or len(health) == 0:
        raise ValueError("Monster exists")
    monsters[name] = [initiative, piece, health]
    print(monsters[name])

def delete_monster():
    global dlt_monster
    monster = dlt_monster.get()
    if monster not in monsters or len(monster) == 0:
        raise ValueError("Monster doesn't exist")
    else:
        del monsters[monster]


def change_monster_health():
    name = change_monster_health_nameent.get()
    new_amount = change_monster_healthent.get()
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


# 'first_line' now contains the content of the first line from the file


with open("savefile.txt", "r") as json_file:
    # Load the players and monsters dictionaries from the JSON data
    players = json.loads(json_file.readline().strip())
    monsters = json.loads(json_file.readline().strip())

def update_summary():

    for widget in root.winfo_children():
        widget.destroy()

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
        label = ctk.CTkLabel(root, text=f'{name:15} {initiative:11} {piece:>18} {health:15}')
        label.place(x=dx, y=dy)
    create_window()


def create_window():
    global new_monster_name, new_monster_initiative, new_monster_piece, new_monster_health,new_player_name, new_player_initiative, new_player_piece, dlt_monster, dlt_player, change_monster_healthent, change_monster_healthent, change_monster_health_nameent
    summaryFormat1 = ctk.CTkLabel(root, text="Player           Initiative          Piece\n--------------- ----------- ----------------")
    summaryFormat1.place(x=250, y=10)
    summaryFormat2 = ctk.CTkLabel(root, text="Monster          Initiative            Piece               Health\n--------------- ----------- ---------------- ---------")
    summaryFormat2.place(x=220, y=300)



    reloadSummary = ctk.CTkButton(root, text="Relod Summary", command=update_summary)
    reloadSummary.place(x=555, y=15)

    delete_player_lbl = ctk.CTkLabel(root, text="Enter Player Name\nfor deletion             ", font=('Arial', 14))
    delete_player_lbl.place(x=565, y=86)

    delete_player_btn = ctk.CTkButton(root, text="Delete Player", font=('Arial', 14), command=delete_player)
    delete_player_btn.place(x=565, y=155)

    dlt_player = ctk.CTkEntry(root, width=120, font=('Arial', 14))
    dlt_player.place(x=565, y=120)



    delete_monster_lbl = ctk.CTkLabel(root, text="Enter Monster Name\nfor deletion           ", font=('Arial', 14))
    delete_monster_lbl.place(x=565, y=206)

    delete_monster_btn = ctk.CTkButton(root, text="Delete Monster", font=('Arial', 14), command=delete_monster)
    delete_monster_btn.place(x=565, y=275)

    dlt_monster = ctk.CTkEntry(root, width=120, font=('Arial', 14))
    dlt_monster.place(x=565, y=240)







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



    save = ctk.CTkButton(root, text="Save", command=saveAndExit, font=('Arial', 14))
    save.place(x=565, y=510)




    new_monster_namelbl = ctk.CTkLabel(root, text="Enter Monster Name", font=('Arial', 14))
    new_monster_namelbl.place(x=8, y=294)

    new_monster_name = ctk.CTkEntry(root, width=100, font=('Airal', 14))
    new_monster_name.place(x=8, y=322)

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

    change_monster_healthlbl = ctk.CTkLabel(root, text="Enter New Monster Health", font=('Arial', 14))
    change_monster_healthlbl.place(x=565, y=320)

    change_monster_healthent = ctk.CTkEntry(root, width=100, font=('Airal', 14))
    change_monster_healthent.place(x=565, y=348)
    
    change_monster_health_namelbl = ctk.CTkLabel(root, text="Enter Monster Name", font=('Arial', 14))
    change_monster_health_namelbl.place(x=565, y=390)

    change_monster_health_nameent = ctk.CTkEntry(root, width=100, font=('Airal', 14))
    change_monster_health_nameent.place(x=565, y=418)
    
    change_monster_healthbtn = ctk.CTkButton(root, text="Change Monster Health", command=change_monster_health, width=100, font=('Airal', 15))
    change_monster_healthbtn.place(x=565, y=450)

    new_monster = ctk.CTkButton(root, text="Add New Monster", command=add_monster, width=100, font=('Airal', 15))
    new_monster.place(x=8, y=574)

create_window()

update_summary()

root.mainloop()
