'''
17.	An array contains values: [[0,0,0],[0,0,0],[0,0,0]]. 
Create a program that replaces the values of the main diagonal with 1. 
Use loop statements. Display the modified array. Sample result:
1 0 0
0 1 0
0 0 1
'''
array = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,len(array)):
    array[i][i] = 1


for row in array:
    line=''
    for item in row:
        line+=str(item)+' '
    print(line)