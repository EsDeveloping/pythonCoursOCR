#! /usr/bin/env python3
# coding: utf-8


"""module multipli contenant la fonction table"""


def calcul(nb, max=10):
	"""Fonction affichant la table de multiplication par nb de

	1 * nb jusqu'à max * nb"""


	i = 0
	while i < max:
		print("{} * {} = {}".format(i + 1, nb, (i + 1) * nb))
		i += 1



######################    MAIN     ################################
def main():
	nb = input("Entrez un nombre entier a multiplier ou 0 pour quiter")
	while int(nb) != 0:
		calcul(int(nb))
		nb = input("Entrez un nombre entier a multiplier ou 0 pour quiter")

if __name__ == "__main__":
	main()
