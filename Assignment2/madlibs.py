WIZARD = 'Karel the Omniscient'
NUMBER_OF = 6174 # fun fact: this number is called Kaprekar's constant, and it is a pretty mysterious number :)
FRUIT = 'mangoes'
PRICE = 2.99
YEARS = 300

def main():
    print("There once was a wizard by the name of " + WIZARD + " who loved to eat " + FRUIT + ".")
    print(WIZARD + " always kept a stash of " + str(NUMBER_OF) + " " + FRUIT + " in their mini fridge!")
    print(WIZARD + " realized they couldn't keep all those " + FRUIT + " to themselves,")
    print("so they sold them at the market for $" + str(PRICE) + " apiece,")
    print("and with the earnings bought fruit to share with the entire village!")
    print("Legend says", YEARS, "years later, "+ WIZARD+ " is still eating fruit.")

if __name__ == '__main__':
    main()
