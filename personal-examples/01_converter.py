"""Module to perform inter-conversion between different units of measurement"""

# Import modules.

import sys
import custom_module_clear_screen

# Define functions.

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
