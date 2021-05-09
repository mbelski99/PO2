import functools

class Fraction:
    def nwd(x,y):
        x= abs(x)
        y= abs(y)
        while x != 0:
            x,y = y %x,x
        return y

    def __init__(self,numerator, denominator):
        divisor = Fraction.nwd(numerator,denominator)
        self.numerator = (1 if denominator > 0 else -1)* numerator//divisor
        self.denominator = abs(denominator)// divisor

    def __getitem__(self, item):
        if item == 0:
            return self.numerator
        elif item == 1:
            return self.denominator
        else:
            raise IndexError

    def __repr__(self):
        return f"{type(self).__name__}({self.numerator},{self.denominator})"

    def __str__(self):
        return f"{self[0]}/{self[1]}"
    def __add__(self, other):
        return Fraction(self[0] * other[1] + self[1] * other[0], self[1] * other[1])
    def __sub__(self, other):
        return Fraction(self[0] * other[1] - self[1] * other[0], self[1] * other[1])
    def __mul__(self, other):
        return Fraction(self[0] * other[1], self[1] * other[1])
    def __truediv__(self, other):
        return Fraction(self[0] * other[1], self[1] * other[1])
    def __eq__(self, other):
        return not (self - other)[0]
    def __lt__(self, other):
        return (self - other)[0] < 0
    def __float__(self):
        return self[0]/self[1]
    def __int__(self):
        return self[0]//self[1]


f1 = Fraction(1,2)
f2 = Fraction(4,5)
print(f1+f2)
print(repr(f1-f2))