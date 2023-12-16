'''
18.	Find any text file on the Internet and download it to your computer. 
Then write a program that copies the contents of this file to the copy.txt file. 
Copy the contents of the file as a whole. 
Finally, open both files in any text editor and check that their contents are the same.
'''

file = open(r"D:\test\filename.txt",'r')
file2 = open(r"D:\test\filenameCOPY.txt",'w')

file2.writelines(file)