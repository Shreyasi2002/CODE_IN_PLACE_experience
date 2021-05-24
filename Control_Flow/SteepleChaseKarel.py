from karel.stanfordkarel import *

"""
File: SteepleChaseKarel.py
--------------------------
Karel runs a steeple chase that is 9 avenues long.
Hurdles are of arbitrary height and placement.
"""


def main():
    """
    To run a race that is 9 avenues long, we need to move
    forward or jump hurdles 8 times.
    """

    
    for i in range(8):
        if front_is_clear():
            move()
        else:
            run_the_race()

def run_the_race():
    turn_left()
    pass_hurdle()
    turn_right()
    move()
    turn_right()
    move_to_wall()
    turn_left()


def move_to_wall():
    while front_is_clear():
        move()

def pass_hurdle():
    while right_is_blocked():
        move()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program('SuperSteepleChaseKarel.w')
