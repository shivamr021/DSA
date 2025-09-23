from os import *
from sys import *
from collections import *
from math import *

class Rectangle:
    def __init__(self, length=0, breadth=0):
        # store the values of length and breadth
        self.length = length
        self.breadth = breadth

    def getArea(self):
        # calculate and return area
        return self.length * self.breadth

