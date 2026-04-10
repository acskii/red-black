# This file handles user interaction with the console to run this project

# To provide required functionality, we need to follow these steps:
#   - Load current dictionary
#   - Create a red-black tree object
#   - Insert all current words in dictionary into the tree
#   - Allow user to choose either to look up or insert word using red-black tree object
#   - Print all red-black tree object properties to show to user

from red_black_tree import RedBlackTree

CHOICE_MESSAGE = """
    Do you want to:
    [0] Exit
    [1] Insert a word
    [2] Look up a word
"""


def start_interface(tree: RedBlackTree):
    while True:
        choice = get_choice()
        
        if (choice == 1):
            # Insert word
            word = input("Enter a word: ")
            tree.insert(word)
            print("Black Height: " + str(tree.black_height()))
            print("Tree Height: " + str(tree.tree_height()))
            print("Tree Size: " + str(tree.tree_size()))
        elif (choice == 0):
            # Exit
            return
        else:
            # Look up word
            word = input("Enter a word: ")
            found = tree.search(word)
            print("YES" if found else "NO")
            print("Black Height: " + str(tree.black_height()))
            print("Tree Height: " + str(tree.tree_height()))
            print("Tree Size: " + str(tree.tree_size()))
            

def get_choice():
    while True:
        print(CHOICE_MESSAGE)
        
        try:
            choice = int(input("Enter your choice: "))
            if (0 <= choice <= 2): return choice
        except:
            continue
