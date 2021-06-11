# Multiple Inheritance

class User():
    def sign_in_method(self):
        print('You are logged on')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack_power(self):
        print(f'You are attacking with power {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack_arrows(self):
        print(f'You are attacking with {self.arrows} arrows.')


class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


obj1 = Hybrid('mmm', 10, 1000000)

obj1.attack_arrows()
obj1.attack_power()
obj1.sign_in_method()
