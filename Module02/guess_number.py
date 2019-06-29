import random

print('----------------------------------------')
print('        GUESS THAT NUMBER GAME')
print('----------------------------------------')
print()

number = random.randint(0,100)
guess = -1

name = input('Player what is your name? ')

while guess !=number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < number:
        print('Sorry {}, your guess of {} was too LOW. Play again?'.format(name, guess))
    elif guess > number:
        print('Sorry {}, your guess of {} was too HIGH. Play again?'.format(name, guess))
    else:
        print('Excellent work {}, you won, it was {}!'.format(name, guess))

print('done')