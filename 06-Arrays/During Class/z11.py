'''
11.	Create a program that displays the name of month for a given month number (1 to 12). 
Define a month(n) function that returns the name of month for the number n. 
Store month names in an array. 
Using defined function, display month names for the following month numbers: 1, 9, 12.
'''
def month(n):
    months = ['January','February','March,','April','May','June','July','August','September','October','November','December']
    return months[n-1]
print(month(1))
print(month(9))
print(month(12))