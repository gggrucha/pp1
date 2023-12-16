def f(num1,num2,operator):
    if operator == '+':
        return num1+num2
    if operator == '%':
        return num1%num2
    if operator == '**':
        return num1**num2
    if operator == '*':
        return num1*num2
    if operator == '-':
        return num1-num2
    
print(
f(2,3, "+"),
f(2,3, "%"),
f(2,3, "**"),
f(2,3, "*"),
f(2,3, "-"),
)
    