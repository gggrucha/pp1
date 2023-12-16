'''
43.	A text contains any number of words. 
Define a function f(name) that returns the acronym (first letters of all words). 
Sample result:
f("Internet of Things") returns "IoT"
f("For Your Information") returns "FYI"
f("Python") returns "P"
'''
def f(name):
    wynik = ''
    lista = name.split(' ')
    for item in lista:
        wynik+=item[0]
    return wynik

print(f("Internet of Things"))
print(f("For Your Information"))
