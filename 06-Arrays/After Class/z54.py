'''
54.	Create a function transpose_matrix(m) that returns transposed matrix m:
https://en.wikipedia.org/wiki/Transpose
'''

def transpose_matrix(matrix):
    mat = []  # transponowana
    for i in range(len(matrix)):
        mat.append([])  # tworzenie pustych miejsc 
    for j in range(len(matrix)): #0,1
        for h in range(len(matrix[j])): #0
            mat[h].append(matrix[j][h]) 
    
    return mat


matrix = [[1,2],[3,4]]
print(transpose_matrix(matrix))