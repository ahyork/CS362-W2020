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

#number of curses and victory cards
nV = tu.calculate_nV(player_names) # moved into testUtility
nC = tu.calculate_nC(player_names) # moved into testUtility

#Define box
box = tu.create_box(nV) # moved into testUtility

#Define supply order
supply_order = tu.define_supply_order() # moved into testUtility

#Pick 10 cards from box to be in the supply.
supply = tu.pull_cards_from_box(box) # moved into testUtility

#The supply always has these cards
tu.add_standard_treasure(supply, player_names) # moved into testUtility
tu.add_standard_victory_points_and_curses(supply, nV, nC) # moved into testUtility

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
