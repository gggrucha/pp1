'''
20.	Variables a and b contain two integer numbers.
 Write a program that calculates and displays the result of their division, 
 rounded down to the nearest whole number. Display also the remainder of the division. Sample result:
Number one: 17
Number two: 5
Division result: 3
Remainder: 2
'''
a = 19
b = 5
print(f'Number one: {a}\nNumber two: {b}\nDivision result:{a//b}\nRemainder: {a-a//b*b}')
