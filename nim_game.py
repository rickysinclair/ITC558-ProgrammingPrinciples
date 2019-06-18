# Simple game of Nim
#
# In this game two players take turns removing objects from distinct heaps or piles. On
# each turn, a player must remove at least one object, and may remove any number of objects
# provided they all come from the same heap/pile. The goal of the game is to avoid taking the
# last object.
#
# In this implementation of the game, there are 3 piles of objects. At the start of the game,
# each of the three piles will be initialized by a random number of objects. Random number
# should is between 5 and 15. The players will take turns picking up objects from the piles. A
# player can even pick up all items from a single pile. The player that picks up last object (across
# all piles) loses.


import random

PILE_A = random.randint(5, 15)  # random number generation for piles
PILE_B = random.randint(5, 15)
PILE_C = random.randint(5, 15)

PLAYER = "Player 1"  # initialise PLAYER


def display():
    """ The display function displays a graphical representation of the
    nim game and also displays the total of remaining items in each pile
    """
    print("A:", "*" * PILE_A) # graphically display items
    print("B:", "*" * PILE_B)
    print("C:", "*" * PILE_C)
    print("(" + str(PILE_A) + ", " +
          str(PILE_B) + ", " +
          str(PILE_C) + ")\n")  # numerically display total remaining items


def switchPlayers(player):
    """ The switchPlayers function switches PLAYER 1 -> PLAYER 2 or vice versa
    :param PLAYER:
    :return: PLAYER
    """
    if player == "Player 1":  # switch PLAYER names
        player = "Player 2"
    else:
        player = "Player 1"
    return player  # return PLAYER value to calling function


def getAmount(amount):
    """ The getAmount function prompts the user to enter the amount of items
    to remove from the pile and check for valid values to ensure an int has been
    entered
    :param amount:
    :return: amount
    """
    while True:
        try:
            amount = int(input("Choose how many objects to remove: "))  # check for int value
            if amount > 0:  # check for valid number
                break
            else:
                print("ERR: Sorry, that is not a valid number.")
        except ValueError:
            print("ERR: Sorry, that is not a valid number.")
    return (amount)  # return amount to calling function


def selectPile():
    """The selectPile function validates the user input by checking that they have selected a valid pile
    that has a value greater than 0.  It then calls the getAmount function to decrement the selected pile.
    """
    amount = ""

    global PILE_A  # access global variables for piles
    global PILE_B
    global PILE_C

    selectedPile = input("{}, choose your pile (A, B, C): ".format(PLAYER))

    while selectedPile != "A" and \
            selectedPile != "B" and \
            selectedPile != "C":  # check for valid pile selection
        print("ERR: Sorry, that is not a valid pile.")
        selectedPile = input("{}, choose your pile (A, B, C): ".format(PLAYER))

    while selectedPile == "A" and PILE_A == 0 or \
            selectedPile == "B" and PILE_B == 0 or \
            selectedPile == "C" and PILE_C == 0:  # check if selected pile has items remaining
        print("ERR: Sorry, this pile is already empty.")
        selectedPile = input("{}, choose your pile (A, B, C): ".format(PLAYER))

    if selectedPile == "A":
        amount = getAmount(amount)  # call amount entry function and assign return value to amount variable
        while amount > PILE_A:
            print("ERR: Sorry, there is not enough objects to remove in this pile.")
            amount = getAmount(amount)  # assign valid value to amount
        PILE_A -= amount;  # decrement PILE_A
        print("OK\n")

    elif selectedPile == "B":
        amount = getAmount(amount)  # call amount entry function and assign return value to amount variable
        while amount > PILE_B:
            print("ERR: Sorry, there is not enough objects to remove in this pile.")
            amount = getAmount(amount)  # assign valid value to amount
        PILE_B -= amount;  # decrement PILE_B
        print("OK\n")

    elif selectedPile == "C":
        amount = getAmount(amount)  # call amount entry function and assign return value to amount variable
        while amount > PILE_C:
            print("ERR: Sorry, there is not enough objects to remove in this pile.")
            amount = getAmount(amount)  # assign valid value to amount
        PILE_C -= amount;  # decrement PILE_C
        print("OK\n")


def main():
    global PLAYER  # access global variable for PLAYER

    global PILE_A  # access global variables for piles
    global PILE_B
    global PILE_C

    print("===== Welcome to Nim Game =====")  # display welcome message
    print("\nHere are the three piles")

    while True:

        totalPile = PILE_A + PILE_B + PILE_C  # calculate total items left in all piles

        if totalPile == 0:  # check to see if all piles are empty for end game
            PLAYER = switchPlayers(PLAYER)  # call function to switch players
            print("{} picked up the last object. <<<{}>>> is the WINNER."
                  "\n\nThanks for playing. Goodbye.".format(PLAYER, switchPlayers(PLAYER)))
            input() # input to prevent window from closing after game ends
            break  # break while loop to end game

        display()  # call display function

        selectPile()  # call selectPile function

        PLAYER = switchPlayers(PLAYER)  # switch PLAYER variable by calling switchPlayer function


main()
