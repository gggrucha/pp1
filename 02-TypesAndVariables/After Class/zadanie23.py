import math
'''23.	The length of the sides of the triangle is a, b and c.
 Write a program that calculates the area of the triangle (using the Heron formula) 
 and the triangle circumference. Read the values of the triangle sides from the keyboard. 
 Sample result:
Enter a: …
Enter b: …
Enter c: …
Triangle area: …
Triangle circumference: …
'''
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

po = (a + b + c)/2  #połowa boku trójkąta

area = math.pow(po*(po-a)*(po-b)*(po-c),2)
circumference = po*2

print(f'Triangle area: {area}')
print(f'Triangle circumference: {circumference}')