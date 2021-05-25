"""
TODO: Write a description here
"""

import random
TOTAL_STONES = 20
PLAYERS = [1,2]
flag=0 # indicator to determine the number of player

def input_is_invalid(amount):
    if (amount == 1 or amount == 2):
        return False
    else:
        return True

def change_player(num):
    if num % 2 == 0:
        return PLAYERS[1]
    else:
        return PLAYERS[0]


def main():
    num_stones = TOTAL_STONES
    iteration = 0
    while num_stones>0:
        iteration += 1
        player_num = change_player(iteration)
        print("There are", num_stones, "stones left")
        print("Player", player_num, "would you like to remove 1 or 2 stones? ",end="", flush=True)
        amount = int(input())
        while input_is_invalid(amount):
            amount = int(input("Please enter 1 or 2: "))
        num_stones -=amount
        print("")
    player_num = change_player(iteration+1)
    print("Player", player_num, "wins!")


if __name__ == '__main__':
    main()
