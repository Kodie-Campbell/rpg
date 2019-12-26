from random import randint
from tkinter import *

root = Tk()
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
def battle(monster):
    
    monster_hp = randint(10,20)
    combat_text = Label(root, text="the monster is looming over you")
    combat_text.grid(row=o, column=1)
    while monster_hp > 0 and hero.hp > 0:
        print("enter attack or flee")
        action = input(":")
        if action == "flee":
            print("you run in terror out of the cave")
            hero.hp = 0
        if action == "attack":
            print("you swing your dagger")
            damage = randint(1,5)
            print("it hits for " + str(damage) + " points")
            monster_hp = monster_hp - damage
            print("the orc has " + str(monster_hp) + " hp remaining")
            input("press enter to continue:")
            if monster_hp > 0:
                print("the orc slashes with its claws")
                damage = randint(1,5)
                print("it hits for " + str(damage) + " points")
                hero.hp = hero.hp - damage
                print("You have " + str(hero.hp) + " hp remaining")
                input("press enter to continue:")
            else:
                print("You have slain the monster")
                print("Do you go left or right?a")

def create_hero():
    global hero
    global greeting
    global player_name
    global intro_label
    global intro_text
    global next_btn
    name = player_name.get()
    hero = player(name, 100, ["dagger"])
    intro_label.destroy()
    name_button.destroy()
    player_name.destroy()
    intro_text = Label(root,wraplength=250, justify=CENTER, text="Welcome " + hero.name + " you find your self in a cavern.")
    intro_text.grid(row=0, column=0, columnspan=3)
    next_btn = Button(root, text="Next", justify=CENTER, command= move_loop)
    next_btn.grid(row=1, column=1 )
    hp_indicator = Label(root, text="HP: "+ str(hero.hp))
    hp_indicator.grid(row=5, column=0)
    name_plate = Label(root, text=hero.name)
    name_plate.grid(row=5, column=1)
    enemy_hp = Label(root, text= "Foe's hp: " + str(monster_hp))
    enemy_hp.grid(row=5, column=2)

def move_left():
    global  left_btn
    global right_btn
    global nav_text
    global left_label
    global encounter_start
    global start_fight
    nav_text.destroy()
    left_btn.destroy()
    right_btn.destroy()
    left_label = Label(root, wraplength=250, justify=CENTER, text="You go Left")
    left_label.grid(row=0, column=1)
    encounter = randint(0, 2)
    if encounter == 1:
        encounter_start = Label(root, wraplength=250, text="You see an orc ahead\n It attacks")
        encounter_start.grid(row=1, column=1)
        start_fight = Button(root, text="Fight", command=lambda: battle("orc"))
        start_fight.grid(row=2, column=1)
    else:
        left_btn = Button(root, text="Left", command=move_left)
        left_btn.grid(row=1, column=0)
        right_btn = Button(root, text="Right", command=move_right)
        right_btn.grid(row=1, column=2)

def move_right():
    global left_btn
    global right_btn
    global nav_text
    global left_label
    global encounter_start
    global start_fight
    nav_text.destroy()
    left_btn.destroy()
    right_btn.destroy()
    right_label = Label(root, wraplength=250, justify=CENTER, text="You go Right ")
    right_label.grid(row=0, column=1)
    encounter = randint(0, 2)
    if encounter == 1:
        encounter_start = Label(root, wraplength=250, text="You see an orc ahead\n It attacks")
        encounter_start.grid(row=1, column=1)
        start_fight = Button(root, text="Fight", command=lambda: battle("orc"))
        start_fight.grid(row=2, column=1)
    else:
        left_btn = Button(root, text="Left", command=move_left)
        left_btn.grid(row=1, column=0)
        right_btn = Button(root, text="Right", command=move_right)
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
    next_btn.destroy()
    intro_text.destroy()
    if hero.hp > 0:
        nav_text = Label(root, wraplength=250, justify=CENTER, text="You can just make out 2 tunnels at the edge of the flickering light of your torch. Will you go right or left?")
        nav_text.grid(row=0, column=0, columnspan=3)
        left_btn = Button(root, text="Left", command= move_left)
        left_btn.grid(row=1, column=0)
        right_btn = Button(root, text="Right", command= move_right)
        right_btn.grid(row=1, column=2)

    else:
        game_over =Label(root, wraplength=250, justify=CENTER, text="You have fallen in battle. Better luck next time")
        game_over.grid(row=0, column=1, columnspan=3)
        exit_button = Button(root, command=root.quit)
        exit_button.grid(row=1, column=1)
        #encounter = randint(0, 2)
        #if encounter == 1:
            #print("You see an orc ahead")
            #print("It attacks")
           # battle("orc")
       # else:
          #  print("This cavern seems empty")
          #  print("Do you go left or right?")




monster_hp = 0
intro_label = Label(root, text="What is your name?")
intro_label.grid(row=0, column=1)
player_name = Entry(root)
player_name.grid(row=1, column=1)

name_button = Button(root, text="Confirm", command= create_hero)
name_button.grid(row=2, column=1)

root.mainloop()