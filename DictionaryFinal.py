#DictionaryFinal.py
#Designed by Lawrence Abu-Hammour
#July 2018
#This program accepts user input and searches for a key that matches
#what the user is requesting the definition of.

import json #Used to Import, Load, and Analyze *.json files
from difflib import get_close_matches #Used to determine similarity between user-input and an actual key in the *.json list

#Load *.json file into variable "data"
data = json.load(open("data.json"))

#Begin Function
def translate(word):
    #Switches to the lower case version of the user-input
    word = word.lower()
    #Conditional that if the user-input is a direct match to a word in the dictionary, it will ouput the definition
    if word in data:
        return data[word]
    #Conditional that capitalizes the first letter of the user-input to find a matching definition (Eg: Texas, California, etc.)
    elif word.title() in data:
        return data[word.title()]
    #Conditional that capitalizes the entire user-input to find a matching definition (Eg: USA, NATO, etc.)
    elif word.upper() in data
        return data[word.upper()]
    #Checks for similarity between words in the dictionary and the user-input and asks the user if they meant another word.
    #The user will then have to confirm whether or not they meant the other word. Takes into account different scenarios
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s ? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return "That word does not exist. Please double check your input and try again."
        else:
            return "The interactive dictionary did not understand your input. Please double check your input and try again."
    else:
        return "That word does not exist. Please double check your input and try again."

#User Input Occurs Here
word = input("Enter the word you would like the definition for: ")

#Output Statement
output = translate(word)

#Modifies output to optimize the readibility of the definition(s) and other types of outputs.
if type(output)== list:
    for item in output:
        print(item)
else:
    print(output)
