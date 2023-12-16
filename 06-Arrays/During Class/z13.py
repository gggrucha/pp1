'''
13.	An array contains integer numbers: [34,7,19,4,21,8]. 
Create a program that calculates and displays the number of even values in the array. 
Use the 'while' loop statement.
'''
array = [34,7,19,4,21,8]
i=0
evenki=0
while i<len(array):
    if array[i]%2==0:
        evenki+=1
    i+=1
print(evenki)