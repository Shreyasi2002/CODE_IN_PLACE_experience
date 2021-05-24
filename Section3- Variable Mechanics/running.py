"""
Prompts the user to enter numbers and prints
the running total until the user enters 0.
"""

def main():
    num = int(input("Enter a value: "))
    total = num
    while num != 0:
        print("Running total is", total)
        num = int(input("Enter a value: "))
        total += num
    

if __name__ == '__main__':
    main()
