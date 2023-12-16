import math
print(dir(math))

s = 'Aa'
print(min(s),max(s))

print(math.log(math.e))

def addtwo (a, b):
    added = a + b
    return added
addtwo (3, 5)
print (addtwo (3, 5))

g = lambda x,y: x+y
print(g(1,2))