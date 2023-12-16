'''
52.	A two-dimensional array of the size 3 by 5 contains integer numbers. 
Create a program that swaps the first and the last column. 
Display array values in rows and columns before and after changes
'''

def swap(array):
    for i in range(len(array)):  # 0,1,2
        array[i][0], array[i][4] = array[i][4],  array[i][0]  # zamiana zerowego i czwartego elementu array[i,len(array[i])-1]
    return array


arr = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7]]
print(swap(arr))