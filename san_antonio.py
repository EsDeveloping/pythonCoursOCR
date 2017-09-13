# -*- coding: latin-1 -*-

quotes = [

    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 

    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."

]


characters = [

    "alvin et les Chipmunks", 

    "Babar", 

    "betty boop", 

    "calimero", 

    "casper", 

    "le chat potté", 

    "Kirikou"

]

user_answer = raw_input("Tapez entrée pour connaitre une autre citation ou B pour quitter le programme.")
print(user_answer)

# Show random quote

if user_answer == "B":
	pass
# If user_answer == "B":
	#- leave the program
elif user_answer == "C":
	print("Reponse C")
else:
	pass
# Else:
	# show another quote


# Function random quote
def show_random_quote(my_list):
	quote = my_list[1]
	return quote
	# get a random number
	# get a quote from an array
	# print the quote in the interpreter, print() ?

print(show_random_quote(quotes))
