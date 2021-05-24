from karel.stanfordkarel import *

"""
File: Mountain.py
----------------------------
Karel climbs a mountain of any size and plants a beeper at the top.
"""

def main():
    # Milestone 1: Climb the mountain
    ascend_mountain()
    # Milestone 2: Put beeper at the top
    put_beeper()
    # Milestone 3: Descend the mountain()
    descend_mountain()

def ascend_mountain():
    while front_is_blocked():
        step_up()

def descend_mountain():
    while front_is_clear():
        step_down()

def step_up():
    # Climbs one step up the mountain
    turn_left()
    move()
    turn_right()
    move()

def step_down():
    # Moves one step down the mountain
    move()
    turn_right()
    move()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    run_karel_program('Mountain2.w')
