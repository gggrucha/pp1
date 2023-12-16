'''
51.	A two-dimensional array of the size 3 by 5 contains integer numbers. 
Create a program that swaps the first and the last row. 
Display array values in rows and columns before and after changes.
'''
arr = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7]]  # trzy wiersze, pięć kolumn

def swap(array):
    brray = array.copy()
    brray[0],brray[len(brray)-1] = brray[len(brray)-1],brray[0]  # swap wartości

    return f'Before changes: {array}\nAfter changes: {brray}'

print(swap(arr))