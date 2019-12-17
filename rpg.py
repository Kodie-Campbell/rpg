from random import randint

class player:

    def __init__(self, name, hp, inventory):
        self.name = name
        self.hp = hp
        self.inventory = inventory
def battle(monster):
    monster_hp = randint(10,20)
    print("the monster is looming over you")
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
player_name = input("What is your name? ")

hero = player(player_name, 100, ["dagger"])

print("Welcome " + hero.name + " you find your self in a cavern.")
print("You can just make out 2 tunnels at the edge of the flickering")
print("light of your torch.")
print("Will you go right or left?")

while hero.hp > 0:
    direction = input(":")
    print("You go " + direction)
    encounter = randint(0,2)
    if encounter == 1:
        print("You see an orc ahead")
        print("It attacks")
        battle("orc")
    else:
        print("This cavern seems empty")
        print("Do you go left or right?")
print("You have fallen in battle. Better luck next time")