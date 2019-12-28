import random
import tkinter
import functools

# set up winodow and basic cell config
root = tkinter.Tk()
root.geometry("250x200")
root.title("cave explorer")
root.rowconfigure(0, {"minsize": 30})
root.columnconfigure(0, {"minsize": 30})
root.rowconfigure(1, {"minsize": 30})
root.columnconfigure(1, {"minsize": 30})
root.rowconfigure(2, {"minsize": 30})
root.columnconfigure(2, {"minsize": 30})
root.rowconfigure(3, {"minsize": 30})
root.rowconfigure(4, {"minsize": 30})
root.rowconfigure(5, {"minsize": 30})
root.rowconfigure(6, {"minsize": 30})


# creates a player object to store character information
class Player:
    def __init__(self, name, hp, inventory):
        self.name = name
        self.hp = hp
        self.inventory = inventory


# function for when the player looses a fight
# noinspection PyGlobalUndefined
def loose_fight(monster):
    global winner_text
    global nav_text
    global left_btn
    global right_btn
    global attack_text
    global damage_text
    global next_btn
    global monster_hp
    # remove unneeded widgets from the screen
    attack_text.destroy()
    damage_text.destroy()
    next_btn.destroy()
    # set monster hp to 0
    monster_hp = 0
    # update the enemy hp on screen
    enemy_hp.config(text="Foe's hp: " + str(monster_hp))
    # display player death text
    looser_text = tkinter.Label(root, wraplength=250, text="You have been defeated by the " + monster)
    looser_text.grid(row=0, column=0, columnspan=3)
    # creates and displays a button to close the game
    close_app = tkinter.Button(root, text="close", command=root.quit)
    close_app.grid(row=1, column=1)


# function for when a player wins a fight
# noinspection PyGlobalUndefined
def win_fight(monster):
    global winner_text
    global nav_text
    global left_btn
    global right_btn
    global attack_text
    global damage_text
    global next_btn
    global monster_hp
    # remove unneeded widgets from the screen
    attack_text.destroy()
    damage_text.destroy()
    next_btn.destroy()
    # set monster hp to 0
    monster_hp = 0
    # update enemy hp counter on screen
    enemy_hp.config(text="Foe's hp: " + str(monster_hp))
    # display combat winner text
    winner_text = tkinter.Label(root, wraplength=250, text="You have defeted the " + monster)
    winner_text.grid(row=0, column=0, columnspan=3)
    # display text prompting the user to select a direction
    nav_text = tkinter.Label(root, wraplength=250, justify=tkinter.CENTER, text="You can just make out 2 tunnels at "
                                                                                "the edge of the flickering light of "
                                                                                "your torch. Will you go right or "
                                                                                "left?")
    nav_text.grid(row=1, column=0, columnspan=3)
    # create and display buttons for choosing direction and
    # moving to he appropriate function
    left_btn = tkinter.Button(root, text="Left", command=move_left)
    left_btn.grid(row=2, column=0)
    right_btn = tkinter.Button(root, text="Right", command=move_right)
    right_btn.grid(row=2, column=2)


# function for handling the monsters turn to attack
# noinspection PyGlobalUndefined
def monsterattack(monster):
    global attack_text
    global damage_text
    global next_btn
    global dir_label
    # remove unneeded widgets from the screen
    dir_label.destroy()
    attack_text.destroy()
    damage_text.destroy()
    # randomly generate the attacks damage
    damage = random.randint(0, 5)
    # display the monsters attack to the user
    attack_text = tkinter.Label(root, wraplength=250, text="The " + monster + " attacks")
    attack_text.grid(row=0, column=0, columnspan=3)
    damage_text = tkinter.Label(root, wraplength=250, text="It hits for " + str(damage) + " points")
    damage_text.grid(row=1, column=0, columnspan=3)
    # subtract the monster damage from the heros health
    hero.hp = hero.hp - damage
    # update the hero's hp indicator on screen
    hp_indicator.config(text="HP: " + str(hero.hp))
    # set partial variable to insert into the next button if the hero is not dead
    action_with_arg = functools.partial(battle, monster)
    # check if the hero is dead
    if hero.hp <= 0:
        # if the hero is dead update next button to go to loose_fight function
        action_with_arg = functools.partial(loose_fight, monster)
    # Next button to go to next stage of combat if the hero is not dead
    # or to loose_fight if hero is dead
    next_btn.config(command=action_with_arg)


# function to handle the players attack turn
# noinspection PyGlobalUndefined
def attack(monster):
    global monster_hp
    global combat_text
    global battle_options
    global attack_text
    global damage_text
    global next_btn
    # remove unneeded widgets from the screen
    combat_text.destroy()
    battle_options.destroy()
    attack_btn.destroy()
    flee_btn.destroy()
    # show attack flavor text
    attack_text = tkinter.Label(root, wraplength=250, text="You swing your dagger at the " + monster)
    attack_text.grid(row=0, column=0, columnspan=3)
    # randomly generate attack damage
    damage = random.randint(0, 5)
    # display attack damage to the user
    damage_text = tkinter.Label(root, wraplength=250, text="You hit for " + str(damage) + " points")
    damage_text.grid(row=1, column=0, columnspan=3)
    # subtract attack damage from the monster's hp
    monster_hp = monster_hp - damage
    # update the enemy hp indicator on screen
    enemy_hp.config(text="Foe's hp: " + str(monster_hp))
    # set partial variable for next button to the monsterattack variable
    action_with_arg = functools.partial(monsterattack, monster)
    # check if the monster is dead
    if monster_hp <= 0:
        # set partial variable to win_fight if monster is dead
        action_with_arg = functools.partial(win_fight, monster)
    # create next button to go to monsterattack or win fight
    next_btn = tkinter.Button(root, text="Next", command=action_with_arg)
    next_btn.grid(row=2, column=1)


# function to handle the user fleeing from battle
# noinspection PyGlobalUndefined
def flee(monster):
    global combat_text
    global battle_options
    # remove unneeded widgets from the screen
    combat_text.destroy()
    battle_options.destroy()
    attack_btn.destroy()
    flee_btn.destroy()
    # display fleeing text to the user
    fleeing = tkinter.Label(root, wraplength=250, text=" The " + monster + "has terified you. You have fled from the "
                                                                           "cave in shame")
    fleeing.grid(row=0, column=0, columnspan=3)
    # create and display a button to close the game
    close_app = tkinter.Button(root, text="close", command=root.quit)
    close_app.grid(row=1, column=1)


# function for beginning the combat loop
# noinspection PyGlobalUndefined
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
    # remove unneeded widgets from the screen, since this function is called
    # from multiple functions some widgets may or may not exist this prevents
    # errors when trying to remove non existent widgets
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
    # if monsters hp is 0 this is the first time though the combat loop so
    # randomly generate enemy hp
    if monster_hp == 0:
        monster_hp = random.randint(10, 20)
    # update enemy hp indicator on screen
    enemy_hp.config(text="Foe's hp: " + str(monster_hp))
    # update hero hp indicator on screen
    hp_indicator.config(text="HP: " + str(hero.hp))
    # display combat flavor text
    combat_text = tkinter.Label(root, text="the monster is looming over you")
    combat_text.grid(row=0, column=0, columnspan=3)
    # prompt user for action selection
    battle_options = tkinter.Label(root, text="Do you attack or flee")
    battle_options.grid(row=1, column=0, columnspan=3)
    # button for attack that starts the attack function
    attack_btn = tkinter.Button(root, text="attack", command=lambda: attack(monster))
    attack_btn.grid(row=2, column=2)
    # button for flee that starts the flee fucntion
    flee_btn = tkinter.Button(root, text="Flee", command=lambda: flee(monster))
    flee_btn.grid(row=2, column=0)


# function to create a hero from player input
# noinspection PyGlobalUndefined
def create_hero():
    global hero
    global greeting
    global player_name
    global intro_label
    global intro_text
    global next_btn
    global enemy_hp
    global hp_indicator
    # input box for getting the hero name
    name = player_name.get()
    # creates a hero with the name and default hp and inventory
    hero = Player(name, 100, ["dagger"])
    # removes unneeded widgets from the screen
    intro_label.destroy()
    name_button.destroy()
    player_name.destroy()
    # displays intro text
    intro_text = tkinter.Label(root, wraplength=250, justify=tkinter.CENTER, text="Welcome " + hero.name + " you find "
                                                                                                           "your self"
                                                                                                           " in a "
                                                                                                           "cavern.")
    intro_text.grid(row=0, column=0, columnspan=3)
    # button to move to the movement loop
    next_btn = tkinter.Button(root, text="Next", justify=tkinter.CENTER, command=move_loop)
    next_btn.grid(row=1, column=1)
    # creates hero h indicator on screen
    hp_indicator = tkinter.Label(root, text="HP: " + str(hero.hp))
    hp_indicator.grid(row=5, column=0)
    # creates nameplate on screen
    name_plate = tkinter.Label(root, text=hero.name)
    name_plate.grid(row=5, column=1)
    # creates enemy hp indicator on screen
    enemy_hp = tkinter.Label(root, text="Foe's hp: " + str(monster_hp))
    enemy_hp.grid(row=5, column=2)


# this function handles the player moving left
# noinspection PyGlobalUndefined
def move_left():
    global left_btn
    global right_btn
    global nav_text
    global dir_label
    global encounter_start
    global start_fight
    global winner_text
    # remove unneeded widgets from the screen, since this function is called
    # from multiple functions some widgets may or may not exist this prevents
    # errors when trying to remove non existent widgets
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
    # displays the move left text to the user
    dir_label = tkinter.Label(root, wraplength=250, justify=tkinter.CENTER, text="You go Left")
    dir_label.grid(row=0, column=1)
    # randomly set a number to see if an encounter happens
    encounter = random.randint(0, 2)
    # uses encounter variable to see if an encounter happens
    if encounter == 1:
        # removes unneeded widgets from he screen
        dir_label.destroy()
        # displays encounter start text
        encounter_start = tkinter.Label(root, wraplength=250, text="You see an orc ahead\n It attacks")
        encounter_start.grid(row=1, column=1)
        # button to launch the battle function
        start_fight = tkinter.Button(root, text="Fight", command=lambda: battle("orc"))
        start_fight.grid(row=2, column=1)
    # if no encounter happens prompt user to select another direction
    else:
        left_btn = tkinter.Button(root, text="Left", command=move_left)
        left_btn.grid(row=1, column=0)
        right_btn = tkinter.Button(root, text="Right", command=move_right)
        right_btn.grid(row=1, column=2)


# this function handles the player moving right
# noinspection PyGlobalUndefined
def move_right():
    global left_btn
    global right_btn
    global nav_text
    global encounter_start
    global start_fight
    global dir_label
    global winner_text
    # remove unneeded widgets from the screen, since this function is called
    # from multiple functions some widgets may or may not exist this prevents
    # errors when trying to remove non existent widgets
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
    # displays the move right text to the user
    dir_label = tkinter.Label(root, wraplength=250, justify=tkinter.CENTER, text="You go Right ")
    dir_label.grid(row=0, column=1)
    # randomly set a number to see if an encounter happens
    encounter = random.randint(0, 2)
    if encounter == 1:
        # removes unneeded widgets from he screen
        dir_label.destroy()
        # displays encounter start text
        encounter_start = tkinter.Label(root, wraplength=250, text="You see an orc ahead\n It attacks")
        encounter_start.grid(row=1, column=1)
        # button to launch the battle function
        start_fight = tkinter.Button(root, text="Fight", command=lambda: battle("orc"))
        start_fight.grid(row=2, column=1)
    # if no encounter happens prompt user to select another direction
    else:
        left_btn = tkinter.Button(root, text="Left", command=move_left)
        left_btn.grid(row=1, column=0)
        right_btn = tkinter.Button(root, text="Right", command=move_right)
        right_btn.grid(row=1, column=2)


# function to start movement
# noinspection PyGlobalUndefined
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
    # remove unneeded widgets from the screen, since this function is called
    # from multiple functions some widgets may or may not exist this prevents
    # errors when trying to remove non existent widgets
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
    # removes unneeded widgets from the screen
    next_btn.destroy()
    intro_text.destroy()
    nav_text = tkinter.Label(root, wraplength=250, justify=tkinter.CENTER, text="You can just make out 2 tunnels "
                                                                                "at the edge of the flickering "
                                                                                "light of your torch. Will you go "
                                                                                "right or left?")
    nav_text.grid(row=0, column=0, columnspan=3)
    # buttons for the user to select left or right movement
    left_btn = tkinter.Button(root, text="Left", command=move_left)
    left_btn.grid(row=1, column=0)
    right_btn = tkinter.Button(root, text="Right", command=move_right)
    right_btn.grid(row=1, column=2)


# sets initial monster hp to 0
monster_hp = 0
# displays game start text asking for hero name
intro_label = tkinter.Label(root, text="What is your name?")
intro_label.grid(row=0, column=1)
player_name = tkinter.Entry(root)
player_name.grid(row=1, column=1)
# Button to use the input to create a hero object
name_button = tkinter.Button(root, text="Confirm", command=create_hero)
name_button.grid(row=2, column=1)
# mainloop for the game window
root.mainloop()
