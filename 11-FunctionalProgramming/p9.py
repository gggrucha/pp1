'''
9.	Write a program that converts speed in meters per second to speed in kilometers per hour. 
Use an anonymous function. Sample result:
10 m/s = 36 km/h
35 m/s = 126 km/h
'''
metry = 10
a = lambda x: x*3.6
print(f'{metry} m/s = {int(a(metry))} km/h')