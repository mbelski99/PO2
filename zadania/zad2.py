from random import randint

class Coin(object):

    def __init__(self):
        self.side=0
        self.throw()

    def throw(self):
        self.side=randint(0,1)

    def showSide(self):
        if self.side:
                print("orzeł")
        else:
            print("reszka")

c1=Coin()
c2=Coin()
c5=Coin()
sum=0
wins=0
for x in range(1000):
    while sum < 20:
        c1.throw()
        c2.throw()
        c5.throw()
        if c1.side:
         sum += 1
        if c2.side:
            sum += 2
        if c5.side:
         sum += 5
    else:
        if sum == 20:
            wins += 1
    sum=0
print(wins)