# Change.py
# A program to calculate the value of some change in dollars

def main(): # Defines the function to a variable
    print("Change counter") # Name of what the function does
    print() # Creates a space
    print("Please enter the count of each coin type.") # Instructions
    quarters = eval(input("Quarters: ")) # Input for quarters
    dimes = eval(input("Dimes: ")) # Input for dimes
    nickles = eval(input("Nickles: ")) # Input for nickles
    pennies = eval(input("Pennies: ")) # Input for pennies
    total = quarters * .25 + dimes * .10 + nickles * .05 + pennies *.01 # Equation to sum everything
    print() # New line
    print("The total value of your change is", total) # The total
    
main() # Call to function