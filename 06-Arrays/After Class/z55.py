'''
55.	Then, create a program that displays transposed matrices, in rows and columns, 
for the following matrices.
a.	1 2 3
4 5 6
7 8 9
b.	1 2 3 4 5
6 7 8 9 0
c.	5 6 7 8
'''
def transpose_matrix(matrix):
    mat = []  # transponowana
    for i in range(len(matrix)+1):
        mat.append([])  # tworzenie pustych miejsc 
    for j in range(len(matrix)): #0,1
        for h in range(len(matrix[j])): #0
            mat[h].append(matrix[j][h]) 
    
    return mat

def displaya(matrix):
    for i in range(len(matrix)):
        line = ''
        for j in range(len(matrix[i])):
            line+=str(matrix[i][j])
        print(line)

displaya(transpose_matrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))

