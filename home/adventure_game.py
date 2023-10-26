# You can use this workspace to write and submit your adventure game project.
import time
import random
import sys

enemies = ['Troll', 'Demon', 'Giant', 'Wicked fairie', 'gorgon']
weapon = ['battle axe', 'cross', 'sling of stone', 'charm', 'sword']
armed = None
index = random.randrange(0, 4)
chestBox = weapon[index]
initial_weapon = "dagger"
prepared = False

message_a = "You find yourself standing in an open field,"
message_b = "filled with grass and yellow wildflowers."
message = message_a + message_b
message2_a = f"Rumor has it that a {enemies[index]} is somewhere around here,"
message2_b = "and has been terrifying the nearby village."
message2 = message2_a + message2_b
message3 = "In front of you is a house."
message4 = "To your right is a dark cave."
message5 = "In your hand you hold your trusty (but not very effective) dagger."
option1 = "Enter 1 to knock on the door of the house."
option2 = "Enter 2 to peer into the cave."
inputs = "What would you like to do?"


def print_pause(message):
    print(message)
    time.sleep(1)


print_pause('\n')
print_pause(message)
print_pause(message2)
print_pause(message3)
print_pause(message4)
print_pause(message5)


a = True


def restart():
    global armed
    global index
    global chestBox
    global initial_weapon
    global prepared
    a = True
    while a:
        q = input("Would you like to play again? (y/n)")
        print_pause("\n")
        if q.lower() == "y" or q.title() == "Yes":
            print_pause("Excellent! Restarting the game ...")
            armed = None
            index = random.randrange(0, 4)
            chestBox = weapon[index]
            initial_weapon = "dagger"
            prepared = False
            return True
        elif q.lower() == "n" or q.title() == "No":
            print_pause("Thanks for playing! See you next time.")
            sys.exit()
            return False
        else:
            continue

            
def fight():
    # Things that happen when the player fights
    print_pause("\n")
    if armed:
        d_1 = f"As the {enemies[index]} moves to attack, "
        d_2 = f'you unsheath your new {initial_weapon}.'
        d = d_1 + d_2
        print_pause(d)
        f = f"The {weapon[index]} shines brightly in your hand"
        print_pause(f"{f} as you brace yourself for the attack.")
        g = f"But the {enemies[index]} takes one look"
        print_pause(f"{g} at your shiny new toy and runs away!")
        print_pause("\n")
        vc = "You have rid the town of the"
        print_pause(f"{vc} {enemies[index]}. You are victorious!")
        restart()
    else:
        print_pause("\n")
        print_pause("You do your best...")
        re = "but your {initial_weapon} is no"
        print_pause(f"{re} match for the {enemies[index]}.")
        print_pause("You have been defeated!")
        print_pause("\n")
        print_pause("GAME OVER!")
        restart()


def cave(ar, in_we):
    # Things that happen to the player goes in the cave
    print_pause("\n")
    print_pause("You peer cautiously into the cave.") 
    if ar:
        gg = "You've been here before, "
        print_pause1("{gg}and gotten all the good stuff.")
        print_pause2("It's just an empty cave now.")
        print_stop = print_pause1 + print_pause2
        armed = ar
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a chest box behind a rock.")
        print_pause(f"And in it, you have found the {weapon[index]}")
        gh = "You discard your silly old "
        print_pause(f"{in_we} and take the {weapon[index]} with you.")
        armed = weapon[index]
    print_pause("You walk back out to the field.")
    return armed


def field():
    # Things that happen when the player runs back to the field
    print('\n')
    print_pause(option1)
    print_pause(option2)
    print_pause(inputs)


def house():
    # Things that happen to the player in the house
    print_pause("\n")
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens and out steps "
                f"a {enemies[index]}.")
    print_pause(f"Eep! This is the {enemies[index]} house!")
    print_pause(f"The {enemies[index]} attacks you!")
    
    if not prepared:

        print_pause(f"You feel a bit under-prepared for this, what with only "
                    f"having a {initial_weapon}.")
        
    while True:
        action = input("Would you like to (1) fight or (2) run away?\n")
        if action == '1':
            fight()
            return True
        elif action == '2':
            print_pause("You run back into the field. Luckily, you don't seem "
                        "to have been followed.")
            return True
        else:
            print("Invalid input. Please enter 1 or 2.")


while True:
    field()
    ans = input("(Please enter 1 or 2).\n")

    if ans == '1':
        house_result = house()
        if house_result:
            continue
        else:
            a = restart()
    elif ans == '2':
        armed = cave(armed, initial_weapon)
        initial_weapon = armed
        prepared = True
    else:
        print("Invalid input. Please enter 1 or 2.")
        continue
