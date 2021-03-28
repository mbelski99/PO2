import random
    class Die:
        def __init__(self, sides):
            self._sides = sides
            self._value = None

        def roll(self):
            self._value = random.randint(1,self._sides)

        def get_sides(self):
            return self._sides

        def get_value(self):
            return self._value

    playerDie = Die(6)
    compDie = Die(6)
    playerSum = 0
    compSum = 0

    while True:
        playerDie.roll()
        compDie.roll()
        playerSum += playerDie.get_value()
        compSum += compDie.get_value()
        print (f"\nWartosc oczek gracza: {playerSum}")
        if(playerSum > 21):
            break
        answer = input("Czy chcesz rzucic kolejny raz? T/N").upper()
        if(answer == "T"):
            while(compSum < 19):
                compDie.roll()
                compSum += compDie.get_value()
            break

    if (playerSum <=21 and playerSum > compSum and compSum<=21) or (compSum > 21 and playerSum<=21):
        print(f'\n\ntwoj wynik: {playerSum} , wynik komputera: {compSum}. WYGRALES!!!\n\n')
    elif sum_komp==sum_gracz:
        print(f'\n\ntwoj wynik: {playerSum} , wynik komputera: {compSum}. REMIS!!!\n\n')
    else:
       print(f'\n\ntwoj wynik: {playerSum} , wynik komputera: {compSum}. PRZEGRALES!!!\n\n')