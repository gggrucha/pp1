'''
26.	An array contains a list of Polish names: Genowefa, Onufry, Celestyna, Alojzy, Pankracy. 
Create a program that displays the longest name (consisting of the largest number of characters). Sample result:
Names: Genowefa Onufry Celestyna Alojzy Pankracy
Longest name: Celestyna
'''
names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

def longest_name(names):
    long = names[0]  # zakładam, że pierwsze jest najdłuższe 
    for name in names:
        if len(name)>len(long):
            long = name
    return f'Longest name: {long}'

print(longest_name(names))