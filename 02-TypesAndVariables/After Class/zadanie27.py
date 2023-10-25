'''27.	Write a program that checks whether the number entered from the keyboard is between -10 and 10. 
Display True if the number is in the given range, and False otherwise. Sample result: 
Enter number: 17
Number in the range <-10,10>: True
'''

num = float(input('Enter number: '))
if num >= -10 and num <= 10:
    num_in_range = True
else:
    num_in_range = False
print(f'Number in the range <-10,10>: {num_in_range}')