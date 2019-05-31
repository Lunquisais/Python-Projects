# coffeeship.py
# A program to determine the cost of shipping coffee based on pounds

def main(): # Definess funtion to variable
    lb = eval(input("How many pounds of coffee did you purchase? ")) # Creates input for the pounds of coffee
    
    cost = float(10.5 * lb) + float(float(.86 * lb) + 1.50) # Equation for converting pounds of coffe by price
    
    print("The cost will be", cost) # Output
    
main() # Call to function