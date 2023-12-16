'''
18.	An array contains values: [[True,False],[True,True],[False,False]]. 
Create a program that changes values of an array to the opposite. Use a loop statement. Sample result:
[[False,True],[False,False],[True,True]]
'''
array = [[True,False],[True,True],[False,False]]

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == True:
            array[i][j] = False
        else: 
            array[i][j] = True
print(array)
