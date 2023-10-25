'''
24.	Vehicle registration numbers in Kraków start with the letters KR or KK. 
Write a program that checks whether the vehicle registration number entered from the keyboard means 
a vehicle from Krakow. 
Display True whether a car is from Kraków or False otherwise. 
Sample result:
Enter vehicle registration number: KR45091
Car from Kraków: True
'''
rej = input('rej: ')
if ('KR' or 'KK') in rej:
    print('Car from Kraków: True')
else:
    print('Car from Kraków: False')