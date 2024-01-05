'''
29.	At one of the Olympic Games, the medal classification is as follows:
{"country":"Denmark","gold":2,"silver":4,"bronze":6}
{"country":"Finland","gold":5,"silver":0,"bronze":4}
{"country":"USA","gold":12,"silver":5,"bronze":11}
{"country":"Peru","gold":0,"silver":1,"bronze":7}
Write a program that creates a bar chart showing the total number of medals won by each country. 
Add a title for the chart and descriptions for the x and y axes. 
Tip: Use the map() function to create arrays of data for your chart
'''
ogames = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
{"country":"Finland","gold":5,"silver":0,"bronze":4},
{"country":"USA","gold":12,"silver":5,"bronze":11},
{"country":"Peru","gold":0,"silver":1,"bronze":7}]

x = list(map(lambda x:x['gold']+x['silver']+x['bronze'],ogames))
print(x)
y = list(map(lambda x:x['country'],ogames))
print(y)

import matplotlib.pyplot as plt

plt.plot(y,x, 'o:r')
plt.show()