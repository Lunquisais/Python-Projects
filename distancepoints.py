# distancepoints.py
# A program to measure the distance between two points

def main(): # Defines function to main
    print("This program measures the distance between two point.") # Description of program
    print() # Blank line for spacing
    
    x1, y1 = eval(input("Please enter the first point: ")) # Input for first coordinate
    x2, y2 = eval(input("Please enter the second point: ")) # Input for second coordinate
    
    d = (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2) # Equation for distance
    
    print("The distance between the twwo points is", d) # Output
    
main() # Call to function