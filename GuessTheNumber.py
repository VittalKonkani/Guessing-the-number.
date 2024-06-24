# Guessing-the-number.
import random
secretnum= random.randint(1,5)
count=1
while True:
    guess=int(input("Guess any number between 0 and 5   "))
    if guess==secretnum:
        print("You guessed it right!. Congrats . Then when is the party?")
        break
    else:
        print("Kindly try again!")
        count += 1

print(f"You took {count} chances to guess it right")
