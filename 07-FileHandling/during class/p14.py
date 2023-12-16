'''
14.	Create a program that allows you to add a name of next product you want to buy at the end of the text file shopping.txt. 
Enter the product name from the keyboard. Tip: open the file in appending mode.
'''

file = open(r"D:\test\shopping.txt",'a',encoding='utf-8')
product = input('Podaj produkt który chcesz dodać do listy zakupowej: ')
file.writelines(product+'\n')
