# easter.py
# A program to determine when Easter is based on the year

def main(): # Defines function to the variable main
    print("What day did Easter land on?") # Poses the question
    print() # line for spacing
    year = eval(input("Please enter the year you wish to know: ")) # Input for the year
    
    c = year// 100 # equation for determining year
    epact = (8 + (c // 4) - c + ((8 * c + 13) // 25)) + 11 * (year % 19) % 30 # Equation for determining the day easter landed on
             
    print(epact) # Output
             
main() # Call to function