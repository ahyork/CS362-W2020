    # -*- coding: utf-8 -*-
"""
Created on Sunday 12 January 2020

@author: Arthur York (yorkar)
"""

import Dominion
import random
from collections import defaultdict
import testUtility as tu

#Get player names
player_names = tu.define_player_names() # moved into testUtility

#Define box
box = tu.create_box([]) # moved into testUtility

#Define supply order
supply_order = tu.define_supply_order() # moved into testUtility

#Pick 10 cards from box to be in the supply.
supply = tu.pull_cards_from_box(box) # moved into testUtility

#The supply always has these cards
# pass an empty array into the function below so when it initializes the
#   number of gardens it will always put 8, no matter how many people are
#   playing. This won't crash the program but it goes against the rules of the
#   game.
tu.add_standard_treasure_vp_curses(supply, []) # moved into testUtility

#initialize the trash
trash = []

#Costruct the Player objects
players = tu.construct_players(player_names) # moved into testUtility

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)
