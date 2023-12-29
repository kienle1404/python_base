# A robot moves in a plane starting from the original point (0,0). The robot can move toward
# UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance
# from current position after a sequence of movement and original point. If the distance is a
# float, then just print the nearest integer.
# Example: If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be: 2. Because the position after all run all
# movements above is [2, 1]
# Hints: Using sqrt to calculate the distance

from math import sqrt

def compute_distance(movements:tuple)->int:
    x = 0
    y = 0
    for movement in movements:
        direction, step = movement.split()
        step = int(step)
        if direction == "UP":
            y += step
        elif direction == "DOWN":
            y -= step
        elif direction == "RIGHT":
            x += step
        elif direction == "LEFT":
            x -= step
    distance = int(sqrt(x*x + y*y))
    return distance

movements = ("UP 5", "DOWN 3", "LEFT 3", "RIGHT 2")
print(compute_distance(movements))