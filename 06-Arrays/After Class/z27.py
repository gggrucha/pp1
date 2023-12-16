'''
27.	An array contains integer numbers: 12, 6, 4, 9, 10. 
Create a program that displays the array values graphically as below. 
Define a function star(n) that returns the given number of asterisks as a string. Use a defined function in the program.
12: ************
 6: ******
 4: ****
 9: *********
10: **********
'''
arr = [12, 6, 4, 9, 10]
max_width = len(str(max(arr)))  # największa liczba w liście (służy do wyrównywania przy printowaniu)

def star(n):
    return '*'*n

for number in arr:
    print(f'{number:>{max_width}}: {star(number)}')