def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        counter = n-2
        a = 0
        b = 1
        while counter>=0:
            t = b
            b = a + b
            a = t
            counter-=1
        return a
    
print(f(5),f(9))