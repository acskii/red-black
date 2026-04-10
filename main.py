# TEAM DETAILS
# Ahmed Abd Al Moneim
# Details: 
#       ID: 9284
#       Group: 3
#       Section: 1
#
# Andrew Sameh
# Details:
#       ID: 9489
#       Group: 3
#       Section: 1
#
# Galal Mohamed
# Details:
#       ID: 9453
#       Group: 3
#       Section: 1

from dictionary import load_dictionary
from red_black_tree import RedBlackTree
from interface import start_interface

def main():
    # Loading current words
    words = load_dictionary()
    tree = RedBlackTree()
    
    # Initialising tree
    for word in words:
        tree.insert(word)
    
    # Start user interface
    start_interface(tree)

if __name__ == "__main__":
    main()