'''
20.	An array contains integer numbers: 34,7,19,4,21,8. 
Create a program that calculates and displays the number of even values in the array. 
Use the 'while' loop statement.
'''
arr = [34,7,19,4,21,8]

def even_values_in_array(array):
    evens = 0 # number of even values
    n = 0
    while n<len(array):
        if array[n]%2==0:
            evens+=1
        n+=1
    return evens
print(even_values_in_array(arr))