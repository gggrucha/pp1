'''
21.	An array contains natural numbers: 15, 8, 31, 47, 2, 19. 
Create a program that displays the contents of the array in reverse order. Use any loop statement. Sample result:
existed array: 15 8 31 47 2 19 
reverse array: 19 2 47 31 8 15
'''
arr = [15, 8, 31, 47, 2, 19]

# mój działający
n = len(arr)-1  # ostatni element w liście
i = 0  # pierwszy element w liście 
while i<n:
    arr[n],arr[i] = arr[i],arr[n]
    i+=1
    n-=1
print(arr)

#chad lgpt
'''
reversed_array = []
for i in range (len(arr)-1, -1, -1):
    reversed_array.append(arr[i])
print(reversed_array)
'''

#alternatywny sposób (działa)
arr = arr[::-1]
print(arr)