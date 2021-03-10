"""
Generates a random number between 1 and 20. The player has to guess
the number generated. The player will be given clues depending on
whether the number entered is greater or lower than the randomly
generated.

Axel, Marcel
"""


import random


number = int(random.uniform(1,20))

guess = False

while not guess:
  print("Guess number between 1 and 20.")
  try:
    #guesed_number = int(raw_input()) #for py2
    guesed_number = int(input()) #for py3

    if guesed_number == number:
      print("You win! Well done.")
      guess = True
    elif guesed_number < number:
      print("Try with a bigger number.")
    elif guesed_number > number:
      print("Try with a smaller number.")


  except ValueError:
    print("Only numbers are admitted.")
