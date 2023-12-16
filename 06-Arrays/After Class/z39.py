'''
39.	Write a program to separate even and odd numbers of a given array of integers.
Put all even numbers first, and then odd numbers.
'''
array = [1,5,34,2,8,67]
print('Array: ', array)
odd_arr = []
even_arr = []
for element in array:
    if element %2==0:
        even_arr.append(element)
    elif element %2!=0:
        odd_arr.append(element)
array = even_arr+odd_arr
print('New array: ', array)