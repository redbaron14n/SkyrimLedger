# ###################
# Ian Janes
# Skyrim Ledger
# List interpreter subfile
# ###################

import os

FILE_EXTENSION = ".list"
SUBDIRECTORY = "./Lists"

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

get_shopping_lists()