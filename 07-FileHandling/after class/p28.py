'''
28.	Find any text file on the Internet and download it to your computer. 
Then write a program that displays all words with at least six letters from the file. 
Display each word on a separate line. Use regular expressions
'''
# import re
# file = open(r"D:\test\shoppinglist.txt",'r')
# ## wyszukiwanie słów spełniających kryteria
# lista_slow = []
# for line in file:
#     reg = re.search(r'\b\w{6,\b}',line)
#     if reg:
#         lista_slow.append(line)
#         print('udalo si e')
#     print(reg)
#     # if len(reg)>0:   
#     #     lista_slow.extend(reg)        
# print('l_slow:',lista_slow)


# ## wyświetlanie tych słów

import re

def display_long_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Use regular expression to find words with at least six letters
    words = re.findall(r'\b\w{6,}\b', text)

    # Display each word on a separate line
    for word in words:
        print(word)

# Replace 'your_file.txt' with the actual path to your file
file_path = r"D:\test\shoppinglist.txt"
display_long_words(file_path)
