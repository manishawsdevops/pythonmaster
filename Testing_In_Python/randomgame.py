from random import randint


def run_guess(guess, answer):
    if 0 < guess < 11:
        if int(guess) == answer:
            print('Hey you are a genius')
            return True
    else:
        print('Hey Domino, I said 1 ~ 10')


if (__name__ == '__main__'):
    answer = randint(1, 10)

    while True:
        try:
            guess = int(input('Please enter a number from 1 - 10: '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('Please enter a number between 1 ~10')
            continue
