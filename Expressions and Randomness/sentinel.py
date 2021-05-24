"""
Asks the user for a number until they enter -1
Reports the total value of all the numbers at the end
"""

SENTINEL_VALUE = -1

def main():
    total = 0 # stores the total of the numbers user inputs
    num = int(input("Type a number : "))
    while num != -1:   # checks whether the number user inputs is the sentinel value
        total += num    # calculates the total of all the user inputs

        # Takes the next input from the user
        num = int(input("Type a number : "))

    print("total is", total)

if __name__ == '__main__':
    main()
