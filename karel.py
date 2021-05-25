N_COLS = 3 # notice these constants!
N_ROWS = 3

def main():
    print("Welcome to first person Karel. You're at row 1, column 1, facing East (facing column " + str(N_COLS) + ")")
    facing_direction = 'East' # this variable will keep track of the way Karel is facing -- it changes if the user says to "turn left"!
    curr_col = 1 # this variable ...
    curr_row = 1 # ... and this one keep track of Karel's position in the world! they may change if the user says to "move"
    action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
    while action != "":
        flag = 0
        if action == "move":
            if facing_direction == 'East':
                if curr_col < N_COLS:
                    curr_col += 1
                    flag = 1
                else:
                    flag = 0

            elif facing_direction == 'West':
                if curr_col > 1:
                    curr_col -= 1
                    flag = 1
                else:
                    flag = 0

            elif facing_direction == 'North':
                if curr_row < N_rows:
                    curr_row += 1
                    flag = 1
                else:
                    flag = 0

            elif facing_direction == 'South':
                if curr_row > 1:
                    curr_row -= 1
                    flag = 1
                else:
                    flag = 0

            if flag == 1:
                print("You moved one step forward and now you're at row", curr_row, "column", curr_col)
            else:
                print("You can't move forward!")

        elif action == "turn left":
            if facing_direction == 'East':
                facing_direction = 'North'
            elif facing_direction == 'North':
                facing_direction = 'West'
            elif facing_direction == 'West':
                facing_direction = 'South'
            elif facing_direction == 'South':
                facing_direction = 'East'

            print("You turned left and are now facing " + facing_direction + ".")
        
        action = input("What would you like to do? You can move and turn left. Press enter to finish. ")

    print("You've ended up at row " + str(curr_row) + " and column " + str(curr_col) + " facing " + facing_direction + ".")


if __name__ == "__main__":
    main()
