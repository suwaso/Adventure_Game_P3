import time
import random


def print_text(txt_to_print):
    print(txt_to_print)
    time.sleep(1.8)


def intro(Weapons, Monsters, Villages):
    print_text("\nYou are one of the most famous knights in this region\n")
    print_text("A message has come to you from the people of the " + Villages +
               " Village asking you for help to save them from " + Monsters +
               " that attacking their herd\n")
    print_text("You have reached the grazing area of " + Villages + " Village,"
               "a vast area full of grass\n")
    print_text("In front of you is a Woods.\n")
    print_text("In your left hand is an abandoned house.\n")
    print_text("Currently you have a knife in your hand but its not in good"
               " condition.\n")


def Grazing(Weapons, Monsters, Villages):
    print_text("What would you like to do?")
    print_text("Enter 1 to go to the woods")
    print_text("Enter 2 to discover the abandoned house ")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            Woods(Weapons, Monsters, Villages)
            break
        elif choice1 == "2":
            house(Weapons, Monsters, Villages)
            break


def house(Weapons, Monsters, Villages):
    if "Hunting rifle" in Weapons:
        print_text("\nYou carfuly enter into the house.")
        print_text("\nLooks like you've forgotten, you've been here before "
                   "and got the gun, nothing really cool here to take it")
        print_text("\nYou walk back to the Grazing area.\n")
    else:
        print_text("\nYou carfuly enter into the house.")
        print_text("\nIt looks like a dilapidated house and dust everywhere")
        print_text("\nBut you found the hunting rifle hanging on the wall")
        print_text("\nWow, it's in good condition and full of ammunition")
        print_text("\nYou have take it with you")
        print_text("\nYou walk back out to the Grazing area.\n")
        Weapons.append("Hunting rifle")
    Grazing(Weapons, Monsters, Villages)


def Woods(Weapons, Monsters, Villages):
    print_text("\nYou are going very carefully towards the woods")
    print_text("\nAmidst the dense trees, you heard a movement eastward ")
    print_text("\nYou go cautiously toward that sound. It's like a sound of "
               + Monsters + ".")
    print_text("\nOH NO! its the " + Monsters + " in front of you!")
    print_text("\nThe " + Monsters + " comes to you!\n")
    if "Hunting rifle" not in Weapons:
        print_text("You live under pressure, how a shabby knife can"
                   " help you in this situation\n")
    while True:
        choice2 = input("What would be your decision in this case?"
                        " (1) Fighting or (2) run away?")
        if choice2 == "1":
            if "Hunting rifle" in Weapons:
                print_text("\nOnce the " + Monsters + " has gone out to "
                           "attack you, you have take your Hunting rifle")
                print_text("\nHere your skills as a knight began to appear")
                print_text("\nAn unmistakable shot was fired at the "
                           + Monsters + ", and within seconds the monster"
                           " fell to the ground!")
                print_text("\nThe villagers have been freed from this monster")
                print_text("\nThe monster killed, and you WON!\n")
            else:
                print_text("\nYou try to resist, but you don't have any tools"
                           " to help you win")
                print_text("\nyour knife can't beat "
                           + Monsters + ".")
                print_text("\nYou have been Killed!\n")
            play_again()
            break
        if choice2 == "2":
            print_text("\nYou run back faster into the Grazing area. ")
            print_text("\nYou are a lucky!, you are faster than "
                       + Monsters + "")
            print_text("\nYou are Safe now\n")
            Grazing(Weapons, Monsters, Villages)
            break


def play_again():
    again = input("Do you want to play again? (y/n)").lower()
    if again == "y":
        print_text("\n\n\n\nAmazing! lets play again\n\n\n\n")
        start_game()
    elif again == "n":
        print_text("\n\n\n\nThank you for play this game :)"
                   " feel free to come and play again anytime.\n\n\n\n")
    else:
        play_again()


def start_game():
    Weapons = []
    Monsters = random.choice(["Bigfoot", "Vampires", "Werewolves",
                              "Chupacabra"])
    Villages = random.choice(["Dammam", "Khobar", "Jubail"])
    intro(Weapons, Monsters, Villages)
    Grazing(Weapons, Monsters, Villages)


start_game()
