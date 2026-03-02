from math import sqrt, pow

def distance(x1, y1, x2, y2) -> int:
    return int(sqrt(pow(x1-x2, 2) + pow(y1-y2, 2)))

def circle_condition(x, y, circle_x, circle_y, radius):
    return distance(x, y, circle_x, circle_y) <= radius