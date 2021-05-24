"""
Simulates a magic eight ball.
Prompts the user to type a yes or no question and gives
a random answer from a set of prefabricated responses.
"""

import random
RESPONSES = ["As I see it, yes.", "Ask again later.", "Better not to tell you now."
, "Cannot predict now.", "Concentrate and ask again.", "Don't count on it." 
, "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no."
, "My sources say no.", "Outlook not so good.", "Outlook good.", "Reply hazy, try again."
, "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes."
, "Yes - definitely.", "You may rely on it."]
TOTAL_RESPONSES = 19

def main():
    question = input("Ask a yes or no question: ")
    num = 0   # to represent the index of the RESPONSES list
    while question != "":
        num = random.randint(0, TOTAL_RESPONSES)
        print(RESPONSES [num])
        question = input("Ask a yes or no question: ")

if __name__ == "__main__":
    main()
