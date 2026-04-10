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
    
    try:
        with open(DICTIONARY_FILE, 'r') as dict:
            for line in dict:
                words.append(line.strip())
    except (OSError):
        print("[DICTIONARY]: No dictionary file found")
        return []
    
    return words

# Append dictionary text content with a word
def append_onto_dictionary(word: str) -> bool:
    # Append the given word to the end of the text content

    try:
        with open(DICTIONARY_FILE, 'a') as dict:
            dict.write("\n" + word.strip())
    except (OSError):
        print("[DICTIONARY]: Couldn't append word onto dictionary")
        return False
    
    return True

# Overwrite dictionary text content with provided list
def overwrite_dictionary(words: list[str]) -> bool:
    # Replace all file content here with the words in the given list

    try:
        with open(DICTIONARY_FILE, 'w') as dict:
            content = []
            for word in words:
                content.append(word + "\n")
                
            dict.write("".join(content))
    except (OSError):
        print("[DICTIONARY]: Couldn't overwrite dictionary")
        return False
    
    return True