class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.tiredness = 0

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
        self.tiredness += 1

    @property
    def mood(self):
        happiness = self._hunger + self._tiredness
        if happiness < 5:
            return "zadowolony"
        elif happiness < 11:
            return "podenerwowany"
        else:
            return "wściekły"

    def talk(self):
        self._passage_of_time
        print(self.happiness)

    def eat(self, food=4):
        self._passage_of_time
        self.hunger -= food

    def play(self, fun=4):
        self._passage_of_time
        self.tiredness -= fun

    pass


if __name__ == '__main__':
    pet1 = Pet("Burek")