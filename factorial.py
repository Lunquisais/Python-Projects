# factorial.py
# A program to compute the factorial of a number
# Illustrates for loop with an acccumulator

def main(): # Defines function to variable main
    n = eval(input("Please enter a whole number: ")) # Creates input for number to be factorialed
    fact = 1 # Initial fact
    for factor in range(n,1,-1): # Loop to go through all of the numbers from n down to 1.
        fact = fact * factor # Multiplying n * n-1
    print("The factorial of:", n, "is", fact) # Output
        
main() # Call to function