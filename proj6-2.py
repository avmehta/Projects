
# Proj6.py

#from player import Player
from Player1 import Player

# ------------------------------------------------------------------------------
# This portion of the code defines the functions used in the main code that is
# further down. 

def generateDict(filename):
    """This function takes a given file and extracts information. It then uses 
    this information to generate a dictionary, with the player's name as the 
    key and corresponding Player object as its definition."""
    
    inputFile = open(filename, 'r', encoding = "windows-1252")
    playerLine = inputFile.readline()
   
    # The first line of the code is purely headers and must be discarded.
    playerDict = {} 
    
    for playerLine in inputFile:

        
        playerInfo = playerLine.split(",")
        name = playerInfo[2] + " " + playerInfo[3]
        team = playerInfo[4]
        year = playerInfo[1]
        points = float(playerInfo[8])
        rebounds = float(playerInfo[11])
        assists = float(playerInfo[12])
        steals = float(playerInfo[13])
        blocks = float(playerInfo[14])
        fgattempted = float(playerInfo[17])
        fgmade = float(playerInfo[18])
        ftattempted = float(playerInfo[19])
        ftmade = float(playerInfo[20])
        turnovers = float(playerInfo[15])
        gamesplayed = float(playerInfo[6])
        penalties = float(playerInfo[16])
        

        if name not in playerDict:
            playerDict[name] = Player(playerInfo[2], playerInfo[3])

        playerDict[name].update(team, year, points, rebounds, assists, steals\
                                , blocks, fgattempted, fgmade, ftattempted, ftmade,\
                                turnovers, gamesplayed, penalties)
        # The update command belongs to the class Player: it takes the given
        # information and updates the Player object's information about itself,
        # automatically recalculating its associated overall career rating.
        

    inputFile.close()

    return playerDict


def generateList(playerDict):
    """This function serves two purposes. Firstly, it takes the previously
    created player dictionary and generates a list of Player objects. It sorts 
    this list such that the Players are organized in alphabetical order by 
    last name. Secondly, it prints a sorted list of players with efficiencies 
    greater than or equal to nine"""

    playerList = []
    length = len(playerDict)
    
    for element in playerDict:
        newPlayer = playerDict[element]
        playerList.append(newPlayer)
        
    playerList.sort()

    for i in range(length):
        name = playerList[i].returnName()
        rating = (playerList[i].getEfficiency())
        
        if rating >= 9.00:
            #rating = playerList[i].getEfficiency()
            print("%-20s %s %7.2f" % (name, "rating:", rating))
        
        
    print()
            
    return

# ------------------------------------------------------------------------------

playerDict = generateDict('bball.csv')
generateList(playerDict)
# First a dictionary of Players is created using a function.
# Then a list of players is printed in alphabetical order, also via a function.

userInput = input("Do you want information about a particular player: ")
print(userInput)
print()
userInput = userInput.lower()

while userInput == 'y':
# If the user enters anything but 'Y' or 'y', the program will terminate.
    
    requestedPlayer = input("Enter player's name: ")
    print(requestedPlayer)
    print()
    
    if requestedPlayer in playerDict:
    # This statement serves to check whether or not the player name exists
    # in the dictionary. If it does not, the else statement below states so.
        
        print("Pick one")
        print("a) Overall player rating")
        print("b) Individual years and ratings")
        print()
        letterChoice = input("Enter choice: ")
        print(letterChoice)
        letterChoice = letterChoice.lower()
        print()
        
        if letterChoice == 'a':
            # If choice A is chosen, the player name and his 
            rating = playerDict[requestedPlayer].getEfficiency()
            print("%-16s %s %5.2f" % (requestedPlayer, "rating:", rating))
            
        elif letterChoice == 'b':
            # If choice B is chosen, the player's career information is listed
            # by year, with each incident's rating reported separately.
            playerDict[requestedPlayer].printInfo()
        else: 
            # If anything else is chosen, the program states it is illegal.
            print("You've entered an illegal choice")
    
    else:
        print("This player is not in the system.")

    print()
    userInput = input("Do you want information about another player: ")
    print(userInput)
    print()
    
    userInput = userInput.lower()
