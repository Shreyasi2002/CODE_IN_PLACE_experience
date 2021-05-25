"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 
MAX_2DIGIT_NUM = 99
MIN_2DIGIT_NUM = 10

def main():
    num1 = random.randint(MIN_2DIGIT_NUM, MAX_2DIGIT_NUM)
    num2 = random.randint(MIN_2DIGIT_NUM, MAX_2DIGIT_NUM)
    print("What is", num1, "+", num2,"?")
    answer = int(input("Your answer: "))
    if answer == (num1+num2):
        print("Correct!")
    else:
        print("Incorrect. The expected anser is", (num1+num2))

if __name__ == '__main__':
    main()
