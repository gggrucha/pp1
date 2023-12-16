'''
48.	A function create_2d_arr(x,y) creates and returns two dimensional array with values of 0. 
Create a program and the function. 
Then create a two-dimensional array with dimensions of 3 by 5. Display the created array.
'''

def create_2d_arr(x,y):
    arr = []
    for row in range(x):
        arr.append([])
    for row in arr:
        for cos in range(y):
            row.append(0)
    return arr

print(create_2d_arr(3,5))