# cumcube.py
# A program to determin the sums of cubric roots of a number

def main(): # Defining the function to a variable
    n = int(eval(input("Please enter a whole number to find the sum of it its cubes: "))) # Input for cube root
    
    total = 0 # Initial starting point
    for i in range(1, n+1): # Loop to make the cube
        total = total + i**3 # Equation for cubing
        
    print("The total sum of all the cubes is", total, ".") # Output
    
main() # Function