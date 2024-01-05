'''
20.	An array contains numbers from 1 to 20. Write a program that calculates and displays their third power. 
Use the map() and an anonymous function.
'''
array = [i for i in range(1,21)]
print(list(map(lambda x: x**3,array)))