'''
31.	Write a program that enables a user to challenge a computer. 
The computer throws dice. 
Then, the user then tries to guess the number from dice by entering a number from 1 to 6 from the keyboard. 
If the user has guessed the number from the dice, the computer displays True. 
Otherwise, the computer displays False.
'''
import random
a = random.randrange(1,7)
b = int(input('Zgadnij liczbę'))
if a == b:
    print('True')
else:
    print('False')
