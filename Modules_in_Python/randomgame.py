from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))
# print(answer)

while True:
    try:
        guess = int(input('Please enter a number from 1 - 10: '))
        if 0 < guess < 11:
            if int(guess) == answer:
                print('Hey you are a genius')
                break
        else:
            print('Hey Domino, I said 1 ~ 10')
            continue
    except ValueError:
        print('Please enter a number between 1 ~10')

# generate a number from 1 - 10
# get input from user
# check that input is from 1 - 10
# check if number is the right guess otherwise ask again.
