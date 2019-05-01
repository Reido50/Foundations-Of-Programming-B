# Length Unit Conversion Calculator
# Reid Harry
# 4/29/2019
# Converts between length units based on user input

from math import *
import sys

lengthUnits = ["cm", "in", "ft", "yd", "m", "km", "mi"]
unitStr = ""
lengthConversions = [1.0, 2.54, 12.0, 3.0, 1.09361, 1000.0, 1.60934]
lengthUnitPos = -1
newLengthUnitPos = 0
userUnit = ""
userVal = 0.0

def listConcat(list):
    global unitStr

    for x in range(len(list)):
        if(x < len(list)-1):
            unitStr += list[x] + ", "
        else:
            unitStr += list[x]

def convert(old, new):
    global lengthConversions
    global userVal 
    
    if(old != -1):
        increment = int(copysign(1.0, new - old))
        for x in range(int(old), int(new), increment):
            if(increment > 0):
                userVal/=lengthConversions[x+increment]
            elif(increment < 0):
                userVal*=lengthConversions[x]

def promptUnit():
    global lengthUnits
    global UnitStr
    global lengthUnitPos
    global newLengthUnitPos
    global userUnit

    while(userUnit == ""):
        # Prompt user for a length unit
        if(lengthUnitPos == -1):
            userUnit = input("Which unit of length would you like to start with (" + unitStr  + ")? Enter 'stop' to quit program:").lower()
        else:
            userUnit = input("Which unit of length would you like to convert to (" + unitStr + ")? Enter 'stop' to quit program:").lower()

        # Check for stop
        if(userUnit == "stop"):
            print("Thank you for using the Length Unit Coversion Calculator!")
            sys.exit()

        # Check for length unit in constant list
        for u in range(len(lengthUnits)):
            if(lengthUnits[u] == userUnit):   # Length unit found
                newLengthUnitPos = u
                convert(lengthUnitPos, newLengthUnitPos)
                lengthUnitPos = u
                break
            elif(u == len(lengthUnits) - 1):  # Length unit not found
                userUnit = ""
                print("The unit you chose was not found. Try again.")

def promptMeasure():
    global userVal
    global userUnit

    userVal = abs(float(input("Enter the measurement you would like to use (" + str(userUnit) + "):")))

def main():
    global userUnit
    global lengthUnits
    
    listConcat(lengthUnits)

    print("Length Unit Conversion Calculator")
    print("---------------------------------")

    # Request initial values of unit and measurement
    promptUnit()
    promptMeasure()

    while(True):
        # Reset user input
        userUnit = ""

        # Request conversion unit
        promptUnit()

        # Print answer
        print(str(round(userVal, 3)) + " " + userUnit)

main()