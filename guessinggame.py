import random

random = random.randint(0, 49)
random += 1

print("Howdy!\n You have been invited to the guessing game.\n You have to guess a random number between 1 to 50 and if it matches the number by the computer you win.\n If not, try again.\n Good Luck!")

i = 100


while i != random:
    i = int(input("Enter a number between 1 to 50. "))


    if i == random:
        print("Well played brother.")
    print("The number is wrong. Try again.")
