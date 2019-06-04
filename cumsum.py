# cumsum.py
# A program to add the cumulative sum of a number

def main(): # Defines the function to main
    n = int(eval(input("Please enter a whole number: "))) # Input for cumulative sum
    fact = 0 # Baseline for addition
    for i in range(1, n+1): # Creates loop to add number and next number
        fact = fact + i # The addition of the number and the next number
    print("The cumulative sum of", n, "is", fact) # Output of cumulative sum
    
main() # Function