# test utility file that modularizes code for easy testing use.
# 12 January 2020
# Arthur York
import Dominion
import random
from collections import defaultdict

# function for defining player names, can be changed to prompt user later
def define_player_names():
    player_names = ["Annie","*Ben","*Carla"]
    return player_names

# function for calculating the number of victory point cards that will be in
#   the game based on the number of players
def calculate_nV(player_names):
    if len(player_names)>2:
        return 12
    else:
        return 8

# function that calculates the number of curse cards in the game based on the
#   number of players
def calculate_nC(player_names):
    return -10 + 10 * len(player_names)

# creates the box variable. This holds all of the cards that can possibly be
#   put into a game. This does not include treasure, curse, or victory points
def create_box(player_names):
    nV = calculate_nV(player_names)
    box = {}
    box["Woodcutter"]=[Dominion.Woodcutter()]*10
    box["Smithy"]=[Dominion.Smithy()]*10
    box["Laboratory"]=[Dominion.Laboratory()]*10
    box["Village"]=[Dominion.Village()]*10
    box["Festival"]=[Dominion.Festival()]*10
    box["Market"]=[Dominion.Market()]*10
    box["Chancellor"]=[Dominion.Chancellor()]*10
    box["Workshop"]=[Dominion.Workshop()]*10
    box["Moneylender"]=[Dominion.Moneylender()]*10
    box["Chapel"]=[Dominion.Chapel()]*10
    box["Cellar"]=[Dominion.Cellar()]*10
    box["Remodel"]=[Dominion.Remodel()]*10
    box["Adventurer"]=[Dominion.Adventurer()]*10
    box["Feast"]=[Dominion.Feast()]*10
    box["Mine"]=[Dominion.Mine()]*10
    box["Library"]=[Dominion.Library()]*10
    box["Gardens"]=[Dominion.Gardens()]*nV
    box["Moat"]=[Dominion.Moat()]*10
    box["Council Room"]=[Dominion.Council_Room()]*10
    box["Witch"]=[Dominion.Witch()]*10
    box["Bureaucrat"]=[Dominion.Bureaucrat()]*10
    box["Militia"]=[Dominion.Militia()]*10
    box["Spy"]=[Dominion.Spy()]*10
    box["Thief"]=[Dominion.Thief()]*10
    box["Throne Room"]=[Dominion.Throne_Room()]*10
    return box

# function that defines the supply order (the order the cards appear based on
#   their cost)
def define_supply_order():
    return      {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
                3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                6:['Gold','Adventurer'],8:['Province']}

# Randomly pulls 10 different card stacks from the box to use in the game.
#   the value returned becomes the supply
def pull_cards_from_box(box):
    boxlist = [k for k in box]
    random.shuffle(boxlist)
    random10 = boxlist[:10]
    return defaultdict(list,[(k,box[k]) for k in random10])

# Adds the standard treasure, victory point, and curse cards to the supply
def add_standard_treasure_vp_curses(supply, player_names):
    nV = calculate_nV(player_names)
    nC = calculate_nC(player_names)
    # add the treasure
    supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
    supply["Silver"]=[Dominion.Silver()]*40
    supply["Gold"]=[Dominion.Gold()]*30
    # add the victory points
    supply["Estate"]=[Dominion.Estate()]*nV
    supply["Duchy"]=[Dominion.Duchy()]*nV
    supply["Province"]=[Dominion.Province()]*nV
    # add the curses
    supply["Curse"]=[Dominion.Curse()]*nC

# Creates the player objects so they can be used to play the game
def construct_players(player_names):
    players = []
    for name in player_names:
        if name[0]=="*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0]=="^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))
    return players

