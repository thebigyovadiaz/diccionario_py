# Import Library JSON
import json

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
    else:
        return ("The word doesn't exist, please check it.")
    
# Input from user
word_user = input("Enter a word: ")

# Retriving the function
print(retrive_definition(word_user))
