# This file handles all related operations to the dictionary text file
# This includes helper methods that provide interactions with the text file

# DICTIONARY TEXT FILE FORMAT:
#   Each line contains ONE word.
#   Each word is separated by a new line character

# Constant relative file path for dictionary
DICTIONARY_FILE = "./dictionary.txt"

# Loads all words within text file provided
def load_dictionary() -> list[str]:
    words = []
    
    # Include reading functionality here
    
    return words


# Append dictionary text content with a word
def append_onto_dictionary(word: str) -> bool:
    # Append the given word to the end of the text content
    # Follow the dictionary text file format
    # Return False if any error or failure occurs during overwrite
    return True

# Overwrite dictionary text content with provided list
def overwrite_dictionary(words: list[str]) -> bool:
    # Replace all file content here with the words in the given list
    # Follow the dictionary text file format
    # Return False if any error or failure occurs during overwrite
    return True