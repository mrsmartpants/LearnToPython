
# Do while will execute atleast once

# do
# Excutes this
# While Condition

# Guess a number between 1:10
# You guessed it right

import random

secretno = 7

while True:
    i = int(input("Enter a number between 1 to 10 "))
    if i == secretno:
        print("you guessed right")
        break



