from karel.stanfordkarel import *

"""
File: Doraemon.py
----------------------- 
Sadly, this can only work in dimensions 20 X 20....... :(
"""

def main():
    """
    Let's say "Hi!" to Doraemon..... ;)
    """
    row1()
    move_up_left()
    row2()
    move_up_right()
    row3()
    move_up_left()
    row4()
    move_up_right()
    row5()
    move_up_left()
    row6()
    move_up_right()
    row7()
    move_up_left()
    row8()
    move_up_right()
    row9()
    move_up_left()
    row10()
    move_up_right()
    row11()
    move_up_left()
    row12()
    move_up_right()
    row13()
    move_up_left()
    row14()
    move_up_right()
    row15()
    move_up_left()
    row16()
    move_up_right()
    row17()
    move_up_left()
    row18()
    move_up_right()
    row19()
    move_up_left()
    row20()

def row1():
    for i in range(3):
        move()
    paint_corner(BLACK)
    move()
    for i in range(9):
        paint_corner(RED)
        move()
    paint_corner(GRAY)
    move()
    for i in range(2):
        paint_corner(YELLOW)
        move()
    paint_corner(GRAY)
    move_to_wall()

def row2():
    for i in range(3):
        move()
    paint_corner(BLACK)
    move()
    for i in range(2):
        paint_corner(GRAY)
        move()
    for i in range(11):
        paint_corner(BLACK)
        move()
    move_to_wall()

def row3():
    for i in range(3):
        move()
    paint_corner(BLACK)
    move()
    for i in range(2):
        paint_corner(BLUE)
        move()
    paint_corner(BLACK)
    move()
    for i in range(10):
        move()
    paint_corner(BLACK)
    move_to_wall()

def row4():
    move()
    move()
    paint_corner(BLACK)
    move()
    for i in range(11):
        move()
    paint_corner(BLACK)
    move()
    for i in range(2):
        paint_corner(BLUE)
        move()
    paint_corner(BLACK)
    move_to_wall()

def row5():
    for i in range(2):
        move()
    paint_corner(BLACK)
    move()
    for i in range(2):
        paint_corner(BLUE)
        move()
    paint_corner(BLACK)
    move()
    for i in range(7):
        move()
    for i in range(6):
        paint_corner(BLACK)
        move()
    move_to_wall()

def row6():
    move()
    paint_corner(BLACK)
    move()
    move()
    move()
    paint_corner(BLACK)
    move()
    move()
    move()
    paint_corner(BLACK)
    move()
    for i in range(7):
        move()
    paint_corner(BLACK)
    move()
    for i in range(2):
        paint_corner(BLUE)
        move()
    paint_corner(BLACK)
    move_to_wall()

def row7():
    move()
    paint_corner(BLACK)
    move()
    for i in range(2):
        paint_corner(BLUE)
        move()
    paint_corner(BLACK)
    move()
    for i in range(4):
        move()
    for i in range(2):
        paint_corner(BLACK)
        move()
    for i in range(4):
        move()
    paint_corner(BLACK)
    move()
    for i in range(3):
        move()
    paint_corner(BLACK)

def row8():
    paint_corner(BLACK)
    move()
    for i in range(3):
        move()
    paint_corner(BLACK)
    move()
    for i in range(10):
        move()
    paint_corner(BLACK)
    move()
    for i in range(3):
        paint_corner(BLUE)
        move()
    paint_corner(BLACK)

def row9():
    paint_corner(BLACK)
    move()
    for i in range(3):
        paint_corner(BLUE)
        move()
    paint_corner(BLACK)
    move()
    for i in range(3):
        move()
    for i in range(3):
        paint_corner(BLACK)
        move()
    for i in range(4):
        move()
    paint_corner(BLACK)
    move()
    move()
    for i in range(2):
        paint_corner(BLACK)
        move()
    paint_corner(BLACK)

def row10():
    paint_corner(BLACK)
    move()
    for i in range(3):
        move()
    paint_corner(BLACK)
    move()
    for i in range(10):
        move()
    paint_corner(BLACK)
    move()
    for i in range(3):
        paint_corner(BLUE)
        move()
    paint_corner(BLACK)

def row11():
    paint_corner(BLACK)
    move()
    for i in range(3):
        paint_corner(BLUE)
        move()
    paint_corner(BLACK)
    move()
    for i in range(3):
        move()
    for i in range(3):
        paint_corner(BLACK)
        move()
    for i in range(3):
        move()
    paint_corner(GRAY)
    move()
    for i in range(3):
        move()
    paint_corner(BLACK)
    move()
    paint_corner(BLACK)

def row12():
    paint_corner(BLACK)
    move()
    for i in range(3):
        move()
    paint_corner(GRAY)
    move()
    paint_corner(RED)
    move()
    paint_corner(GRAY)
    move()
    for i in range(2):
        paint_corner(BLACK)
        move()
    for i in range(5):
        move()
    paint_corner(BLACK)
    move()
    for i in range(4):
        paint_corner(BLUE)
        move()
    paint_corner(BLACK)

def row13():
    paint_corner(BLACK)
    move()
    for i in range(5):
        paint_corner(BLUE)
        move()
    paint_corner(BLACK)
    move()
    for i in range(3):
        move()
    paint_corner(BLACK)
    move()
    move()
    move()
    paint_corner(GRAY)
    move()
    paint_corner(RED)
    move()
    paint_corner(GRAY)
    move()
    paint_corner(BLACK)
    move()
    move()
    paint_corner(BLACK)
    move()
    paint_corner(BLACK)

def row14():
    paint_corner(BLACK)
    move()
    paint_corner(BLUE)
    move()
    paint_corner(BLACK)
    move()
    move()
    move()
    paint_corner(GRAY)
    move()
    for i in range(4):
        move()
    for i in range(3):
        paint_corner(BLACK)
        move()
    for i in range(6):
        paint_corner(BLUE)
        move()
    paint_corner(BLACK)

def row15():
    move()
    paint_corner(BLACK)
    move()
    for i in range(7):
        paint_corner(BLUE)
        move()
    paint_corner(BLACK)
    move()
    for i in range(2):
        move()
    for i in range(2):
        paint_corner(BLACK)
        move()
    move()
    paint_corner(BLACK)
    move()
    move()
    paint_corner(BLUE)
    move()
    paint_corner(BLACK)
    move_to_wall()

def row16():
    move()
    paint_corner(BLACK)
    move()
    paint_corner(BLUE)
    move()
    for i in range(3):
        move()
    paint_corner(BLACK)
    move()
    for i in range(3):
        move()
    paint_corner(BLACK)
    move()
    for i in range(7):
        paint_corner(BLUE)
        move()
    paint_corner(BLACK)
    move_to_wall()

def row17():
    for i in range(2):
        move()
    paint_corner(BLACK)
    move()
    for i in range(7):
        paint_corner(BLUE)
        move()
    paint_corner(BLACK)
    move()
    for i in range(2):
        move()
    paint_corner(BLACK)
    move()
    move()
    move()
    paint_corner(BLUE)
    move()
    paint_corner(BLACK)
    move_to_wall()

def row18():
    for i in range(3):
        move()
    for i in range(2):
        paint_corner(BLACK)
        move()
    for i in range(2):
        paint_corner(BLUE)
        move()
    for i in range(2):
        paint_corner(BLACK)
        move()
    for i in range(7):
        paint_corner(BLUE)
        move()
    paint_corner(BLACK)
    move_to_wall()

def row19():
    for i in range(4):
        move()
    for i in range(2):
        paint_corner(BLACK)
        move()
    for i in range(8):
        paint_corner(BLUE)
        move()
    for i in range(2):
        paint_corner(BLACK)
        move()
    move_to_wall()

def row20():
    for i in range(6):
        move()
    for i in range(8):
        paint_corner(BLACK)
        move()
    move_to_wall()

def move_to_wall():
    while front_is_clear():
        move()

def move_up_left():
    turn_left()
    move()
    turn_left()

def move_up_right():
    turn_right()
    move()
    turn_right()

def turn_right():
    turn_left()
    turn_left()
    turn_left()



if __name__ == "__main__":
    run_karel_program()
