import random
import tkinter
import functools

root = tkinter.Tk()
root.geometry("250x200")
root.title("cave explorer")
root.rowconfigure(0, {"minsize": 30})
root.columnconfigure(0,{"minsize": 30})
root.rowconfigure(1, {"minsize": 30})
root.columnconfigure(1,{"minsize": 30})
root.rowconfigure(2, {"minsize": 30})
root.columnconfigure(2,{"minsize": 30})
root.rowconfigure(3, {"minsize": 30})
root.rowconfigure(4, {"minsize": 30})
root.rowconfigure(5, {"minsize": 30})
root.rowconfigure(6, {"minsize": 30})

class player:
    def __init__(self, name, hp, inventory):
        self.name = name
        self.hp = hp
        self.inventory = inventory

def loose_fight():
    global winner_text
    global nav_text
    global left_btn
    global right_btn
    global attack_text
    global damage_text
    global next_btn
    attack_text.destroy()
    damage_text.destroy()
    next_btn.destroy()
    monster_hp = 0
    enemy_hp.config(text="Foe's hp: " + str(monster_hp))
    looser_text = tkinter.Label(root, wraplength=250, text="You have been defeted by the " + monster)
    looser_text.grid(row=0, column=0, columnspan=3)
    close_app = tkinter.Button(root, text="close", command=root.quit)
    close_app.grid(row=1, column=1)

def win_fight(monster):
    global winner_text
    global nav_text
    global left_btn
    global right_btn
    global attack_text
    global damage_text
    global next_btn
    attack_text.destroy()
    damage_text.destroy()
    next_btn.destroy()
    monster_hp = 0
    enemy_hp.config(text="Foe's hp: " + str(monster_hp))
    winner_text = tkinter.Label(root, wraplength=250, text="You have defeted the " + monster)
    winner_text.grid(row=0, column=0, columnspan=3)
    nav_text = tkinter.Label(root, wraplength=250, justify=tkinter.CENTER, text="You can just make out 2 tunnels at the edge of the flickering light of your torch. Will you go right or left?")
    nav_text.grid(row=1, column=0, columnspan=3)
    left_btn = tkinter.Button(root, text="Left", command=move_left)
    left_btn.grid(row=2, column=0)
    right_btn = tkinter.Button(root, text="Right", command= move_right)
    right_btn.grid(row=2, column=2)

def monsterAttack(monster):
    global attack_text
    global damage_text
    global next_btn
    global dir_label
    dir_label.destroy()
    attack_text.destroy()
    damage_text.destroy()
    damage = random.randint(0, 5)
    attack_text = tkinter.Label(root, wraplength=250, text="The " + monster + " attacks")
    attack_text.grid(row=0, column=0, columnspan=3)
    damage_text = tkinter.Label(root, wraplength=250, text="It hits for " + str(damage) + " points")
    damage_text.grid(row=1, column=0, columnspan=3)
    hero.hp = hero.hp - damage
    hp_indicator.config(text="HP: " + str(hero.hp))
    action_with_arg = functools.partial(battle, monster)
    if hero.hp <= 0:
        action_with_arg = functools.partial(loose_fight, monster)
    next_btn.config(command=action_with_arg)


def attack(monster):
    global monster_hp
    global combat_text
    global battle_options
    global attack_text
    global damage_text
    global next_btn
    combat_text.destroy()
    battle_options.destroy()
    attack_btn.destroy()
    flee_btn.destroy()
    attack_text = tkinter.Label(root, wraplength=250, text="You swing your dagger at the " + monster)
    attack_text.grid(row=0, column=0, columnspan=3)
    damage = random.randint(0, 5)
    damage_text = tkinter.Label(root, wraplength=250, text="You hit for " + str(damage) + " points")
    damage_text.grid(row=1, column=0, columnspan=3)
    monster_hp = monster_hp - damage
    enemy_hp.config(text="Foe's hp: " + str(monster_hp))
    action_with_arg = functools.partial(monsterAttack, monster)
    if monster_hp <= 0:
        action_with_arg = functools.partial(win_fight, monster)
    next_btn = tkinter.Button(root, text="Next", command= action_with_arg)
    next_btn.grid(row=2, column=1)

def flee(monster):
    global combat_text
    global battle_options
    combat_text.destroy()
    battle_options.destroy()
    attack_btn.destroy()
    flee_btn.destroy()
    fleeing = tkinter.Label(root, wraplength=250, text="You Have fled from the cave in shame")
    fleeing.grid(row=0, column=0, columnspan=3)
    close_app = tkinter.Button(root, text="close", command=root.quit)
    close_app.grid(row=1, column=1)

def battle(monster):
    global monster_hp
    global flee_btn
    global enemy_hp
    global hp_indicator
    global combat_text
    global battle_options
    global attack_btn
    global flee_btn
    global dir_label
    global damage_text
    global attack_text
    dir_label.destroy()
    try:
        next_btn.destroy()
    except (NameError, AttributeError):
        pass
    try:
        damage_text.destroy()
    except (NameError, AttributeError):
        pass
    try:
        attack_text.destroy()
    except (NameError, AttributeError):
        pass
    start_fight.destroy()
    encounter_start.destroy()
    if monster_hp == 0:
        monster_hp = random.randint(10, 20)
    enemy_hp.config(text="Foe's hp: " + str(monster_hp))
    hp_indicator.config(text="HP: " + str(hero.hp))
    combat_text = tkinter.Label(root, text="the monster is looming over you")
    combat_text.grid(row=0, column=0, columnspan=3)
    battle_options = tkinter.Label(root, text ="Do you attack or flee")
    battle_options.grid(row= 1, column=0, columnspan=3)
    attack_btn = tkinter.Button(root, text="attack", command= lambda: attack(monster))
    attack_btn.grid(row=2, column= 2)
    flee_btn = tkinter.Button(root, text="Flee", command= lambda: flee(monster))
    flee_btn.grid(row=2, column=0)

def create_hero():
    global hero
    global greeting
    global player_name
    global intro_label
    global intro_text
    global next_btn
    global enemy_hp
    global hp_indicator
    name = player_name.get()
    hero = player(name, 100, ["dagger"])
    intro_label.destroy()
    name_button.destroy()
    player_name.destroy()
    intro_text = tkinter.Label(root, wraplength=250, justify=tkinter.CENTER, text="Welcome " + hero.name + " you find your self in a cavern.")
    intro_text.grid(row=0, column=0, columnspan=3)
    next_btn = tkinter.Button(root, text="Next", justify=tkinter.CENTER, command= move_loop)
    next_btn.grid(row=1, column=1 )
    hp_indicator = tkinter.Label(root, text="HP: " + str(hero.hp))
    hp_indicator.grid(row=5, column=0)
    name_plate = tkinter.Label(root, text=hero.name)
    name_plate.grid(row=5, column=1)
    enemy_hp = tkinter.Label(root, text="Foe's hp: " + str(monster_hp))
    enemy_hp.grid(row=5, column=2)

def move_left():
    global  left_btn
    global right_btn
    global nav_text
    global dir_label
    global encounter_start
    global start_fight
    global winner_text
    try:
        dir_label.destroy()
    except (NameError, AttributeError):
        pass
    try:
        winner_text.destroy()
    except (NameError, AttributeError):
        pass
    nav_text.destroy()
    left_btn.destroy()
    right_btn.destroy()
    dir_label = tkinter.Label(root, wraplength=250, justify=tkinter.CENTER, text="You go Left")
    dir_label.grid(row=0, column=1)
    encounter = random.randint(0, 2)
    if encounter == 1:
        dir_label.destroy()
        encounter_start = tkinter.Label(root, wraplength=250, text="You see an orc ahead\n It attacks")
        encounter_start.grid(row=1, column=1)
        start_fight = tkinter.Button(root, text="Fight", command=lambda: battle("orc"))
        start_fight.grid(row=2, column=1)
        root.update_idletasks()
    else:
        left_btn = tkinter.Button(root, text="Left", command=move_left)
        left_btn.grid(row=1, column=0)
        right_btn = tkinter.Button(root, text="Right", command=move_right)
        right_btn.grid(row=1, column=2)

def move_right():
    global left_btn
    global right_btn
    global nav_text
    global encounter_start
    global start_fight
    global dir_label
    global winner_text
    try:
        dir_label.destroy()
    except (NameError, AttributeError):
        pass
    try:
        winner_text.destroy()
    except (NameError, AttributeError):
        pass
    nav_text.destroy()
    left_btn.destroy()
    right_btn.destroy()
    dir_label = tkinter.Label(root, wraplength=250, justify=tkinter.CENTER, text="You go Right ")
    dir_label.grid(row=0, column=1)
    encounter = random.randint(0, 2)
    if encounter == 1:
        dir_label.destroy()
        encounter_start = tkinter.Label(root, wraplength=250, text="You see an orc ahead\n It attacks")
        encounter_start.grid(row=1, column=1)
        start_fight = tkinter.Button(root, text="Fight", command=lambda: battle("orc"))
        start_fight.grid(row=2, column=1)
    else:
        left_btn = tkinter.Button(root, text="Left", command=move_left)
        left_btn.grid(row=1, column=0)
        right_btn = tkinter.Button(root, text="Right", command=move_right)
        right_btn.grid(row=1, column=2)

def move_loop():
    global move_dir
    global nav_text
    global left_btn
    global right_btn
    global movement
    global next_btn
    global intro_text
    global hero
    global winner_text
    try:
        winner_text.destroy()
    except (NameError, AttributeError):
        pass
    try:
        nav_text.destroy()
    except (NameError, AttributeError):
        pass
    try:
        right_btn.destroy()
    except (NameError, AttributeError):
        pass
    try:
        left_btn.destroy()
    except (NameError, AttributeError):
        pass
    next_btn.destroy()
    intro_text.destroy()
    if hero.hp > 0:
        nav_text = tkinter.Label(root, wraplength=250, justify=tkinter.CENTER, text="You can just make out 2 tunnels at the edge of the flickering light of your torch. Will you go right or left?")
        nav_text.grid(row=0, column=0, columnspan=3)
        left_btn = tkinter.Button(root, text="Left", command= move_left)
        left_btn.grid(row=1, column=0)
        right_btn = tkinter.Button(root, text="Right", command= move_right)
        right_btn.grid(row=1, column=2)

    else:
        game_over =tkinter.Label(root, wraplength=250, justify=tkinter.CENTER, text="You have fallen in battle. Better luck next time")
        game_over.grid(row=0, column=1, columnspan=3)
        exit_button = tkinter.Button(root, command=root.quit)
        exit_button.grid(row=1, column=1)

monster_hp = 0
intro_label = tkinter.Label(root, text="What is your name?")
intro_label.grid(row=0, column=1)
player_name = tkinter.Entry(root)
player_name.grid(row=1, column=1)
name_button = tkinter.Button(root, text="Confirm", command= create_hero)
name_button.grid(row=2, column=1)
root.mainloop()