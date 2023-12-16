'''
40.	The array contains integer 8 numbers in the range 1 to 999. 
Write a program that displays elements of the array formatted as below.
-----------------------------------------
|   1|  23|   5| 382|   1|  17|   4| 906|
-----------------------------------------
'''
array = [1,23,5,382,1,17,4,906]
max_size = len(str(max(array)))+1  # w tym wypadku 4

for i in range(len(array)):
    print(f'|{array[i]:>{max_size}}',end='')
print('|')  # końcowy