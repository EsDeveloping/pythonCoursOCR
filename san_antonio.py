# -*- coding: utf-8 -*-
import random
import json

# json = JavaScript Object Notation

quotes = []
characters = []
#quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !","On doit pouvoir choisir entre s'écouter parler et se faire entendre."]
#characters = ["alvin et les Chipmunks","Babar","betty boop", "calimero","casper","le chat potté","Kirikou"]

def import_list_from_json():
	value = []
	with open('characters.json') as f:
		data = json.load(f)
		for character in data:
			value.append(character['character'])
		return value

def import_quote_from_json():
	value = []
	with open('quote.json')	as f:
		data = json.load(f)
		for citation in data:
			value.append(citation['quote'])
		return value

characters = import_list_from_json()
quotes = import_quote_from_json()

def show_random_item(my_list):
	rand_numb = random.randint(0,len(my_list) -1)
	quote = my_list[rand_numb]
	return quote

def show_random_quote(my_list):
	rand_numb = random.randint(0, len(my_list) -1)
	quote = my_list[rand_numb].replace("\n\t\t\t\t\t\t\t\t\t", "\n\t\t")
	return quote

def capitalize(words):
	for word in words:
		word.capitalize()

def message(character, quote):
	capitalize(character)
	capitalize(quote)
	return "{} a dit : {}".format(character, quote)

user_answer = ""


while user_answer != "B":
	print(message(show_random_item(characters), show_random_quote(quotes)))
	user_answer = input("\n\nTapez entrée pour connaitre une autre citation ou B pour quitter le programme.")



	

#print(show_random_quote(quotes))
