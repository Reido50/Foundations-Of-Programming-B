# Length Unit Conversion Calculator
# Reid Harry
# 4/29/2019
# Converts between length units based on user input

def main():
    print("Length Unit Conversion Calculator")
    print("---------------------------------")

    lengthUnits = ["cm", "in", "ft", "yd", "m", "km", "mi"]
    lengthUnitPos = 0
    measureVal = 0
    userUnit = ""
    userVal = 0

    # Request initial units and measurement
    while(userUnit == ""):
        userUnit = input("Which unit of length would you like to use (cm, in, ft, yd, m, km, mi)? Enter 'stop' to quit program:").lower()
        #for u in lengthUnits:
        
    userVal = float(input("Enter the measurement you would like to use in " + userUnit + ":"))
main()