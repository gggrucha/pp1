def f(n):
    line = ''
    if n == 0:
        return 'Error'
    if n == 1:
        return str(n)
    for i in range (1,n+1):
        line+=str(i)
    return line

print(f(2))