'''
14.	An array contains values: [[2,5,4],[9,0,3]]. Create a program that displays:
a.	the array
b.	size of the array (number of rows and columns)
c.	value 5 from the array
d.	value 3 from the array
e.	second row of the array as below:
9 0 3
'''
array = [[2,5,4],[9,0,3]]
print(array)

# rozmiar macierzy
print(f'{len(array)}x{len(array[0])}')

print(array[0][1])
print(array[1][2])

for i in array[1]:
    print(i,end=' ')