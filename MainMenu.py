# ###################
# Ian Janes
# Skyrim Ledger
# Main menu subfile
# ###################

import os

FILE_EXTENSION = ".list"
SUBDIRECTORY = "./Lists"

def show_menu():

    """
    Prints menu options for user.

    @param na : na

    @return na : na
    """

    print("Please pick an option from the following:")
    print("\t(L): List")
    print("\t(P): Prices")
    print("\t(S): Skills")

def get_menu_choice():

    """
    Gets a choice from the user and initiates its corresponding function based on the options presented by the 'show_menu' function.

    @param na : na

    @return na : na
    """

    valid = False
    while valid == False:
        response = input().lower()
        if response == "l":
            valid = True
            pass # Needs to implement a function to print the shopping list
        elif response == "p":
            valid = True
            pass # Needs to implement a function to view the prices of individual items
        elif response == "r":
            show_menu()
        elif response == "s":
            valid = True
            pass # Needs to implement a function to view the user's speech and other skills/perks
        else:
            print("Invalid response. For a list of options, enter \"R\".")

def get_shopping_lists():

    """
    Creates and returns a list of all 'FILE_EXTENSION' files in 'SUBDIRECTORY'.

    @param na : na

    @return lists (list) : List of all 'FILE_EXTENSION' files in 'SUBDIRECTORY'.
    """

    lists = []
    for item in os.listdir(SUBDIRECTORY):
        if item.endswith(FILE_EXTENSION):
            lists.append(item)
    return lists

def print_lists(lists):

    """
    Prints shopping list options for user.

    @param (list) lists : The list of 'FILE_EXTENSION' files.

    @return na : na
    """

    print("Choose one of the lists to view:")
    for i in range(len(lists)):
        print(f"\t({i}): {lists[i]}")

lists = get_shopping_lists() # debug
print_lists(lists) # debug