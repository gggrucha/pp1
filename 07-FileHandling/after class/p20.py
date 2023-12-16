'''
20. (...). Then write a program that creates a shoppinglist.txt file, 
in which save the contents of the MeatAndFish.txt and the GrainsAndBread.txt files.
'''
file1 = open(r"D:\test\MeatAndFish.txt",'r')
file2 = open(r"D:\test\GrainsAndBread.txt",'r')

file3 = open(r"D:\test\shoppinglist.txt",'a')  # jeśli plik nie istnieje to go stworzy
file3.writelines(file1)
file3.writelines(file2)