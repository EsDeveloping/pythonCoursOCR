#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random

# Initialize seed so we always get the same result between two runs.
# Comment this out if you want to change results between two runs.
# More on this here: http://stackoverflow.com/questions/22639587/random-seed-what-does-it-do
random.seed(0)

##################################################
#################### VOTES SETUP #################
##################################################

VOTES = 100000
MEDIAN = VOTES/2
CANDIDATES = {
    "hermione": "Hermione Granger",
    "balou": "Balou",
    "chuck-norris": "Chuck Norris",
    "elsa": "Elsa",
    "gandalf": "Gandalf",
    "beyonce": "Beyoncé"
}

MENTIONS = [
    "A rejeter",
    "Insuffisant",
    "Passable",
    "Assez Bien",
    "Bien",
    "Très bien",
    "Excellent"
]

def create_votes():
    return [
        {
            "hermione": random.randint(3, 6),
            "balou": random.randint(0, 6),
            "chuck-norris": random.randint(0, 2),
            "elsa": random.randint(1, 2),
            "gandalf": random.randint(3, 6),
            "beyonce": random.randint(2, 6)
        } for _ in range(0, VOTES)
    ]

##################################################
#################### FUNCTIONS ###################
##################################################

candidates = {
    'hermione': [0,1,2,3,4,5,6],
    'balou': [0,1,2,3,4,5,6],
    'chuck-norris': [0,1,2,3,4,5,6],
    'elsa': [0,1,2,3,4,5,6],
    'gandalf': [0,1,2,3,4,5,6],
    'beyonce': [0,1,2,3,4,5,6]
}

def results_hash(votes):
    candidates_results = { 
        candidate: [0]*len(MENTIONS)
        for candidate in CANDIDATES.keys()
    }
    for vote in votes:
        for candidate, mention in vote.items():
            candidates_results[candidate][mention] +=1
    print(candidates_results)
    #return candidates_results


##################################################
#################### MAIN FUNCTION ###############
##################################################

def main():
    votes = create_votes()
    results = results_hash(votes)

if __name__ == '__main__':
    main()