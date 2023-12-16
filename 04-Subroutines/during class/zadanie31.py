def f(x,y):
    wynik = 0
    for num in range(x,y):
        if num%2==0 and num<0:
            wynik+=1
    return wynik

print(f(-7,8),f(-1,11))
