'''
44.	Write a program that calculates the sum and arithmetic mean of numbers entered from the keyboard. 
Entering 0 ends entering numbers. Sample result
Enter number: 15
Enter number: 8
Enter number: 10
Enter number: 0
RESULT: Quantity=3, Sum=33, Mean=11
'''
lista = []
while True:
    num = int(input('Enter number: '))
    if num == 0:
        break

    lista.append(num)
print('dziala?')
print(f'RESULT: Quantity={len(lista)}, Sum={sum(lista)}, Mean={sum(lista[:len(lista)])/len(lista)}')