#A Full Featured English Dictonary Program In Python{CLI}

import json
import sys
import difflib


while True:
    def main(dataInput):
        wordOutput = json.load(open("data.json"))
        return wordOutput[dataInput.lower()]

    try :
        word = input("Type in a word (Enter exit() to quit app): ")
        if word == "exit()":
            sys.exit()
        else:
            nl = 0
            for x in main(word):
                nl = nl + 1
                print(str(nl) + ". {}".format(x))
            print("\n")
    except KeyError:
        wordCheck = json.load(open("data.json"))
        out = difflib.get_close_matches(word, wordCheck.keys())
        if out:
            print("Did you mean" + " {}?".format(str(out[0])))
            condition = input("Type in Yes or No: ")
        else:
            print("Invalid Word, please try again")
            sys.exit()
        if condition.lower() == "yes" or condition.lower() == "y":
            nl = 0
            for x in main(out[0]):
                nl = nl + 1
                print(str(nl) + ". {}".format(x))
            print("\n")
        elif condition.lower() == "no" or condition.lower() == "n":
            print("The Word " + "'{}'".format(word) + " Doesn't exist\nPlease try again\n")
        else:
            print("Invalid Response, Please try again")
            sys.exit()

    