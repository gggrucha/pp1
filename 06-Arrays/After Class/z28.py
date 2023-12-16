'''
28.	Define a function compare(array1, array2) that returns True if both arrays are the same or False otherwise.  
Two arrays are the same if they have the same number of elements and values of elements in cells of arrays with the same index are equal. 
Then create a program and try to compare the following arrays: 
a.	["water","book","sky"]   ["water","book","sky"]
b.	[True,False]   [True,False,True]
c.	[5,3,1]   [5,3,1]
d.	[3,2,1]   [3,2]
Display both arrays and the result of comparison. Sample result:
Array1: water book sky
Array2: water book sky
Comparison: arrays are the same

'''

def compare(array1,array2):
    if len(array1)!=len(array2):
        return False
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

print(
compare(["water","book","sky"], ["water","book","sky"]),
compare([True,False],   [True,False,True]),
compare([5,3,1],[5,3,1]),
compare([3,2,1],[3,2])
)