'''
26.	Measuring stations recorded the following temperatures in degrees Celsius:
{"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
Write a program that creates a bar chart showing temperatures recorded in cities. 
Add a title for the chart and descriptions for the x and y axes. 
Tip: use the map() function to create two arrays of data for the chart.
'''
dic = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
l1 = []
l2 = []
for k,v in dic.items():
    l1.append(k)
    l2.append(v)

print(l1)
print(l2)

import matplotlib.pyplot as plt

plt.plot(l1,l2, 'o:r')
plt.show()