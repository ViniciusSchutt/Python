# This is a simple but fun guess the numer game
import random
name = str(input("Hello there, what is you name? "))
secretNumber = random.randint(1, 20)
print(f'Well, {name}, I am thinking of a number between 1 and 20.')

# ask the player to guess n times
n = int(input(f'So {name}, in how many tries you think you can guess my number?\n'))
for guessTaken in range(n):
    guess = int(input(f'Ok, take a guess then!'))
    if guess < secretNumber:
        print('Nope, your guess is too low.')
    elif guess > secretNumber:
        print('Nope, your guess is too high.')
    elif guess == secretNumber:
        print(f'Good job {name}! You read my m... I mean, you guessed my number in {guessTaken} times, nice!')
    else:
        print(f'Maximum tries {name}, sorry! The number I was thinking of was {secretNumber}.\n'
              f'Better luck next time, see ya =)')
