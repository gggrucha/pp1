'''
41.	Write a program that checks whether the first array is a subset of the second one 
(whether all elements of the first array appear in the second array).'''
# Podzbiór oznacza, że każdy element zbioru B musi być również elementem zbioru A
first = []
second = []

for element in first:
    if element not in second:
        print(False)
