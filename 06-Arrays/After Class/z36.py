'''
36.	Write a program that counts the number of occurrences of any value from a tuple. Sample result:
Tuple: 50,20,40,50,30,50
Value: 50
Number of occurrences: 3
'''
occurencies = 0
t = 50,20,40,50,30,50
print('Tuple: ',t)
value = int(input('Value: '))
for element in t:
    if element == value:
        occurencies+=1
print('Number of occurencies: ', occurencies)