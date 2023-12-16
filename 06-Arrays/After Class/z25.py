'''
25.	An array contains values: 15, 8, 31, 47, 2, 19. 
Create a program that calculates and displays the array and the arithmetic mean of array values. 
Use the “while” loop statement
'''

arr = [15, 8, 31, 47, 2, 19]

def array_and_arythmetic_mean(array):
    arythmetic_mean = 0
    i = 0
    while i<len(array):
        arythmetic_mean+=array[i]
        i+=1
    arythmetic_mean/=len(array) 
    return f'Array: {array}\nArythmetic mean: {arythmetic_mean}'

print(array_and_arythmetic_mean(arr))