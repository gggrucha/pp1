'''
56.	Create a function that convert two-dimensional (2D) array into 1D. 
Then create a program that displays 1D array for the following 2D arrays.
a.	2 3
1 5 
b.	5 0 3 7 5
9 0 9 1 2
c.	2 1
3 5
7 4
2 6
'''

twodim_arr1 = [[2, 3],[1, 5]]  # a
twodim_arr2 = [[5, 0, 3, 7, 5],[9, 0, 9, 1, 2]]  # b
twodim_arr3 = [[2, 1],[3, 5],[7, 4],[2, 6]]  # c

def twoToOneDim(matrix):
    array = []
    for list in matrix:
        for element in list:
            array.append(element)
    return array

print(twoToOneDim(twodim_arr1))
print(twoToOneDim(twodim_arr2))
print(twoToOneDim(twodim_arr3))