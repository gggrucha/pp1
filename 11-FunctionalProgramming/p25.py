'''
25.	Measuring stations recorded the following temperatures in degrees Celsius:
{"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
Write a program that displays the names of towns where positive temperatures were recorded. 
Use anonymous and filter() functions. Sample result:
Cities with positive temperatures: Krakow Sopot Opole
'''
dic = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

posytive = list(filter(lambda x: dic[x]>0,dic.keys()))
print('Cities with positive temperatures:',posytive)