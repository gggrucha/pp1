'''
42.	Define the function f(number1,number2,number3), 
which returns the difference between the largest and smallest numbers. Sample result:
f(7,4,9) returns 5
f(2,12,8) returns 10
'''
def f(num1,num2,num3):
    
    lista = [num1,num2,num3]
    lista= sorted(lista)
    wynik = abs(lista[0] - lista[2])
    return wynik

print(f(7,4,9))
print(f(2,12,8))