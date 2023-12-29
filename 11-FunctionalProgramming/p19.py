'''
19.	The final grades obtained by students in the "Economic Geography" course are included in the array:
[3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
Write a program that calculates the arithmetic mean of the grades, excluding negative grades (2.0). 
Use the filter() along with an anonymous function. Sample result:
Arithmetic mean for grades <> 2.0 is 3.85
'''
grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

mean = sum(list(filter(lambda x: x>2.1, grades)))/len(list(filter(lambda x: x>2.1, grades)))

print(mean)