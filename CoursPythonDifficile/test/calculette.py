#! /usr/bin/env python3
# coding: utf-8


# Calculette réaliser pour utiliser les boucles
def calcul():
	table = input("Quel table de mutiplication voulez vous voir? 0 pour quiter \n")

	while int(table) != 0:
		i = 0
		while i < 10:
			print("{} * {} = {}".format(i + 1, int(table), (i + 1) * int(table)))
			i += 1
		table = input("Quel table de mutiplication voulez vous voir? 0 pour quiter")

def main():
	calcul()

if __name__ == "__main__":
	main()
