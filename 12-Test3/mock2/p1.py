'''
Create a function f(n) that returns the difference between the largest and smallest odd digit contained in the number n. 
When the number n does not contain odd digits, the function returns -1. Example:
f(10852)  4
f(7235973)  6
f(4388)  0
f(846206)  -1
'''
def f(n):
    lista = list(str(n))
    lista = list(filter(lambda x: int(x)%2==1,lista))
    print(lista)
    maxi=max(lista)
    mini=min(lista)
    return int(maxi)-int(mini)

print(f(10852))