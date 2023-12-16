'''
50.	An array contains integer numbers: [[-38, 19], [5,40],[-7,11],[29,16]]. 
Create a program that finds the smallest and largest values in the array 
and in which row and column they are located
'''
arr = [[-38,19], [5,40],[-7,11],[29,16]]

def smallest(array):
    smal = arr[0][0]  # zakładam, że pierwszy element jest najmniejszy
    inde = (0,0)  # index tego elementu
    for i in range(len(array)):  # for row in array:
        for j in range(len(array[i])): 
            if smal > array[i][j]:    
                smal = array[i][j]
                inde = (i,j)
    return f'Smallest number: {smal}, with index: {inde}'

def largest(array):
    larg = arr[0][0]  # zakładam, że pierwszy element jest największy
    inde = (0,0)  # index największego
    for i in range(len(array)):
        for j in range(len(array[i])): 
            if larg < array[i][j]:    
                larg = array[i][j]
                inde = (i,j)
    return f'Largest number: {larg}, with index: {inde}'


print(smallest(arr))
print(largest(arr))