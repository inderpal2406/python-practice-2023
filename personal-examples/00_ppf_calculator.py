"""Module to calculate maturity amount for PPF investment scheme in India"""

# Import modules.

import custom_module_clear_screen

# Define functions.

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
        investmentChoice = input("Will you do an annual/monthly investment? [annual|monthly]: ")
        if investmentChoice == "annual":
            print("Annual investments are recommended to be done in Apr every year, when financial year starts.")
            startYear = int(input("Enter start year: "))
            endYear = int(input("Enter end year: "))
            investmentAmount = int(input("Enter yearly investment amount: "))
            yearDifference = endYear - startYear
            noOfYears = yearDifference
            totalInvestment = investmentAmount*noOfYears
            noOfYear = 1  # We calculate interest for each year as compounding takes place.
            roi = 7.1
            interest = 0
            balAmount = 0
            while yearDifference != 0:
                principal = investmentAmount + balAmount
                interest = (principal*noOfYear*roi)/100  # calculate for entire year where n=1 in (pnr)/100
                balAmount = principal + interest
                yearDifference = yearDifference-1
            balAmount = int(balAmount)
            growthInMoney = balAmount - totalInvestment
            print(f"""
            An yearly investment of {investmentAmount} done every year between
            {startYear} and {endYear}, which is for a period of {noOfYears} years,
            would yield a maturity amount of {balAmount} rupees, on a total
            investment of {totalInvestment} rupees, at the rate of interest (ROI) as {roi}%p.a.
            So, total growth in money = {growthInMoney} rupees
            """)
            print("The maturity amount will change if ROI gets revised by govt in any quarter.")
        elif investmentChoice == "monthly":
            pass
        userChoice = input("Do you want to repeat again? [y|n]: ")
        if userChoice == "y":
            pass
        elif userChoice == "n":
            quit()

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
