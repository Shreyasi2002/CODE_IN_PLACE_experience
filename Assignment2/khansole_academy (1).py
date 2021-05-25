"""
TODO: This code randomly generates addition problems 
until the user has gotten 3 problems correct in a row.

"""

import random 
MAX_2DIGIT_NUM = 99
MIN_2DIGIT_NUM = 10

def main():
    num_correct = 0
    while num_correct<3:
        num1 = random.randint(MIN_2DIGIT_NUM, MAX_2DIGIT_NUM)
        num2 = random.randint(MIN_2DIGIT_NUM, MAX_2DIGIT_NUM)
        print("What is", num1, "+", num2,"?")
        answer = int(input("Your answer: "))
        if answer == (num1+num2):
            num_correct +=1
            print("Correct! You've gotten", num_correct, "correct in a row.")
        else:
            num_correct = 0
            print("Incorrect. The expected answer is", (num1+num2))
    print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()
