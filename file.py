#A code that auto format strings inputted by the user i.e:
# Auto capitalizes the first letter in a string, adds a fullstop to a sentence and a question mark
#to a question

def sentence(phrase):
    capitalized = phrase.capitalize()
    interrogatives = ("how", "why", "what", "where", "when", "who", "are")
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
userInput = input("Say Something: ")
while userInput != 'end' :
    results.append(sentence(userInput))
    userInput = input("Say Something: ")

def output1():
    x = 0
    for i in results :
        print(results[x])
        x = x + 1

#output1()

print(" ".join(results))