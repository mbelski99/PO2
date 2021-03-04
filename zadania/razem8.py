class Pet:

    def __init__(self, name, hunger=0, tirdness=0):
        self.name = name
        self.hunger = hunger
        self.tirdness = tirdness

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.length > 2 and value.isalpha():
            self._name = value
        else:
            print("nazwa powinna zawierać same litery oraz jej długość nie może być mniejsza niż 3")
            self._name = False

    def _passage_of_time(self):
        self.hunger += 1
        self.tirdness += 1

    @property
    def mood(self):

        happiness = self.hunger + self.tirdness
        if happiness < 5:
            m = "szczesliwy"
        elif happiness <= 10:
            m = "zadowolony"
        elif happiness <= 15:
            m = "podenerwowany"
        else:
            m = "wsciekly"
        return m

    def talk(self):
        print("nastrój:", self.mood)
        self._passage_of_time()

    def eat(self, food=4):
        while food > 3:
            food = int(input("ile jedzenia chcesz dac?"))
            if food > 3:
                print("za dużo")
            else:
                print("dzięki")
                self.hunger -= food
                if self.hunger < 0:
                    self.hunger = 0
                self._passage_of_time

    def play(self, fun=4):
        while fun > 3:
            fun = int(input("jak dlugo chcesz sie bawic?"))
            if fun > 3:
                print("za dużo")
            else:
                print("super")
                self.tirdness -= fun
                if self.tirdness < 0:
                    self.tirdness = 0
                self._passage_of_time


def main():
    pet1_name = input("Jak chcesz nazwac swojego pupila? ")
    name = name(pet1_name)
    pet1 = Pet(name)

    select = None
    while select != "0":
        print \
            ("""
		Symulator opieki nad wirtualnym zwierzakiem

		1 - Nastrój
		2 - Jedzenie
		3 - Zabawa
		0 - Zakończ
		""")

        select = input("Co chcesz zrobić: ")
        print()

        if select == "1":
            pet1.talk()
        elif select == "2":
            pet1.eat()
        elif select == "3":
            pet1.play()
        elif select == "0":
            print("Koniec")
        else:
            print("Nie wybrałeś żadnej opcji")


main()