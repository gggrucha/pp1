'''
16.	An array contains values: [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]. 
Create a program that calculates the sum of all odd numbers
'''
arr = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
suma=0
for row in arr:
    for item in row:
        if item%2!=0:
            suma+=item
print(suma)