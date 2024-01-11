'''
Create a function f(x,y,digit) that returns how many times the given digit appears in numbers in the range from x to y. 
Example:
f(10,15,1)  7
f(28,32,2)  3
f(100,105,6)  0
f(100,101,0)  3
'''
def f(x,y,digit):
    counter = 0
    for num in range(x,y+1):
        for cyferka in str(num):
            if str(digit)==cyferka:
                counter+=1
    return counter

print(f(10,15,1))
print(f(28,32,2))
print(f(100,105,6))
print(f(100,101,0))