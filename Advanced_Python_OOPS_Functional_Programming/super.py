# super() is the function which can be used to call the methods of the parent class.

class User():
    def __init__(self, email):
        self.email = email

    def sign_in_method(self):
        print('You are logged on')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'You are attacking with power {self.power}')


class Archer(User):
    def __init__(self, name, arrows, email):
        super().__init__(email)
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'You are attacking with {self.arrows} arrows.')


player1 = Wizard('Manish', 27, 'mmm@gmail.com')
player2 = Archer('Gandhi', 27, 'gggg@gmail.com')

print(player1.email)
print(player2.email)
