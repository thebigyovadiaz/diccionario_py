# Import Librarys
import json
from difflib import get_close_matches

# Loading the data json
data = json.load(open("dictionary.json"))

# Function retrive definition
def retrive_definition(word):
    # Lower case to word
    word = word.lower()
    
    # Check exist word
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
		
		# If the answers is yes, retrive definition of suggested word
        if (action == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == "n"):
            return ("The word doesn't exist, yet.")
        else:
            return ("We don't understand your entry. Apologies.")

# Input from user
word_user = input("Enter a word: ")

# Retriving the function
output = retrive_definition(word_user)

# If a word has more than one definition, print them recursively
if type(output) == list:
    for item in output:
        print("-",item)
#For words having single definition
else:
    print("-",output)
