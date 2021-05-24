from karel.stanfordkarel import *

# File: HospitalKarel.py
# -----------------------------
# Here is a place to program your Section problem

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        if beepers_present():
            pick_beeper()
            build_hospital()

        if front_is_clear():
            move()
        
def build_hospital():
    turn_left()
    for i in range(2):
        put_beeper()
        move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    for i in range(2):
        move()
        put_beeper()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == '__main__':
    run_karel_program('HospitalKarel2.w')
