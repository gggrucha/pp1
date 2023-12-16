'''
53.	In mathematics, a matrix is a rectangular array or table of numbers, symbols, or expressions, arranged in rows and columns, e.g.:
-7  12 38
41 -19 11
Create a function identity_matrix(n) that returns an identity matrix (2D array) of size n (https://en.wikipedia.org/wiki/Identity_matrix). 
Then, create a function that displays a 2D array in rows and columns. 
Finally, create a program that displays three identity matrices with dimensions of 3, 5 and 8. 
Sample result:
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
'''

def identity_matrix(n):
    arr = [[0 for b in range(n)] for a in range(n)]  # zrobienie pustej macierzy 
    for i in range(n):
        for j in range(n):
            if i == j :
                arr[i][j] = 1
    return arr


def displaya(arr):
    for i in range(len(arr)):
        line = ''
        for j in range(len(arr[i])):
            line+=str(arr[i][j]) + ' '
        print(line)
    print()


displaya(identity_matrix(3))
displaya(identity_matrix(5))
displaya(identity_matrix(8))
