'''
12.	An array contains integer numbers: [34,7,19,4,21,8]. 
Create a program that calculates and displays the number of even values in the array. 
Use the 'for' loop statement.
'''
array=[34,7,19,4,21,8]
evenki=0
for num in array:
    if num%2==0:
        evenki+=1
print(evenki)