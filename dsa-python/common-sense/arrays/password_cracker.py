from random import *
import time

password = input (" password: ")
letters = ["a", "b", "c", "d", "e", "f",   "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
counter = 0
guess = ""
start = time.perf_counter()
while (guess != password):
    guess = ""
    for letter in password:
        guessletter = letters[randint(0,25)]
        guess = str(guessletter) + str(guess)

    print(f'attempt # {counter} - guess = {guess}')
    if(guess == password):
        print(f'matched: {guess} in {counter} attempts')
        stop = time.perf_counter()
        break
    counter += 1

print( f'password guessed in {stop - start:0.2f} seconds')