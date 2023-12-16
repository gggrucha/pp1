'''
45.	An expression contains operators for adding and subtracting single-digit numbers. 
Define a function f(expression) that returns the value of the expression. Sample result:
f("2+3") returns 5
f("3+8+1") returns 12
f("2+3-4+5-0") returns 6
'''
def f(expression):
    wynik=int(expression[0])
    for i in range (0,len(expression)-1): # -1 żeby nie wyleciało z range
        if expression[i] == '+' or expression[i] == '-':
            if expression[i] == '+':
                wynik= wynik + int(expression[i+1])
            elif expression[i] == '-':
                wynik = wynik - int(expression[i+1])
    return wynik

print(f('2+3'))
print(f('2+3-4+5-0'))