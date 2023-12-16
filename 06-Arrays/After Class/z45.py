'''
45.	Write a program that draws the function y = sin(x) for an angle value in the range 0-360 degrees
'''

import matplotlib.pyplot as plt
import math

x = [i for i in range(0,361)]
y = [] 
for n in x: 
    y += [math.sin(n)]  # n to element listy x

plt.plot(x,y, 'o:r')
plt.show()