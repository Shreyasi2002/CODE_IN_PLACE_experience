import math

# The constant K in the half life formula
K = -8266.64258429376

def main():
    calculate_age_single_sample()
    
def calculate_age_single_sample():
    # Ask the user to enter the percent of c14 left in their sample
    pct_left = float(input("% of natural c14: "))
    # Calculate the age: https://en.wikipedia.org/wiki/Radiocarbon_dating
    age = K * math.log(pct_left / 100)
    # Print the result
    print("Sample is " + str(age) + " years old.")

if __name__ == '__main__':
    main()
