'''
23.	An array contains numbers: -15, 8, -31, 47, -2, 19. 
Create a program that finds and displays the maximum and minimum number. Do not use available functions.
'''
# nie można używać min() i max()
arr = [-15, 8, -31, 47, -2, 19]

def min_max(array):
    min = array[0]
    max = array[1]
    if min>max: # jeśli minimum większe od maximum to zmieniamy je 
        min,max = max,min

    for i in range(2,len(array)): #zaczynamy od trzeciego elementu bo dwa pierwsze sprawdziliśmy
        if array[i] < min:
            min = array[i]
        elif array[i] > max:
            max = array[i]
    return f'min: {min}, max: {max}'

print(min_max(arr))