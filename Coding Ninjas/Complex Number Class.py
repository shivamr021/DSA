from os import *
from sys import *
from collections import *
from math import *

class ComplexNumbers:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def plus(self, other):
        self.real = self.real + other.real
        self.imag = self.imag + other.imag

    def multiply(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        self.real = real_part
        self.imag = imag_part

    def print(self):
        print(f"{self.real} + i{self.imag}")


# Driver code
if __name__ == "__main__":
    r1, i1 = map(int, input().split())
    r2, i2 = map(int, input().split())
    choice = int(input())

    c1 = ComplexNumbers(r1, i1)
    c2 = ComplexNumbers(r2, i2)

    if choice == 1:
        c1.plus(c2)
        c1.print()
    elif choice == 2:
        c1.multiply(c2)
        c1.print()
