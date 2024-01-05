'''
21.	An array contains numbers from 1 to 20. Write a program that displays only numbers divisible by 2 and 3 without remainder. 
Use the filter() and an anonymous function.
'''
array = [i for i in range(1,21)]
def podz_2_i_3(liczba):
    if liczba %2==0 and liczba %3==0:
        return liczba
print(list(filter(lambda x: podz_2_i_3(x),array)))