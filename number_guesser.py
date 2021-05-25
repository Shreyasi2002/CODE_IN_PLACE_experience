"""
Number Guesser Program

This is an example of how to use variables to 
keep track of information in a program that 
also makes use of loops
"""
import random

def main():
    minimum = 1
    maximum = 100
    num_guess = 0
    guess = random.randint(minimum, maximum)
    feedback = input("Is your number " + str(guess) + "?")
    while feedback != 'correct':
        if feedback == 'lower':
            maximum = guess
        elif feedback == 'higher':
            minimum = guess
        
        num_guess += 1
        guess = random.randint(minimum, maximum)
        feedback = input("Is your number " + str(guess) + "?")

    print("I win! It took me", num_guess, "guesses")

    

if __name__ == "__main__":
    main()
