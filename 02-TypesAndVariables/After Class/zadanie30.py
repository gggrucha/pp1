'''
30.	In many games, the numbers one and six on dice have special meaning. 
Write a program that displays the number of dice rolled and the value True if the number rolled is 1 or 6. 
Sample result:
Dice rolled: 4
Special number: False
'''
import random
dice = random.randrange(1,7)
print('Dice:', dice)
print('Special number: True' if dice==1 or dice==6 else 'Special number: False')
