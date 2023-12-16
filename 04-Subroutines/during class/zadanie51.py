'''
51.	Define a function sum(n) that for the given natural number n calculates the 
sum of all natural numbers between 1 and n. 
Apply recursion. Then, create a program that calculates the sum of natural numbers in the range <1,10>.'''

def sum(n):
    t = n
    result = t
    while t>1:
        t-=1
        sum(t)
    return t

print(sum(1),sum(5),sum(-1))
