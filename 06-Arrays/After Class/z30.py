'''
30.	Create a program that sorts elements of an array containing integer numbers. Apply the Bubble Sort sorting algorithm. 
Define a function bubblesort(array) that returns the sorted array. Try to sort and display any three arrays.
'''

array = [5,3,6,1]
n = len(array) #4
for i in range(n): #0,1,2,3
    for j in range(0,n-i-1): # gdy i=0 to: 
        if array[j] > array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
print(array) 