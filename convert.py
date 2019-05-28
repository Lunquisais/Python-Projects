# Convert.py
# A program to convert Celcius to Farengeight
# By Matt W.

print("Hello, welcome to the Celcius to Farenheight converter. Enjoy!")

def main(): # Defines the function and creates the variable main
    celcius = 0 # Baseline for Celcius
    farenheight = 9/5 * celcius + 32 # Mathematical equation for C to F
    print("The temperature is", farenheight, "degrees Farenheight.") # Output line
    
    for i in range(5): # Loop repeats 5 times
        celcius = celcius + 10 # Increases Celcius by 10 degrees each time
        farenheight = 9/5 * celcius + 32 # Equation for C to F
        print("If the temperature is " celcius "celcius, then it will be ", farenheight "degrees Farenheight.") # Output
        
main() # Call to function