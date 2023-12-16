'''
9.	An array contains values: 2, 3, 7, 5, 4. Create a program that displays:
a.	the array
b.	number of elements
c.	first value
d.	second value
e.	last value
f.	last but one value (do not use negative index values)
g.	sum of the first and last value
h.	middle value
i.	all array values separated by a single space (use a loop statement)
j.	first half of the array values, separated by a single space (use a loop statement)
'''
array = [2,3,7,5,4]
print('the array',array)
print('number of elements',len(array))
print('first value',array[0])
print('second value',array[1])
print('last value',array[-1])
print('last but one value (do not use negative index values)',array[len(array)-2])
print('sum of the first and last value',array[0]+array[-1])
print('middle',array[int((len(array)-1)/2)])

for item in array:
    print(item, end=' ')
print()
for i in range(0, len(array)-1):
    if i<len(array)/2:
        print(array[i], end=' ')