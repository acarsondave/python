import mysql.connector
from difflib import get_close_matches
from sys import exit

conn = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

def Convert(tups, di):
    di = dict(tups)
    return di

cursor = conn.cursor()
word = input("Please enter an English word to get the meaning %s: "
%'(type in exit() to close the program)')
try:
    if word == "exit()":
        exit()
    else:
        query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" %word)
        results = cursor.fetchall() 
        dictionary = {}
        diFormat = Convert(results, dictionary)
        print(diFormat[word])
except KeyError:
    newquery = cursor.execute("SELECT * FROM Dictionary")
    newresults = cursor.fetchall()
    newdictionary = {}
    converted = Convert(newresults, newdictionary)
    matches = get_close_matches(word, converted, n=1, cutoff=0.8)
    if matches:
        print("Did you mean %s, reply with 'Y' or 'N'"%matches[0])
        answer = input()
        if answer == 'y' or answer == 'yes':
            print(diFormat[matches])
        else:
            print("Program is now exiting")
    else:
        print("Word '%s' Doesn't exist"%word)


