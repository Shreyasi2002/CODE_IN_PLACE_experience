"""
Prints the Fizz Buzz sequence up to a given number.
"""

def main():
    num = int(input("Number to count to: "))
    total_fizz = 0
    total_buzz = 0
    total_fizz_buzz = 0
    for i in range(1, num+1):
        check = check_fizz_buzz(i)
        if check == "fizz":
            total_fizz += 1
        elif check == "buzz":
            total_buzz += 1
        elif check == "fizzbuzz":
            total_fizz_buzz += 1
        print(check)

    print("Num fizzed:", total_fizz)
    print("Num buzzed:", total_buzz)
    print("Num fizzbuzzed:", total_fizz_buzz)

def check_fizz_buzz(num):
    if num%3 ==0 and num%5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num
 
if __name__ == '__main__':
    main()
