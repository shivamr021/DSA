def middleOfThree(x: int, y: int, z: int):
    if (x > y and x < z) or (x > z and x < y):
        return x
    elif (y > x and y < z) or (y > z and y < x):
        return y
    else:
        return z
