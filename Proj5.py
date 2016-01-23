# Proj5.py
# Project 5, Fall 2014
# Coded by: Stephen Daniel(703-470-4809), Avi Mehta (571-244-9355)
#           sdaniel@email.wm.edu        , avmehta@email.wm.edu
# 


# The purpose of this program is to sort through football data provided in the 
# form of a CSV file and then provide users with the information they are 
# seeking. The program will first display a menu asking the user what they are 
# looking for. If they choose A, it will prompt them for the name of a rusher, 
# then print his career information and overall rating. If they select B, it 
# will prompt for a team's initials, find the team, and then print all of the 
# rushers associated by year. If C is chosen, a list of players and their 
# overall ratings will be printing in alphabetical order. Selecting Q will 
# cause the program to quit. Every choice inputed by the option will call to a
#helper function that is defined before the main code.

import csv

# ------------------------------------------------------------------------------
# This portion of the code defines several functions that are used in the main 
# code at the bottom of this file.

def getPlayersAndTeams(fileName, teamNames):
    """Given the file name and the dictionary of teamNames, this function will 
    return a dictionary of players (with year, team, and rating in a list as 
    the value) and a dictionary of the team (with player name, year, and rating 
    in a list as the value)."""
    
    inputFile = open(fileName, 'r')
    wasteLine = inputFile.readline()
    
    # Two dictionaries are created and to be returned later.
    players = {}    
    teams = {}
    teamstats = {}
    playerLine = inputFile.readline()    
    
    while playerLine != "":
        playerLine = playerLine.strip()
        playerInfo = playerLine.split(",")
        name = playerInfo[0] + " " + playerInfo[1]
        attempts = float(playerInfo[5])
        yards = float(playerInfo[6])
        touchdowns = float(playerInfo[7])
        fumbles = float(playerInfo[10])
        rating = rusher_rating(yards, attempts, touchdowns, \
                           fumbles)
        year = playerInfo[13]
        team = playerInfo[3]
        playerInformation = (yards, attempts, touchdowns, fumbles)
        playerTuple = (year, team, rating)
        teamTuple = (year, name, rating)
        
        if name not in players:
            players[name] = []  
            
        if team not in teams:
            teams[team] = []  
            
        if team not in teamstats:
            teamstats[team] = []
            
        teamstats[team].append(playerInformation)
        teams[team].append(teamTuple)   
        players[name].append(playerTuple)
        playerLine = inputFile.readline()
        
    inputFile.close()
    
    # The dictionaries are returned in the form of a list.
    return [players, teams, teamstats]

def getOverallRatings(fileName):
    """Given the csv file name, this function will create a list and a 
    dictionary of players with their overall career ratings."""
    
    inputFile = open("rushers.csv", 'r')
    wasteLine = inputFile.readline()
    alphaList = []
    playerLine = inputFile.readline()
    
    while playerLine != "":
        playerLine = playerLine.strip()
        playerInfo = playerLine.split(",")
        name = playerInfo[1] + ", " + playerInfo[0]
        dictName = playerInfo[0] + " " + playerInfo[1]
        attempts = float(playerInfo[5])
        yards = float(playerInfo[6])
        touchdowns = float(playerInfo[7])
        fumbles = float(playerInfo[10])
        year = playerInfo[13]
        team = playerInfo[3]
        neededInfo = [name, attempts, yards, touchdowns, \
                      fumbles, dictName]
        alphaList.append(neededInfo)
        playerLine = inputFile.readline()
        
    inputFile.close()
    alphaList.sort()
    
    # A list and dictionary are created for return at the end of the function.
    ratingsList = []
    ratingsDict = {}
    
    # Something must be attached to the end of alphaList in order for the loop 
    # structure to determine that the end has been reached.    
    #alphaList.append("X")
    for element in alphaList: 
        if element[1] != 0:
            attempts = float(element[1])
            yards = float(element[2])
            touchdowns = float(element[3])
            fumbles = float(element[4])
            name = alphaList[alphaList.index(element) + 1][0]
            
            while(element[0] == name):
                indexNumber = alphaList.index(element)
                attempts += float(alphaList[indexNumber + 1][1])
                yards += float(alphaList[indexNumber + 1][2])
                touchdowns += float(alphaList[indexNumber + 1][3])
                fumbles += float(alphaList[indexNumber + 1][4])
                alphaList.pop(indexNumber + 1)
                #name = alphaList[indexNumber + 1][0]
                name = alphaList[1][0]
                
            totalRating = rusher_rating(yards, attempts, touchdowns, \
                                    fumbles)
            name = alphaList[alphaList.index(element)][0]
            ratingsList.append([name, totalRating])
            dictName = alphaList[alphaList.index(element)][5]
            ratingsDict[dictName] = totalRating
            
    # The list and dictionary are returned in the form of a list.    
    return [ratingsList, ratingsDict]
   
def rusher_rating(yards, att, td, fumbles):
    ''''''  
    if att != 0:
        avgYards = float(yards) / (4.05 * float(att))
        
        if avgYards > 2.375:
            avgYards = 2.375
        perTDs = (float(td)*39.5) / float(att) 
        
        if perTDs > 2.375:
            perTDs = 2.375            
        perFumbles = (2.375 - ((21.5 * float(fumbles)) / float(att)))
        
    else:
        avgYards = 0
        perTDs = 0
        perFumbles = 0
        
    rating = (avgYards + perTDs + perFumbles) * 100 / 4.5
                  
    return rating

def choice_a(players):
    requestedName = input("Enter the player's firstname lastname: ")
    print(requestedName)
    print()
    
    # If the player is not in the dictionary, this error will appear.
    if requestedName not in players:
        print("This person is not in the database.")
        
    else:
        print(requestedName)
        playerInfo = players[requestedName]
        playerInfo.sort()
        length = len(playerInfo)
        
        for i in range(length):
            year = playerInfo[i][0]
            team = teamNames[playerInfo[i][1]]
            rating = float(round(playerInfo[i][2],2))
            print("    played for %-10s %5s %-4s with a rating of %7.2f"\
                    % (team, "in", year, rating))
            
        overallRating = float(round(ratingsDict[requestedName],2))
        print(requestedName, "has an overall rating of", overallRating)
            
        
def choice_b(teams):
    initials = input("Enter team initials: ")
    print(initials)
    print()
    initials = initials.upper()
    yards = 0
    fumbles = 0
    touchdowns = 0 
    attempts = 0 
    
    # If the team initials are not found, this message will appear:
    if initials not in teamNames:
        print("This team is not in the database.")
        
    else:
        teamName = teamNames[initials]
        print(teamName)
        teamInfo = teams[initials]
        teamInfo.sort()
        teamStat = teamstats[initials]
        teamStat.sort()
        lengthstat = len(teamStat)
        length = len(teamInfo)
        
        for i in range(length):
            year = teamInfo[i][0]
            player = teamInfo[i][1]
            rating = float(round(teamInfo[i][2],2))
            if rating != 0.0:
                print("     %-20s %-5s %10.2f" % (player, year, rating))    
                
        #overallRating = str(round(ratingsDict[teams],2))
        for i in range(lengthstat):
            if teamStat[i][1] > 0:
                yards = yards + teamStat[i][0]
                attempts = attempts + teamStat[i][1]
                touchdowns = touchdowns + teamStat[i][2]
                fumbles = fumbles + teamStat[i][3]
        team_rating = rusher_rating(yards, attempts, touchdowns, fumbles)
            
        print("The overall team rating for these 2 years is: %3.2f" %(team_rating))
        
def choice_c(ratingsList):
    
    length = len(ratingsList)
    
    for i in range(length):
        name = ratingsList[i][0]
        totalRating = ratingsList[i][1]
        print("%-25s %8.2f"%(name,totalRating))
    
# ------------------------------------------------------------------------------
# This portion of the code deals with all user input and prints requested 
# information when prompted.

# Important lists and dictionaries are first defined/created:
teamNames = \
{'MIA': 'Miami', 'NO':'New Orleans', 'STL':'St. Louis','NE':'New England',\
'SD':'San Diego','HOU':'Houston','MIN':'Minnesota','IND':'Indianapolis',\
'TEN':'Tennessee','OAK':'Oakland','ARI':'Arizona','KC':'Kansas City',\
'SF':'San Francisco','GB':'Green Bay','DAL':'Dallas','DET':'Detroit',\
'BAL':'Baltimore','CLE':'Cleveland','CIN':'Cincinnati','WAS':'Washington',\
'DEN':'Denver','NYG':'New York Giants','NYJ':'New York Jets','SEA':'Seattle',\
'ATL':'Atlanta', 'CAR':'Carolina','PHI':'Philadelphia','BUF':'Buffalo',\
'CHI':'Chicago','TB':'Tampa Bay',  'PIT':'Pittsburgh','JAX':'Jacksonville'}

# These two functions will return lists comprised of lists and dictionaries.
playersAndTeams = getPlayersAndTeams("rushers.csv", teamNames)
ratingInfo = getOverallRatings(".csv")

# Here the code extracts the list/dictionary needed from the above.
players = playersAndTeams[0]
teams = playersAndTeams[1]
teamstats = playersAndTeams[2]
ratingsList = ratingInfo[0]
ratingsDict = ratingInfo[1]

    
# Start menu loop
choice = ''
    
while choice != 'q':
    
    print("\nMenu choices")
    print("a) Find a rusher and print his career information and overall \
rating.")
    print("b) Find a team and print all the rushers by year.")
    print("c) Print a list of players and their ratings in alpha order.")
    print("q) Quit")
    choice = input("\nEnter choice: ")
    print(choice, "\n")
    choice = choice.lower()
        
    if choice == 'a':
        choice_a(players)
        
    elif choice == 'b':
        choice_b(teams)
        
    elif choice == 'c':
        choice_c(ratingsList)
        
    elif choice == 'q':
        pass
    
    else:
        print("Illegal choice. Try again.")
            
            
print("Thanks for playing.")

