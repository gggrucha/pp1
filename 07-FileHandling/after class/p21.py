'''
21.	Create a program that writes to a text file integer numbers in the range of <1,50>, every number in a separate line
'''

file = open(r"D:\test\rang1to50.txt",'w')
for i in range(1,51):
    file.write(str(i)+'\n')