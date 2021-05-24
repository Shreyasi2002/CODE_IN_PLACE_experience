from karel.stanfordkarel import *

"""
File: Midpoint.py
------------------------
Place a beeper on the middle of the first row.
"""

def main():
    """
    Your code here
    """
    
    paint_corner(CYAN)
    move_to_wall()
    paint_corner(CYAN)
    turn_around()
    move_if()
    while corner_color_is(BLANK):
        steps_to_midpoint()
    turn_around()
    move_if()
    put_beeper()
    move_to_wall()
    turn_around()
    clear_color()
    move_to_beeper()

def steps_to_midpoint():
    while corner_color_is(BLANK):
        move_if()
    turn_around()
    move_if()
    paint_corner(CYAN)
    move_if()
    
def turn_around():
    turn_left()
    turn_left()

def move_if():
    if front_is_clear():
        move()

def move_to_wall():
    while front_is_clear():
        move()

def clear_color():
    while front_is_clear():
        paint_corner(BLANK)
        move()
    paint_corner(BLANK)

def move_to_beeper():
    turn_around()
    while no_beepers_present():
        move()

if __name__ == '__main__':
    run_karel_program('Midpoint8.w')
