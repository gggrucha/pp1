'''
43.	In computer science, every written (graphic) character of human language (letters, digits, symbols, 
etc.) is encoded by assigning it a number. 
This allows characters to be stored, transmitted, and transformed using digital computers. 
Write a program that displays a numerical representation of each letter of your name. 
To convert a character to its numerical representation, use the Python ord() function. 
Sample result:
Name: John
J(74) o(111) h(104) n(110)
'''
name = 'Bartek'
line=''
for char in name:
    line+=f'{char}({ord(char)}) '
print(line)