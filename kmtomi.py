# This is a program which converts kilometers to miles

print("This is a program to convert Kilometers into Miles.")

def main(): # Defines function to main variable
    km = eval(input("How many Kilometers do you want to convert? ")) # Creates the input box for km to mi
    miles = km * 0.62 # Equation for km to mi
    print(km, "kilometers is aproximately", miles, "miles.") # Output from calculations

main() # Call to function