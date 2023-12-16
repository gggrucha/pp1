'''
22.	Create a program that computes the second power of each array element. Sample result:
Array: 8 2 5 1 9
2nd power: 64 4 25 1 81
'''
arr = [8, 2, 5, 1, 9]

def le_programme(array):

    # wyświetlenie listy początkowej
    print('Array: ', end='')
    for element in array:
        print(str(element), end=' ')
    print()
    # wyświetlenie listy końcowej
    print('2nd power: ', end='')
    for element in array:
        print(str(element**2), end=' ')

le_programme(arr)