'''
26.	Write a program that checks whether the number entered from the keyboard is even. 
Display True when the number is even and False when the number is odd. Sample result:
Enter number: 34
Number is even: True
'''
num = int(input('Enter number: '))
if num%2==0:
    even = True
else:
    even = False
print(f'Number is even: {even}')