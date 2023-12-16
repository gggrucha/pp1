'''
12.	Create a program that saves, in separate lines, your name and surname, 
university name and field of study in a text file.  
Tip: open a file in writing mode and use the write() method.
'''
moje_dane = ['Bartek','Nietwójinteres','UEK','Infstos']
# file = open(r"D:\test\p12.txt",'w')
# print(type(file))
# for thing in moje_dane:
#     file.write(thing)
#     print('\n')

with open(r"D:\test\p12.txt",'w') as fil:
    for thing in moje_dane:
        fil.write('{}\n'.format(thing))