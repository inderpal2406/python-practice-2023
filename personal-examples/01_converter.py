"""Module to perform inter-conversion between different units of measurement"""

# Import modules.

import sys
import custom_module_clear_screen

# Define functions.

def mmToft(fnNoOfUnits):
    """Function to convert mm to ft"""
    cmLength = fnNoOfUnits / 10   # convert to cm
    answer = cmLength / 30.48     # convert to ft
    answer = round(answer,2)
    print(f"{fnNoOfUnits} mm = {answer} ft")

def mmToin(fnNoOfUnits):
    """Function to convert mm to inch"""
    cmLength = fnNoOfUnits / 10   # convert to cm
    answer = cmLength / 2.54      # convert to in
    answer = round(answer,2)
    print(f"{fnNoOfUnits} mm = {answer} in")

def mmTocm(fnNoOfUnits):
    """Function to convert mm to cm"""
    answer = fnNoOfUnits / 10
    answer = round(answer,2)
    print(f"{fnNoOfUnits} mm = {answer} cm")

def performLengthConversion(fnFirstChoice,fnSecondChoice,fnNoOfUnits):
    """Function to perform inter-conversion between units of length"""
    if fnFirstChoice == 1:
        if fnSecondChoice == 1:
            print(f"{fnNoOfUnits} mm = {fnNoOfUnits} mm")
        elif fnSecondChoice == 2:
            mmTocm(fnNoOfUnits)
        elif fnSecondChoice == 3:
            mmToin(fnNoOfUnits)
        elif fnSecondChoice == 4:
            mmToft(fnNoOfUnits)

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
