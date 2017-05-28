# -*- coding: utf-8 -*-
"""
A class scheduler that will schedule classes without overlaps
User will enter class information, program will warn if overlaps occur 

@author Cameron Zurmuhl, zurmuhlc@lafayette.edu
@version 1.0
"""
  
#%% The main part of the script that runs the program
# The user will intereact with a menu-driven interface to add their classes
import os
import csv
import time
from Class import Class
from Day import Day

classes = [] #ongoing list of classes
classStringList = [] #classes formated for CSV output

def properMenuChoice(classIndex):
    """
    Method properMenuChoice returns whether the user entered a valid option for the menu
    
    :type classIndex: String
    :param classIndex: The user's menu choice as a letter
    :returns: a boolean whether the user chose a valid choice 
    
    """
    if not classIndex.isdigit():
        print ("'", classIndex, "' needs to be a number corresponding to a class entry\n")
        return False
    if int(classIndex) < 1 or int(classIndex) > len(classes)+1:
        print ("'", classIndex, "' needs to be a number corresponding to a class entry\n")
        return False
    return True

def properTimeInput(time_):
    """
    Method properTimeInput returns whether the user entered a valid time
    
    :type time: String
    :param time: The user's entered time
    :returns: a boolean whether the user entered time in a valid format
    """
    if not time_.isdigit() or len(time_)>4 or int(time_) > 2400 or int(time_) < 0 or int(time_[2])>5:
        print("'",time_, "' is an invalid input for the time. Use 24 hr format.\nExamples: 8 a.m = 0800, 1 p.m = 1300, 2:30 = 1430, 12:50 a.m = 0050\n")
        return False
    return True

def properDayInput(day):
    """
    Method properDayInput returns whether the user erntered a valid day
    
    :type day: String
    :param day: The user's entered day
    :returns: a boolean whether the user entered time in a valid format
    """
    possibleStrings = ["m","mon","monday","tu","tue","tues","tuesday","w",
                      "we","wed","wednesday","th","tr","thu","thur","thurs","thursday","f","fr",
                      "fri","friday","sa","sat","saturday","su","sun","sunday"]
    
    validString = False
    for i in range(0, len(possibleStrings)):
        if possibleStrings[i] == day.lower():
            validString = True
    return validString

def displayClassList(showExtraOption):
    """
    Method displayClassList displays the ongoing list of classes, numbered 
    
    :type showExtraOption: boolean
    :param showExtraOption: Determines if an extra option "none" should be at the bottom of the list 
    """
    if len(classes) == 0:
        print("\nThere are no classes\n")
        delay()
        return
    print()
    outstr = "{0:<12}  {1:^18.5}  {2:>5}"
    print(outstr.format("  Class","Day","Time"))
    for i in range(0, len(classes), 1):
        print(str(i+1) + "." + " " + str(classes[i]))
    if(showExtraOption): #If True is passed to the function, the option for "None" will appear
        print(str(len(classes) + 1) + "." + " None")
    else:
        print()

def mainMenuChoice():
    """
    Method mainMenuChoice displays the main menu and records the user's choice of action
    
    :returns: The user's menu choice as a String
    """
    print("What would you like to do?")
    print("    n) Add a class")
    print("    d) Delete a class")
    print("    e) Edit a class")
    print("    s) Show ongoing list of classes")
    print("    p) Print Schedule to Terminal")
    print("    g) Generate schedule in csv and print to Terminal")
    print("    q) Save and Exit program\n")
    
    choice = input("Input choice here: ")
    
    if choice.lower() in ["n","d","e","s","g","q", "p"]:
        return choice
    else:
        print("\nPlease enter a valid menu choice")
        return None

def addClass():
    """
    Method add class takes user inputs and adds a class to the ongoing list of classes, sorted
    """
    print("\nEnter classes by day. For example enter all your Monday classes first, then Tuesday, etc.")
    print("When asked to put in class meeting times enter in 24 hr format. Example: 1:00 p.m = 1300 8:00 a.m = 0800")
    
    day = input("Day of Class: ")
    while not properDayInput(day): #While format is not correct, persist on getting the correct entry
        print("Please enter a day of the week")
        day = input("Day of Class: ")
        
    className = input("Name of Class: ")
    if className.strip() == "": #If user does not put in a field (or just a bunch of spaces)
        className = "EMPTY ENTRY!"
        
    startTime = input("Starting Time: ")
    while not properTimeInput(startTime):
        startTime = input("StartingTime: ")
        
    endTime = input("Ending Time: ")
    while not properTimeInput(endTime):
        endTime = input("Ending Time: ")
    
    class_ = Class(className, Day(day), startTime, endTime) #Creating class object from user's entries
    for i in range (0, len(classes),1): #Checking for overlaping/duplicate classes
        classInList = classes[i]
        if(class_ == classInList):
            print("\nThere is a scheduling conflict with class: " + str(classInList) + " and " + str(class_))
            print("The class you just entered was not added to schedule. Please try another entry or edit an existing class\n")
            return #Break out of function
            
    classes.append(Class(className.upper(), Day(day), startTime, endTime))
    print("\nClass added to schedule")
    classes.sort()
    delay()
    clearTerminal()
    
def editClass():
    """
    Method edit class accepts user inputs to change fields of a user-selected class in the list
    """
    noChangesMade = True #Keeps track if changes were made at all
    displayClassList(True)
    if len(classes) == 0: #if no classes, return
        return
    
    print("\nWhich class would you like to edit?")
    classIndex = input("Choice: ")
    while not properMenuChoice(classIndex):
        classIndex = input("Choice: ")
    if int(classIndex) == len(classes) + 1: #If the user selected the "none" option from displayClassList
        return
    classIndex = int(classIndex)
        
    class_ = classes[classIndex-1]
    print("\nEnter the data for the class. Press <Enter/Return> to leave unchanged.")
        
    newClassDay = input("Enter new day for class: ")
    if(newClassDay.islower() or newClassDay.isupper()): #If the user put in some kind of string
        while not properDayInput(newClassDay): #Make sure that it is a valid day of the week
            newClassDay = input("Please enter a day of the week: ")
        class_.setDay(Day(newClassDay))
        noChangesMade = False
        
    newClassName = input("Enter new name for class: ")
    if not newClassName.strip() == "": #Check for all blanks/spaces
        class_.setName(newClassName.upper())
        noChangesMade = False
        
    newStartTime = input("Enter new starting time for class: ")
    if(newStartTime.isdigit()): #If the starting time is a digit at all
        while not properTimeInput(newStartTime): #persist for proper entry
            newStartTime = input("Enter a valid new starting time (24 hr format): ")
        class_.setstartTime(newStartTime)
        noChangesMade = False
        
    newEndTime = input("Enter new ending time for class: ")
    if(newEndTime.isdigit()):
        while not properTimeInput(newEndTime):
            newEndTime = input("Enter a valid new ending time (24 hr format): ")
        class_.setendTime(newEndTime)
        noChangesMade = False
        
    if noChangesMade:
        print("\n No Changes Made")
        delay()
    else:
        print("\nChanges Made")
        delay()

def deleteClass():
    """
    Method delete class deletes a user-selected class from the ongoing list of classes
    """
    displayClassList(True)
    if len(classes) == 0:
        return
    
    print("\nWhich class would you like to delete?")
    classIndex = input("Choice: ")
    if int(classIndex) == len(classes) + 1: #Return if choice is None from displayClassList
        return
    else:
        while not properMenuChoice(classIndex): 
            classIndex = input("Please enter a valid menu choice: ")         
    classIndex = int(classIndex)
    className = classes[classIndex-1].getName()
    classDay =  classes[classIndex-1].getDay()
    del classes[classIndex-1]
    print("\nDeleted " + className + " on " + str(classDay))
    delay()

def printSchedule():
    """
    Method printSchedule prints a formated schedule to the Terminal
    """
    print("{0:^45}".format("Your Schedule:\n"))
    print("  Day            Class          Time")
    if(len(classes) == 0):
        print("\nThere are no classes\n")
        return
    for class_ in classes:
        print(class_.scheduleString())
    print()
    
def genScheduleCSV():
    """
    Method genScheduleCSV prints a formated schedule to the Terminal and exports to a csv file
    """
    try: 
        printSchedule()
        save_class_list()
        print("\nSchedule generated, check working directory")
    except Exception as e:
        print("Exception found" + str(e))

def formatFromCSV(String):
    """
    Method formatFromCSV takes a String that represents a class time from a csv file 
    and formates the time appropriately
    
    :type String: String
    :param String: the String to format
    :returns: the correctly formatted String
    """
    #CSV files strip all leading 0s from numbers
    if(len(String)) == 4:
        return String
    elif(len(String)) == 3:
        return ("0" + String).strip()
    elif(len(String)) == 2:
        return ("00" + String).strip()
    elif(len(String)) == 1:
        return ("000" + String).strip()
    
def load_class_list():
    """
    Method load_class_list reads class information from a csv file and adds classes to the
    classes list and the classStringList
    """
    try:
        firstLine = True #keeping track of the first line in the csv file (the header)
        index = 0
        if os.access("mySchedule.csv", os.F_OK): #If the file exists
            f = open("mySchedule.csv")
            for row in csv.reader(f):
                if firstLine:
                    firstLine = False
                    continue #skip first line
                classStringList.insert(index, row) #load file to classString list and to classes list
                classes.insert(index, Class(row[1], Day(row[0]), formatFromCSV(row[2]), formatFromCSV(row[3])))
                index += 1
            f.close()
    except Exception as e:
        print("Exception found:" + e)
       
def save_class_list():
    """
    Method save_class_list exports current information in the classes list to a csv
    """
    try:
        classStringList.clear() #clear the classString List
        for i in range(0,len(classes)):
            classStringList.append(classes[i].csvRow()) #enter classes to the classStringList from the classes
        f = open("mySchedule.csv", 'w', newline =  '')
        csv.writer(f).writerow(["Day", "Class", "Start Time", "End Time"])
        for classCSVString in classStringList:
            csv.writer(f).writerow(classCSVString)
        f.close()
    except Exception as e:
        print("Exception found:" + e)
    
def clearTerminal():
    """
    Method clearTerminal clears the Terminal for any OS
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def delay():
    """
    Method delay delays for 2 seconds by calling time.sleep()
    """
    time.sleep(2)
    
def mainLoop():
    """
    Method mainLoop keeps the program going until the user decides to exit
    """
    clearTerminal()
    load_class_list()
    print("Class Scheduler Program by Cameron Zurmuhl")
    print("Lafayette College, Class of 2020")
    print("Email: zurmuhlc@lafayette.edu\n")
   
    while True:
        choice = mainMenuChoice()
        if choice is None:
            delay()
            clearTerminal()
            continue
        if choice == 'q':
            print("\nExiting...")
            save_class_list()
            delay()
            clearTerminal()
            break
        elif choice == 'n':
            addClass()
        elif choice == 'd':
            deleteClass()
            clearTerminal()
        elif choice == 's':
            displayClassList(False)
            if(len(classes)==0):
                clearTerminal()
        elif choice == 'e':
            editClass()
            clearTerminal()
        elif choice == 'p':
            print()
            printSchedule()
        elif choice == 'g':
            print()
            genScheduleCSV()
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice.")
    
    
if __name__ == '__main__':
    mainLoop()    