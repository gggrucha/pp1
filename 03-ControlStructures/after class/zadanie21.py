a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

if a>b:
    a,b=b,a

print(f'Numbers in ascending order: {a}, {b}')
