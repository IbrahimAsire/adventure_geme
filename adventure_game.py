import time
import random


def print_p(msg_print):
    print(msg_print)
    time.sleep(2)


def intro():
    print_p("Do you think your luck is good?")
    print_p("Your luck will help you if it chooses the correct weapon for you")
    print_p("In front of you a fortress that has three doors.")
    print_p("Behind the three doors are three enemies.")
    print_p("Each of them dies with a specific weapon.")
    print_p("Dracula dies by fire only.\n"
            "The wizardry woman dies by magic talisman only.\n"
            "And the giant die only by the gun .")
    print_p("So,I wish for you good luck !!")


def choose_door(weapon):
    print_p("Choose number please , Let's see your luck today: ")
    door = input(" '1' OR '2' OR '3'\n")
    if door == "1":
        first_door(weapon)
    elif door == "2":
        second_door(weapon)
    elif door == "3":
        third_door(weapon)
    else:
        choose_door(weapon)


def first_door(weapon):
    print_p("Here the wizardry woman, good luck with your luck ..\n "
            "Your weapon is " + weapon + "!")
    if weapon == "magic talisman":
        print_p("You won because you are brave without your luck.")
    else:
        print_p("\nUnfortunately, your luck seems bad today.")
        print_p("You did not get magic talisman to win.")
    play_again(weapon)


def second_door(weapon):
    print_p("Here the the giant, good luck with your luck ..\n"
            "Your weapon is " + weapon + " !")
    if weapon == "the gun":
        print_p("I think you trust your luck so much, "
                "luck is always with the brave ... you won.")
    else:
        print_p("\nThe giant is very strong, does not die easily .. ")
        print_p("Your luck did not give you the gun to win ...")
    play_again(weapon)


def third_door(weapon):
    print_p("Your luck should help you with the vampire dracula.\n "
            "Your weapon is " + weapon + "!")
    if weapon == "fire":
        print_p("Actually, your luck is very good it helped you today .. "
                "Congratulations on your victory, you are brave.")
    else:
        print_p("\nIf luck did not help you, "
                "it is impossible to win over them.")
        print_p("Vampires are one of the most dangerous enemies, "
                "You were defeated .. ")
    play_again(weapon)


def play_again(weapon):
    try_again = input("Hey Brave Do you want to try your luck again? "
                      " 'yes'/ 'no'\n").lower()
    if "no" in try_again:
        print_p("If you feel your luck is good, try again.")
        print_p("\nGoodbye")
    elif "yes" in try_again:
        print_p("Really you are brave, I wish you good luck, "
                "We'll start with you from the beginning, let's go ..")
        play_game()


def play_game():
    intro()
    weapon = random.choice(["the gun", "magic talisman", "fire"])
    choose_door(weapon)
    play_again(weapon)


play_game()
