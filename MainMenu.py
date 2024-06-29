# ###################
# Ian Janes
# Skyrim Ledger
# Main menu subfile
# ###################

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