# Reid Harry
# 4/21/2019
# Converts measurements from inches to centimeters


def main():
    print("Inches to Centimeters Conversion:")

    for x in range(3):
        inch = abs(
            float(input("Enter number of inches for trial " + str(x + 1) + ": ")))
        cm = inch * 2.54
        print(str(inch) + " inches is equal to " + str(cm) + " centimeters.")


main()
