'''
24.	An array contains values: 15, 8, 31, 47, 2, 19. 
Create a program that calculates and displays the array and the arithmetic mean of array values. 
Use the “for” loop statement
'''
arr = [15, 8, 31, 47, 2, 19]

def array_and_arithmetic_mean(array):
    # liczenie średniej arytmetycznej
    arythmetic_mean = 0
    for element in array:
        arythmetic_mean+=element
    arythmetic_mean/=len(array)

    return f'Array: {array}\nArythmetic mean: {arythmetic_mean}'

print(array_and_arithmetic_mean(arr))