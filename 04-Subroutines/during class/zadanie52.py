def power(x,n):
    wynik = 1
    while n>=1:
        wynik = wynik*x
        n=n-1
    return wynik

print(power(3,4))