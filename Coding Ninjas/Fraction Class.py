from math import gcd

class Fraction:
    def __init__(self, num, den):
        self.numerator = num
        self.denominator = den
        self.simplify()

    def add(self, f2):
        # a/b + c/d = (ad + bc)/bd
        new_num = self.numerator * f2.denominator + f2.numerator * self.denominator
        new_den = self.denominator * f2.denominator
        self.numerator = new_num
        self.denominator = new_den
        self.simplify()

    def multiply(self, f2):
        # a/b * c/d = (ac)/(bd)
        new_num = self.numerator * f2.numerator
        new_den = self.denominator * f2.denominator
        self.numerator = new_num
        self.denominator = new_den
        self.simplify()

    def simplify(self):
        g = gcd(self.numerator, self.denominator)
        self.numerator //= g
        self.denominator //= g

    def print(self):
        print(f"{self.numerator}/{self.denominator}")


# Driver code
if __name__ == "__main__":
    # First fraction
    num, den = map(int, input().split())
    f1 = Fraction(num, den)
    
    q = int(input())  # number of queries
    for _ in range(q):
        arr = list(map(int, input().split()))
        t, num2, den2 = arr[0], arr[1], arr[2]
        f2 = Fraction(num2, den2)
        if t == 1:  # add
            f1.add(f2)
            f1.print()
        elif t == 2:  # multiply
            f1.multiply(f2)
            f1.print()
