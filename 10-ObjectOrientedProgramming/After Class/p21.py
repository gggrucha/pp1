'''
21.	Write a program containing a Statistics class that describes the properties of any set of numbers. The class should allow to:
a.	Add to the set of numbers, the next number read from the keyboard (store the numbers in the array)
b.	Display all numbers separated by a space
c.	Determine the greatest number
d.	Determine the smallest number
e.	Calculate the arithmetic mean of numbers
f.	Calculate of the median
g.	Display of calculated / determined statistical quantities (minimum, maximum, arithmetic mean, median)
Then, use the program for numbers:
12, 37, 6, 9, 17 
'''

class Statistics():
    def __init__(self,array_of_nums) -> None:
        self.array = array_of_nums

    def add(self):  # a
        value = input('Podaj liczbę jaką chcesz dodać do listy: ')
        self.array+=value

    def __str__(self):  # b
        line = ''
        for num in self.array:
            line+=str(num)+' '
        return line
    
    def greatest(self):  # c
        return max(self.array)

    def smallest(self):  # d
        return min(self.array)

    def arithmetic_mean(self):  # e
        return (sum(self.array)/len(self.array))

    def median(self):
        if len(self.array) %2==0:
            s = len(self.array)//2  # pierwsza środkowa wartość
            r = s - 1               # druga środkowa wartość
            return (self.array[s]+self.array[r])/2
        elif len(self.array) %2!=0:
            return self.array[(len(self.array)//2)]

    def wyniki(self):
        return f'Minimum: {self.smallest()},\nMaximum: {self.greatest()},\nArithmetic mean: {self.arithmetic_mean()},\nMediana: {self.median()}'

stat = Statistics([12, 37, 6, 9, 17])
print(stat.wyniki())