# Import Library JSON
import json

# Loading the data json
data = json.load(open("dictionary.json"))

# Function retrive definition
def retrive_definition(word):
    # Check exist word
    if word in data:
        return data[word]
    else:
        return ("The word doesn't exist, please check it.")
    
# Input from user
word_user = input("Enter a word: ")

# Retriving the function
print(retrive_definition(word_user))
