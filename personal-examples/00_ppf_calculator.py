"""Module to calculate maturity amount for PPF investment scheme in India"""

# Import modules.

import sys
import custom_module_clear_screen

# Define functions.

def ValidateInputs(FnStartYear,FnInvestmentDuration,FnInvestmentAmount,FnInvestmentChoice):
    """Function to validate user provided inputs"""
    if FnStartYear not in range(1970,2071,1):
        print("\nEntered start year should be between 1970 to 2070. Exiting script!\n")
        sys.exit(1)
    elif FnInvestmentDuration not in range(15,71,5):
        print("\nEntered tenure should be between 15 to 70 as a multiple of 5. Exiting script!\n")
        sys.exit(1)
    elif FnInvestmentChoice == "yearly" and FnInvestmentAmount not in range(1,150001,1):
        print("\nEntered yearly investment amount should be between 1 to 150000. Exiting script!\n")
        sys.exit(1)
    elif FnInvestmentChoice == "monthly" and FnInvestmentAmount not in range(1,12501,1):
        print("\nEntered monthly investment amount should be between 1 to 12500. Exiting script!\n")
        sys.exit(1)
    elif FnInvestmentChoice not in ["yearly","monthly"]:
        print("Function ValidateInputs() accepts last argument as 'yearly' or 'monthly' strings only. Exiting script!\n")
        sys.exit(1)

def AcceptInputs(FnInvestmentChoice):
    """Function to accept user inputs"""
    try:
        FnStartYear = int(input("Enter start year [1970 to 2070]: "))
        FnInvestmentDuration = int(input("Enter tenure in years [Min 15, thereafter 20,25,30...70]: "))
        if FnInvestmentChoice == "yearly":
            FnInvestmentAmount = int(input("Enter yearly investment amount [Max 150000]: "))
        elif FnInvestmentChoice == "monthly":
            FnInvestmentAmount = int(input("Enter monthly investment amount [Max 12500, which is Max 150000 in 1 year]: "))
        else:
            print("Function AcceptInputs() accepts input as 'yearly' or 'monthly' strings only. Exiting script!\n")
            sys.exit(1)
    except ValueError:
        print("\nInvalid input. Please provide integer value only for above 3 inputs. Exiting script!\n")
        sys.exit(1)
    # Return multiple values as tuple.
    return FnStartYear, FnInvestmentDuration, FnInvestmentAmount  # OR return (FnStartYear,FnInvestmentDuration,FnInvestmentAmount)

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("""
    This script calculates maturity amount for PPF investment scheme.
    We'll ask you a series of questions. Based on your answers,
    maturity amount will be calculated.
    """)
    input("Press ENTER key to continue.")
    while True:
        print()
        print("Will you do an annual or monthly investment?")
        print("1. Annual\n2. Monthly")
        try:
            InvestmentChoice = int(input("Enter choice [1|2]: "))
        except ValueError:
            print("\nPlease enter the numbers 1 or 2 only. Exiting script!\n")
            sys.exit(1)
        if InvestmentChoice == 1:
            print("\nThis calculation will be based on investments done in Apr every year, when financial year starts.")
            StartYear, InvestmentDuration, InvestmentAmount = AcceptInputs("yearly")
            ValidateInputs(StartYear,InvestmentDuration,InvestmentAmount,"yearly")
            EndYear = StartYear + InvestmentDuration
            TotalInvestment = InvestmentAmount * InvestmentDuration
            ROI = 7.1
            BalAmount = 0  # Initial balance is considered as 0 when PPF account is opened.
            Iteration = InvestmentDuration
            while Iteration != 0:
                Principal = InvestmentAmount + BalAmount
                Interest = (Principal * ROI)/100  # calculate for entire year where n=1 in (pnr)/100
                BalAmount = Principal + Interest
                # Run loop until interest is calculated for each year for complete duration.
                Iteration = Iteration - 1
            BalAmount = int(BalAmount)
            GrowthInMoney = BalAmount - TotalInvestment
            GrowthInPercentage = round((GrowthInMoney / TotalInvestment) * 100, 2)
            print(f"""
            Investment started in Apr of the year       : {StartYear}
            Investment duration/tenure                  : {InvestmentDuration} years
            End year of the investment tenure           : {EndYear}
            Investment done in each year                : {InvestmentAmount}
            Total investment done over the years        : {TotalInvestment}
            PPF rate of interest                        : {ROI}%p.a.
            Maturity amount in Mar end of the end year  : {BalAmount}
            Growth happened in money                    : {GrowthInMoney}
            Growth expressed in percentage              : {GrowthInPercentage}%
            *** Note: The maturity amount will change if ROI gets revised by govt in any quarter. ***
            """)
        elif InvestmentChoice == 2:
            print("\nThis calculation will be based on monthly investments started in Apr every year, when financial year starts.")
            StartYear, InvestmentDuration, InvestmentAmount = AcceptInputs("monthly")
            ValidateInputs(StartYear,InvestmentDuration,InvestmentAmount,"monthly")
            EndYear = StartYear + InvestmentDuration
            TotalInvestment = InvestmentAmount * 12 * InvestmentDuration
            ROI = 7.1
            BalAmount = 0  # Initial balance is considered as 0 when PPF account is opened.
            Iteration = InvestmentDuration
            while Iteration != 0:
                TotalInterestForYear = 0
                for i in range(1,13,1):
                    Principal = InvestmentAmount + BalAmount
                    Interest = (Principal * ROI)/1200  # calculate for one month where n=1/12 in (pnr)/100
                    TotalInterestForYear = TotalInterestForYear + Interest
                    BalAmount = Principal
                BalAmount = BalAmount + TotalInterestForYear
                Iteration = Iteration - 1
            BalAmount = int(BalAmount)
            GrowthInMoney = BalAmount - TotalInvestment
            GrowthInPercentage = round((GrowthInMoney / TotalInvestment) * 100, 2)
            print(f"""
            Investment started in Apr of the year       : {StartYear}
            Investment duration/tenure                  : {InvestmentDuration} years
            Investment ended in Mar of the year         : {EndYear}
            Investment done in each month               : {InvestmentAmount}
            Total investment done over the years        : {TotalInvestment}
            PPF rate of interest                        : {ROI}%p.a.
            Maturity amount in Mar end of the end year  : {BalAmount}
            Growth happened in money                    : {GrowthInMoney}
            Growth expressed in percentage              : {GrowthInPercentage}%
            *** Note: The maturity amount will change if ROI gets revised by govt in any quarter. ***
            """)
        else:
            print("\nInvalid input. Please enter the numbers 1 or 2 only. Exiting script!\n")
            sys.exit(1)
        userChoice = input("Do you want to repeat again? [y|n]: ")
        if userChoice == "y":
            pass
        elif userChoice == "n":
            quit()

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
