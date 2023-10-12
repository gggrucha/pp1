'''
21.	A variable contains your height in cm. 
Write a program that displays your height both in cm and in feet and inches. Sample result:
I am 170cm tall, i.e. 5 feet and 7 inches
'''
height = 170

cale = height/2.54 # zmieniamy cm na cale (w tym przypadku 66.92913...)

stopy = cale//12 # liczba całkowita w tym przypadku 5.0 stóp

reszta = cale - stopy*12 # wynik to cale tzn. 5 stóp I 6.92.. CALI

print(f'I am {height}cm tall, i.e. {int(stopy)} feet and {int(round(reszta,0))} inches')