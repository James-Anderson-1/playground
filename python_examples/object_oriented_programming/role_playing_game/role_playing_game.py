class Player:
    def __init__(self, name):
        self.name = name

class Computer(Player):
    def __init__(self):
        super().__init__(name="NPC")


    def respond(self, player):
        print("Hello", player.name, "I am", self.name)


class User(Player):
    def __init__(self, name, level):
        super().__init__(name=name)
        self.level = level


    def greet(self):
        print("Hi! What is your name?")

class Extra(Player):
    def __init__(self, name, is_villian):
        super().__init__(name=name)
        self.is_villian =is_villian

    def test_print(self):
        print(self.name)
        print(self.is_villian)

computer = Computer()
user = User("James", 1)
user.greet()
computer.respond(user)