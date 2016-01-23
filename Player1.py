#Player.py

class Player (object):

    def __init__ (self, first, last):
        """The constructor for a player."""
        self.first = first
        self.last = last
        self.rating = 0
        self.info = []
        

    def update (self, team, year, pts, reb, asts, stl, blk, fga, fgm, fta, \
                ftm, turnover, gp, penalties):
        '''create a list of this year's information and calculate an efficiency 
        rating for this year (call effcalc). Append this information onto his
        info list (self.info). Then call a function to calculate his total
        efficiency rating (totalEffCalc).'''   
        
        infolist = [year, team, pts, reb, asts, stl, blk, fga, fgm,\
                           fta, ftm, turnover, gp, penalties]
        x = self.effcalc(infolist)
        
        infolist.append(x)
        
        self.info.append(infolist)
        
        self.totalEffCalc()


    def effcalc (self,infoList):
        
        '''calculate one year's efficiency rating'''
        
        
        inf = (((infoList[2] + infoList[3] + infoList[4] + \
                  infoList[5]+ infoList[6])\
                 - ((infoList[7] - infoList[8]) + (infoList[9]\
                    - infoList[10]) + infoList[11])) /\
                infoList[12])
        if inf > 0:
            inf = inf**(.75)
        return float(inf)
        

    def totalEffCalc(self):
        '''calculate his total efficiency rating'''
        eff = 0.0
        counter = 0
        for lst in self.info:
            
            eff = eff + lst[14]
            counter += 1
    
        totaleff = eff / counter    
        self.rating = totaleff
        
                               
            
    def getEfficiency(self):
        '''return player's efficiency'''
        
        return self.rating

    def returnName(self):
        """Returns the name of the player in first last format."""
        myName = self.first + " " + self.last
        return myName


    def returnReverseName(self):
        """Returns the name of the player in last, first format."""
        myName = self.last + " " + self.first
        return myName


    def __eq__ (self, other):
        """Determines if this person's name is the same as the other's."""
        otherName = other.returnReverseName()
        myName = self.returnReverseName()
        if otherName == myName:
            return True
        else:
            return False


    def __lt__(self,other):
        """Determines if this person's name is less than the other person's
        name alphabetically"""
        otherName = other.returnReverseName()
        myName = self.returnReverseName()
        if myName < otherName:
            return True
        else:
            return False


    def __gt__ (self, other):
        """Determines if this person's name is greater than the other person's
        name alphabetically"""        
        otherName = other.returnReverseName()
        myName = self.returnReverseName()
        if myName > otherName:
            return True
        else:
            return False


    def __str__(self):
        """Returns a string of the person's name and their rating in a nice
        format."""
        return "%s %s" %(self.first + " " + self.last, self.rating)



    def printInfo(self):
        """Prints individual year information about this player including each 
        year's passer rating. The list is in year order."""
        informationList = []
        length = len(self.info)
        for i in range(length):
            year = self.info[i][0]
            team = self.info[i][1]
            efficiency = self.effcalc(self.info[i])
            # Calc is called to determine each individual yearly rating.
            informationList.append([year, team, efficiency])
            
        informationList.sort()
        name = self.returnName()
        for i in range(length):
            #print(name)
            print("%-15s %1s %5s %10s %2s %1s %6.2f" %\
                  (name, "in", informationList[i][0], "played for", \
                   informationList[i][1], "-", informationList[i][2]))
                  
            
        return
