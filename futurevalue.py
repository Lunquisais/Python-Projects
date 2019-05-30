def main(): # Defining the function and binding to main
    print("What will my savings account be in 10 years?") 
    principal = eval(input("What is the principal amount in my bank account? ")) # Creating the input for bank account balance
    fixedval = eval(input("How much do you intended to invest each year? ")) # Creating input for amount invested each year
    apr = eval(input("What is the APR? ")) # Creating input for APR
    period = (apr/4) # Creating quaterly period so APR can be done 4 times each year
    years = eval(input("How many years do you want projections for? ")) # Creating input for amount of years to calculate for
    
    for i in range(years): # Creating loop for annual increase
       principal = (principal + fixedval) * (1 + (period/ 100)) # Equation for principal, investment and apr
       
       print(principal)
            
main()