import random

print('----------------------------------------------')
print('           GUESS THAT PRIMER GAME')
print('----------------------------------------------')
print()

goal = random.choice('ACGT')
for i in range(4):
    goal += random.choice('ACGT')

guess = 'NNNNN'

name = input('Player what is your name? ')

while guess != goal:
    guess = input('Guess a 5 bp primer: ')

    misses = 0
    for i in range(len(guess)):
        if guess[i] != goal[i]:
            misses += 1
    if misses > 0:
        print('Sorry {}, you guessed {} bases wrong. Play again?'.format(name, misses))
    else:
        print('Excellent work %s, you won!' % name)

print('done')