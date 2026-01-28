# imports
from ast import Break, In
import os

import ast

# variable that stores if admin mode is currently enabled
global AdminMode
AdminMode = False


# stores the value (object data) and key (team/individual/event) in a table to be referenced later
global TeamDict
global TeamEventDict
global IndividualDict
global IndividualEventDict

TeamDict = {}
TeamEventDict = {}
IndividualDict = {}
IndividualEventDict = {}

# a list of files that allows a function later to easily load data into the dictionaries from their corresponding files
global TeamFileList
global TeamEventFileList
global IndividualFileList
global IndividualEventFileList

TeamFileList = []
TeamEventFileList = []
IndividualFileList = []
IndividualEventFileList = []


# class to create and manipulate an event
class Event():
    def __init__(self, IsTeamEvent, EventName):
        self.IsTeamEvent = IsTeamEvent
        self.EventName = EventName
    
    def SaveToFile(self, IsTeamEvent):
        file = open(f"{self.EventName}.txt", "w")
        file.write(f"{self.IsTeamEvent}%{self.EventName}")
        file.close()

        if IsTeamEvent:
            self.TeamSave()
        else:
            self.IndividualSave()

    def TeamSave(self):
        TeamEventFileList.append(f"{self.EventName}.txt")
        SaveFileLists()
    
    def IndividualSave(self):
        IndividualEventFileList.append(f"{self.EventName}.txt")
        SaveFileLists()

    def DeleteSelf(self, EventName, IsTeamEvent):
        
        # remove the file
        os.remove(f"{self.EventName}".txt)
        
        # remove from the dictionary and file list
        if IsTeamEvent:
            TeamEventDict.pop(f"{EventName}")
            TeamEventFileList.remove(f"{EventName}.txt")
        else:
            IndividualEventDict.pop(f"{EventName}")
            IndividualEventFileList.remove(f"{EventName}.txt")

    def ReturnEventDetails(self):
        return self.EventName
        


class Team():
    def __init__(self, TeamName, Points, Member1, Member2, Member3, Member4, Member5):
        self.TeamName = TeamName
        self.Points = int(Points)
        self.Member1 = Member1
        self.Member2 = Member2
        self.Member3 = Member3
        self.Member4 = Member4
        self.Member5 = Member5
    
    def DeleteSelf(self):
        
        # remove the file
        os.remove(f"{self.EventName}.txt")

        # remove from dictionary and file list
        TeamDict.pop(f"{self.TeamName}")
        TeamFileList.remove(f"{self.TeamName}.txt")
    
    def SaveToFile(self):
        
        # save data to a file
        file = open(f"{self.TeamName}.txt", "w")
        file.write(f"{self.TeamName}%{self.Points}%{self.Member1}%{self.Member2}%{self.Member3}%{self.Member4}%{self.Member5}")
        file.close()
        
        # append file name to the list of files
        if (f"{self.TeamName}.txt") not in TeamFileList:
            TeamFileList.append(f"{self.TeamName}.txt")
            
        SaveFileLists()
        
    def PrintData(self):
        print(f"Team name: {self.TeamName}")
        print(f"Member 1: {self.Member1}")
        print(f"Member 2: {self.Member2}")
        print(f"Member 3: {self.Member3}")
        print(f"Member 4: {self.Member4}")
        print(f"Member 5: {self.Member5}")
        print(f"Current point count: {self.Points}")
        print("")
        print("============================")
        print("")
        
    def AddPoints(self, PointsAdded):
        # add the points
        self.Points += int(PointsAdded)
        
        # save the change
        self.SaveToFile()
        
    def ReturnName(self):
        return self.TeamName
        


class Individual():
    def __init__(self, Name, Points):
        self.Name = Name
        self.Points = int(Points)
        

    def DeleteSelf(self):
        
        # remove the file
        os.remove(f"{self.Name}.txt")
        
        # remove from dictionary and file list
        IndividualDict.pop(f"{self.Name}")
        IndividualFileList.remove(f"{self.Name}.txt")

    
    def SaveToFile(self):
        
        # save data to a file
        file = open(f"{self.Name}.txt", "w")
        file.write(f"{self.Name}%{self.Points}")
        file.close()
        
        # append file name to the list of files
        IndividualFileList.append(f"{self.Name}.txt")
        SaveFileLists()
        
    def AddPoints(self, PointsAdded):
        # add the points
        self.Points += int(PointsAdded)
        
        # save the change
        self.SaveToFile()
        
    def ReturnName(self):
        return self.Name
    
    def PrintData(self):
        print("")
        print(f"{self.Name} - {self.Points}")
        print("============================")
    



def PrintTeams():
    for Team in TeamDict:
        TeamDict[Team].PrintData()


def PrintIndividuals():
    for Individual in IndividualDict:
        IndividualDict[Individual].PrintData()


def CreateTeam():
    if len(TeamDict) > 3:
        print("")
        print("Team limit reached! (4 teams)")
        print("")
        
    else:
        # gather inputs
        TeamName = input("Enter team name: ")
        Member1 = input("Enter the name of member 1: ")
        Member2 = input("Enter the name of member 2: ")
        Member3 = input("Enter the name of member 3: ")
        Member4 = input("Enter the name of member 4: ")
        Member5 = input("Enter the name of member 5: ")
        print("")
        Points = 0
    
        # create the dictionary entry with the object and save it to a file
        TeamDict[TeamName] = Team(TeamName, Points, Member1, Member2, Member3, Member4, Member5)
        TeamDict[TeamName].SaveToFile()
    
        SaveFileLists()

def CreateIndividual():
    if len(IndividualDict) >= 20:
        print("")
        print("Individual competitor limit reached (20 individuals)")
        print("")

    else:
        Name = input("Enter competitor name: ")
        IndividualDict[Name] = Individual(Name = Name, Points = 0)
        IndividualDict[Name].SaveToFile()
    
        # update file lists
        SaveFileLists()

def CreateEvent(IsTeamEvent):
    # gather inputs
    EventName = input("Enter the name of the event: ")
    
    # save to the correct dictionary based on event type
    if IsTeamEvent:
        TeamEventDict[EventName] = Event(EventName = EventName, IsTeamEvent = True)
        TeamEventDict[EventName].SaveToFile(True)
    else:
        IndividualEventDict[EventName] = Event(EventName = EventName, IsTeamEvent = False)
        IndividualEventDict[EventName].SaveToFile(False)
    
    # update file lists
    SaveFileLists()
        
def RunEvent():
    # gather input
    IsTeamEvent = input("Is this a team event? (Y/N)")
    if IsTeamEvent == "Y" and len(TeamDict) != 4:
        print("")
        print("To run a team event you must have 4 teams!")
        print("")
        return
    elif IsTeamEvent == "N" and len(IndividualDict) != 20:
        print("")
        print("To run an individual event you must have 20 people!")
        print("")
        return
        
    if len(TeamEventDict) == 0 and IsTeamEvent == "Y":
        print("")
        print("There are no team events!")
        print("")
        return
    elif len(IndividualEventDict) == 0 and IsTeamEvent == "N":
        print("")
        print("There are no individual events!")
        print("")
        return
 
    # initialise the necessary variables
    EventCount = 0
    
    MaxPoints = 200
    TeamIncrement = 50
    IndividualIncrement = 10
    
    CurrentPoints = MaxPoints
    
    # dictionary to store the value of each event with the number associated with it in the menu
    EventMenuDict = {}
    
    # list to store the number and placement so the user cant select the same one twice
    BeenPlacedList = [0]
    
    if IsTeamEvent == "Y":
        for TeamEvent in TeamEventDict.values():
            
            # increment EventCount and set it to be the dictionary key for the event
            EventCount += 1
            EventMenuDict[EventCount] = TeamEvent

            EventName = TeamEvent.ReturnEventDetails()
       
            # print the event names
            print("")
            print(f"{str(EventCount)}. {EventName}")
            print("")
        
        # user inputs desired event number and validates it
        ChosenEventNum = int(input("Enter an event to run from the list: ")) 
            
        # gets the selected event from where it was stored in the dictionary earlier
        ChosenEvent = EventMenuDict[ChosenEventNum]
        

        # calculate placements in the scoring

        # remade team dict to store key as integer not name
        TeamDictIntKey = {}
        Key = 0

        for Value in TeamDict.values():
            Key += 1
            TeamDictIntKey[Key] = Value
           
        
        # print the menu
        for Num in range(1,5):

            TeamName = TeamDictIntKey[Num].ReturnName()    

            print("")
            print(f"{Num}. {TeamName}")
            print("")
            
        # gather team placement inputs
        for Placement in range(1,5):
            
            TeamInput = int(input(f"Enter the teams number that came in {Placement}{OrdinalSuffix(Placement)}: "))
            
            while not ValidMenuInput(4, TeamInput):
                TeamInput = int(input(f"INVALID INPUT - Enter the teams number that came in {Placement}{OrdinalSuffix(Placement)}: "))
                
            while TeamInput in BeenPlacedList:
                TeamInput = int(input(f"ALREADY PLACED - Enter the teams number that came in {Placement}{OrdinalSuffix(Placement)}: "))
                
            BeenPlacedList.append(TeamInput)

            TeamSelected = TeamDictIntKey[TeamInput]
            
            TeamSelected.AddPoints(CurrentPoints)
            
            CurrentPoints -= TeamIncrement


      
    # same thing except for individual events
    else:
        for IndividualEvent in IndividualEventDict.values():
            
            # increment EventCount and set it to be the dictionary key for the event
            EventCount += 1
            EventMenuDict[EventCount] = IndividualEvent

            EventName = IndividualEvent.ReturnEventDetails()
       
            # print the event names
            print("")
            print(f"{str(EventCount)}. {EventName}")
            print("")
        
        # user inputs desired event number and validates it
        ChosenEventNum = int(input("Enter an event to run from the list: ")) 
            
        # gets the selected event from where it was stored in the dictionary earlier
        ChosenEvent = EventMenuDict[ChosenEventNum]
        

        # calculate placements in the scoring

        # remade team dict to store key as integer not name
        IndividualDictIntKey = {}
        Key = 0

        for Value in IndividualDict.values():
            Key += 1
            IndividualDictIntKey[Key] = Value
           
        
        # print the menu
        for Num in range(1,21):

            IndividualName = IndividualDictIntKey[Num].ReturnName()    

            print("")
            print(f"{Num}. {IndividualName}")
            print("")
            
        # gather team placement inputs
        for Placement in range(1,21):   
            IndividualInput = int(input(f"Enter the individuals number that came in {Placement}{OrdinalSuffix(Placement)}: "))
            
            while not ValidMenuInput(20, IndividualInput):
                TeamInput = int(input(f"INVALID INPUT - Enter the individuals number that came in {Placement}{OrdinalSuffix(Placement)}: "))
                
            while IndividualInput in BeenPlacedList:
                IndividualInput = int(input(f"ALREADY PLACED - Enter the individuals number that came in {Placement}{OrdinalSuffix(Placement)}: "))
                
            BeenPlacedList.append(IndividualInput)

            IndividualSelected = IndividualDictIntKey[IndividualInput]
            
            IndividualSelected.AddPoints(CurrentPoints)
            
            CurrentPoints -= IndividualIncrement


    # update file lists        
    SaveFileLists()



def OrdinalSuffix(Num):
    if Num > 3:
        return "th"
    elif Num == 3:
        return "rd"
    elif Num == 2:
        return "nd"
    elif Num == 1:
        return "st"
    else:
        return "(SUFFIX UNKNOWN)"


# gathers user input and validates it
def GatherEventMenuInput(EventCount):
    ChosenEventNum = int(input("Please enter choice from the menu: "))
    
    while not ValidMenuInput(EventCount-1, ChosenEventNum):
        ChosenEventNum = int(input("INVALID INPUT - Please enter choice from the menu: "))
        
    return ChosenEventNum

# function to check if the user is an admin or not using the password
def CheckAdmin():
    AdminPassword = "Godalming123"
    if input("Please enter admin password: ") == AdminPassword:
        print("")
        print("Admin password accepted!")
        print("")
        return True
    else:
        print("")
        print("Admin password denied!")
        print("")
        return False
    

# on startup, this function will re-make any objects using the files stored
def RemakeObjects():

    LoadFileLists()
    
    try:
        for TeamFile in TeamFileList:
        
            # open a file, read it, then close it
            file = open(TeamFile, "r")
            TeamDataList = (file.read()).split("%")
            file.close()
        
            # extract data from list
            TeamName = TeamDataList[0]
            Points = TeamDataList[1]
            Member1 = TeamDataList[2]
            Member2 = TeamDataList[3]
            Member3 = TeamDataList[4]
            Member4 = TeamDataList[5]
            Member5 = TeamDataList[6]  

            # create the dictionary key and value
            TeamDict[TeamName] = Team(TeamName, Points, Member1, Member2, Member3, Member4, Member5)
    except:
        pass
    
    try:
        for TeamEvent in TeamEventFileList:
            # open a file, read it, then close it
            file = open(TeamEvent, "r")
            TeamEventDataList = (file.read()).split("%")
            file.close()
        
            # extract data from list
            IsTeamEvent = TeamEventDataList[0]
            EventName = TeamEventDataList[1]

            # create the dictionary key and value
            TeamEventDict[EventName] = Event(bool(IsTeamEvent), EventName)
    except:
        pass
        
    try:
        for IndividualFile in IndividualFileList:
            # open a file, read it, then close it
            file = open(IndividualFile, "r")
            IndividualDataList = (file.read()).split("%")
            file.close()
        
            # extract data from list
            Name = IndividualDataList[0]
            Points = IndividualDataList[1]
        
            # create the dictionary key and value
            IndividualDict[Name] = Individual(Name, Points)
    except:
        pass
        
    try:
        for IndividualEvent in IndividualEventFileList:
            # open a file, read it, then close it
            file = open(IndividualEvent, "r")
            IndividualEventDataList = (file.read()).split("%")
            file.close()
        
            # extract data from list
            IsTeamEvent = TeamEventDataList[0]
            EventName = TeamEventDataList[1]
        
            # create the dictionary key and value
            IndividualEventDict[EventName] = Event(bool(IsTeamEvent), EventName)
    except:
        pass
        
        
        
        
# on startup load the files (if one cant be loaded for whatever reason, its skipped to now cause an error)
def LoadFileLists():
    
    global TeamFileList
    global TeamEventFileList
    global IndividualFileList
    global IndividualEventFileList

    try:
        # Load team file list
        file = open("TeamFileList.txt", "r")
        TeamFileList = ast.literal_eval(file.read())
        file.close()
    except:
        TeamFileList = []
    
    try:
        # Load team event file list
        file = open("TeamEventFileList.txt", "r")
        TeamEventFileList = ast.literal_eval(file.read())
        file.close()
    except:
        TeamEventFileList = []
    
    try:
        # Load individual file list
        file = open("IndividualFileList.txt", "r")
        IndividualFileList = ast.literal_eval(file.read())
        file.close()
    except:
        IndividualFileList = []
      
    try:
        # Load individual event file list
        file = open("IndividualEventFileList.txt", "r")
        IndividualEventFileList = ast.literal_eval(file.read())
        file.close()
    except:
        IndividualEventFileList = []

    

# save the files whenever a change is made
def SaveFileLists():
    # Save team file list
    file = open("TeamFileList.txt", "w")
    file.write(f"{TeamFileList}")
    file.close()
    
    # Save team event file list
    file = open("TeamEventFileList.txt", "w")
    file.write(f"{TeamEventFileList}")
    file.close()
    
    # Save individual file list
    file = open("IndividualFileList.txt", "w")
    file.write(f"{IndividualFileList}")
    file.close()
    
    # Save individual event file list
    file = open("IndividualEventFileList.txt", "w")
    file.write(f"{IndividualEventFileList}")
    file.close()



# main loop for the user to select functions from the menu
def MainMenu():
    # check if "AdminMode" is enabled, deciding if the user can access advanced controls
    AdminMode = False

    while True:

        if not AdminMode:
            print("1. View Team Scores")
            print("2. View Individual Scores")
            print("==========================")
            print("3. Admin Mode")
            print("==========================")
            print("4. Exit")
            print("")
        
            UserInput = input("Please make a selection from the list: ")
            while not ValidMenuInput(4, UserInput):
                UserInput = input(f"Invalid input: must be integer between 1 and 4: ")
            
            if UserInput == "1":
                if len(TeamDict) == 0:
                    print("")
                    print("There are no teams!")
                    print("")
                else:
                    PrintTeams()
            
            elif UserInput == "2":
                if len(IndividualDict) == 0:
                    print("")
                    print("There are no individual competitors!")
                    print("")
                else:
                    PrintIndividuals()
            
            elif UserInput == "3":
                AdminMode = CheckAdmin()

            elif UserInput == "4":
                SaveFileLists()
                exit()
        
            

        else:
            print("1. View Team Scores")
            print("2. View Individual Scores")
            print("==========================")
            print("3. Enter Team")
            print("4. Enter Individual")
            print("==========================")
            print("5. Add Team Event")
            print("6. Add Individual Event")
            print("==========================")
            print("7. Run Event")
            print("==========================")
            print("8. Exit")
            print("")
        
            UserInput = input("Please make a selection from the list: ")
            while not ValidMenuInput(8, UserInput):
                UserInput = input(f"Invalid input: must be integer between 1 and 8: ")
        
            if UserInput == "1":
                if len(TeamDict) == 0:
                    print("")
                    print("There are no teams!")
                    print("")
                else:
                    PrintTeams()
            
            elif UserInput == "2":
                if len(IndividualDict) == 0:
                    print("")
                    print("There are no individual competitors!")
                    print("")
                else:
                    PrintIndividuals()
            
            elif UserInput == "3":
                CreateTeam()
            
            elif UserInput == "4":
                CreateIndividual()
            
            elif UserInput == "5":
                CreateEvent(True)
            
            elif UserInput == "6":
                CreateEvent(False)
            
            elif UserInput == "7":
                RunEvent()

            elif UserInput == "8":
                SaveFileLists()
                exit()
   
def ValidMenuInput(MenuMaxInt, UserInput):
    # Integer Type Check
    try:
        UserInput = int(UserInput)
    except:
        return False
    
    # Range Check
    if UserInput >= 1 and UserInput <= MenuMaxInt:
        return True
    else:
        return False

# main code that runs on startup

RemakeObjects()

MainMenu()