print("This is github learn class")

import random

number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("You guessed it right!")
else:
    print("Wrong guess. The number was:", number)



# This program prints a message and adds two numbers

print("Hello, world!")

a = 5
b = 3

sum = a + b

print("The sum is:", sum)
