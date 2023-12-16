'''
13.	An array film_titles contains any five film titles. 
Write a program that writes the film titles to a text file, each title on a separate line. 
After running the program, open the created text file and check its content
'''
film_titles = ['a','b','c','d','e']

file = open(r"D:\test\filmt.txt",'w',encoding='utf-8')

for i,tytul in enumerate(film_titles):
    file.write(f'{tytul}')
    if i < len(film_titles) - 1:
        file.write('\n')    
    