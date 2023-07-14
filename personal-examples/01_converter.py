"""Module to perform inter-conversion between different units of measurement"""

# Import modules.

import sys
import custom_module_clear_screen

# Define functions.

def intomile(fnNoOfUnits):
    """Function to convert in to mile"""
    fnKmLength = intokm(fnNoOfUnits)
    fnMileLength = fnKmLength / 1.61
    return round(fnMileLength,2)

def intokm(fnNoOfUnits):
    """Function to convert in to km"""
    fnCmLength = intocm(fnNoOfUnits)
    fnKmLength = cmtokm(fnCmLength)
    return round(fnKmLength,2)

def intom(fnNoOfUnits):
    """Function to convert in to m"""
    fnCmLength = intocm(fnNoOfUnits)
    fnMLength = fnCmLength / 100
    return round(fnMLength,2)

def intoft(fnNoOfUnits):
    """Function to convert in to ft"""
    fnCmLength = intocm(fnNoOfUnits)
    fnFtLength = fnCmLength / 30.48
    return round(fnFtLength,2)

def intocm(fnNoOfUnits):
    """Function to convert in to cm"""
    fnCmLength = fnNoOfUnits * 2.54
    return round(fnCmLength,2)

def intomm(fnNoOfUnits):
    """Function to convert in to mm"""
    fnMmLength = fnNoOfUnits * 2.54 * 10
    return round(fnMmLength,2)

def cmtomile(fnNoOfUnits):
    """Function to convert cm to mile"""
    fnKmLength = cmtokm(fnNoOfUnits)
    fnMileLength = fnKmLength / 1.61
    return round(fnMileLength,2)

def cmtokm(fnNoOfUnits):
    """Function to convert cm to km"""
    fnKmLength = fnNoOfUnits / 100000
    return round(fnKmLength,2)

def cmtom(fnNoOfUnits):
    """Function to convert cm to m"""
    fnMLength = fnNoOfUnits / 100
    fnMLength = round(fnMLength,2)
    return fnMLength

def cmtoft(fnNoOfUnits):
    """Function to convert cm to ft"""
    fnFtLength = fnNoOfUnits / 30.48
    fnFtLength = round(fnFtLength,2)
    return fnFtLength

def cmtoin(fnNoOfUnits):
    """Function to convert cm to in"""
    fnInLength = fnNoOfUnits / 2.54
    fnInLength = round(fnInLength,2)
    return fnInLength

def cmtomm(fnNoOfUnits):
    """Function to convert cm to mm"""
    fnMmLength = fnNoOfUnits * 10
    fnMmLength = round(fnMmLength,2)
    return fnMmLength

def mmtomile(fnNoOfUnits):
    """Function to convert mm to mile"""
    fnKmLength = mmtokm(fnNoOfUnits)
    fnMileLength = fnKmLength / 1.61
    fnMileLength = round(fnMileLength,2)
    return fnMileLength

def mmtokm(fnNoOfUnits):
    """Function to convert mm to km"""
    fnMLength = mmtom(fnNoOfUnits)
    fnKmLength = fnMLength / 1000
    fnKmLength = round(fnKmLength,2)
    return fnKmLength

def mmtom(fnNoOfUnits):
    """Function to convert mm to m"""
    fnMLength = fnNoOfUnits / 1000
    fnMLength = round(fnMLength,2)
    return fnMLength

def mmToft(fnNoOfUnits):
    """Function to convert mm to ft"""
    fnCmLength = mmTocm(fnNoOfUnits)   # convert to cm
    fnFtLength = fnCmLength / 30.48     # convert to ft
    fnFtLength = round(fnFtLength,2)
    return fnFtLength

def mmToin(fnNoOfUnits):
    """Function to convert mm to inch"""
    fnCmLength = mmTocm(fnNoOfUnits)   # convert to cm
    fnInLength = fnCmLength / 2.54      # convert to in
    fnInLength = round(fnInLength,2)
    return fnInLength

def mmTocm(fnNoOfUnits):
    """Function to convert mm to cm"""
    fnCmLength = fnNoOfUnits / 10
    fnCmLength = round(fnCmLength,2)
    return fnCmLength

def performLengthConversion(fnFirstChoice,fnSecondChoice,fnNoOfUnits):
    """Function to perform inter-conversion between units of length"""
    if fnFirstChoice == 1:
        if fnSecondChoice == 1:
            print(f"{fnNoOfUnits} mm = {fnNoOfUnits} mm")
        elif fnSecondChoice == 2:
            cmLength = mmTocm(fnNoOfUnits)
            print(f"{fnNoOfUnits} mm = {cmLength} cm")
        elif fnSecondChoice == 3:
            inLength = mmToin(fnNoOfUnits)
            print(f"{fnNoOfUnits} mm = {inLength} in")
        elif fnSecondChoice == 4:
            ftLength = mmToft(fnNoOfUnits)
            print(f"{fnNoOfUnits} mm = {ftLength} ft")
        elif fnSecondChoice == 5:
            mLength = mmtom(fnNoOfUnits)
            print(f"{fnNoOfUnits} mm = {mLength} m")
        elif fnSecondChoice == 6:
            kmLength = mmtokm(fnNoOfUnits)
            print(f"{fnNoOfUnits} mm = {kmLength} km")
        else:
            mileLength = mmtomile(fnNoOfUnits)
            print(f"{fnNoOfUnits} mm = {mileLength} mile")
    elif fnFirstChoice == 2:
        if fnSecondChoice == 1:
            mmLength = cmtomm(fnNoOfUnits)
            print(f"{fnNoOfUnits} cm = {mmLength} mm")
        elif fnSecondChoice == 2:
            print(f"{fnNoOfUnits} cm = {fnNoOfUnits} cm")
        elif fnSecondChoice == 3:
            inLength = cmtoin(fnNoOfUnits)
            print(f"{fnNoOfUnits} cm = {inLength} in")
        elif fnSecondChoice == 4:
            ftLength = cmtoft(fnNoOfUnits)
            print(f"{fnNoOfUnits} cm = {ftLength} ft")
        elif fnSecondChoice == 5:
            mLength = cmtom(fnNoOfUnits)
            print(f"{fnNoOfUnits} cm = {mLength} m")
        elif fnSecondChoice == 6:
            kmLength = cmtokm(fnNoOfUnits)
            print(f"{fnNoOfUnits} cm = {kmLength} km")
        else:
            mileLength = cmtomile(fnNoOfUnits)
            print(f"{fnNoOfUnits} cm = {mileLength} mile")
    elif fnFirstChoice == 3:
        if fnSecondChoice == 1:
            mmLength = intomm(fnNoOfUnits)
            print(f"{fnNoOfUnits} in = {mmLength} mm")
        elif fnSecondChoice == 2:
            cmLength = intocm(fnNoOfUnits)
            print(f"{fnNoOfUnits} in = {cmLength} cm")
        elif fnSecondChoice == 3:
            print(f"{fnNoOfUnits} in = {fnNoOfUnits} in")
        elif fnSecondChoice == 4:
            ftLength = intoft(fnNoOfUnits)
            print(f"{fnNoOfUnits} in = {ftLength} ft")
        elif fnSecondChoice == 5:
            mLength = intom(fnNoOfUnits)
            print(f"{fnNoOfUnits} in = {mLength} m")
        elif fnSecondChoice == 6:
            kmLength = intokm(fnNoOfUnits)
            print(f"{fnNoOfUnits} in = {kmLength} km")
        else:
            mileLength = intomile(fnNoOfUnits)
            print(f"{fnNoOfUnits} in = {mileLength} mile")

def validateInputs(fnFirstChoice,fnSecondChoice,fnNoOfUnits):
    """Function to validate user inputs regarding units"""
    if fnFirstChoice not in range(1,8,1) or fnSecondChoice not in range(1,8,1):
        print("Incorrect choice of units! Please enter a choice between numbers 1,2,3,..,7 only. Exiting script!\n")
        sys.exit(1)
    elif fnNoOfUnits < 0:
        print("Quantity cannot be negative! Please provide positive number only. Exiting script!\n")
        sys.exit(1)

def displayUnitsOfLength():
    """Function to display units of length & accept user input"""
    print("""
    Units of length are:
    1. Millimeter (mm)
    2. Centimeter (cm)
    3. Inch (in)
    4. Foot (ft)
    5. Meter (m)
    6. Kilometer (km)
    7. Mile (mile)
    """)
    try:
        fnFirstChoice = int(input("Which unit do you want to convert [1|2|..|7]: "))
        fnSecondChoice = int(input("To which unit the conversion needs to be done [1|2|..|7]: "))
        fnNoOfUnits = float(input("How many units do you want to convert: "))
    except ValueError:
        print("Please enter a number only. Exiting script!\n")
        sys.exit(1)
    return fnFirstChoice, fnSecondChoice, fnNoOfUnits

def acceptUserChoice():
    """Function to accept user choice for what quantity needs to be processed"""
    print("""
    What do you want to convert?
    1. Length
    2. Weight
    """)
    try:
        fnUserChoice = int(input("Enter choice [1|2]: "))
    except ValueError:
        print("Please provide an integer only. Exiting script!\n")
        sys.exit(1)
    return fnUserChoice

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script performs inter-conversion between different units of measurement.")
    input("Press ENTER key to continue...\n")
    while True:
        userChoice = acceptUserChoice()
        if userChoice == 1:
            firstChoice, secondChoice, noOfUnits = displayUnitsOfLength()
            validateInputs(firstChoice,secondChoice,noOfUnits)
            performLengthConversion(firstChoice,secondChoice,noOfUnits)
        elif userChoice == 2:
            pass
        else:
            print("Invalid choice. Please enter 1 or 2 only. Exiting script!")
            sys.exit(1)
        repeatChoice = input("\nDo you want to repeat again [y|n]: ")
        if repeatChoice == "y":
            continue
        elif repeatChoice == "n":
            break
        else:
            print("Invalid choice! Please enter letters y or n only. Exiting script!\n")
            sys.exit(1)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
