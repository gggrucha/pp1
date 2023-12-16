'''
20.	Write a program that converts any natural number to a binary number. Use the stack. 
To convert a number, divide the number by 2, each time taking the remainder of the division and putting the remainder on the stack. 
Repeat the division until the number you are dividing is zero. 
Then pop and display all values from the stack. Sample result for number 18:
'''
import stack
num = 18

while num!=0:
    t=num//2 
    remainder = num - t*2  # reszta z dzielenia
    stack.push(remainder)
    num=t

for i in range(len(stack.stack)-1,-1,-1):
    print(stack.pop())