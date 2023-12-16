'''
17.	Find any text file on the Internet that contains at least 30 lines of text and download that file to your computer. 
Then write a program that displays the first five lines from the file and then waits for the Enter key to be pressed. 
Then repeat displaying the next five lines from the file, waiting for the Enter key to be pressed each time.
'''

# kalkulacja ilości linijek (ogranicznik fora)
lines = 0
with open(r"D:\test\30lin.txt",'r') as file:
    for line in file:
        lines+=1
file.close()

file = open(r"D:\test\30lin.txt",'r')

for i,line in enumerate(file):
    if i%5==0:
        input()
    print(i+1,line)
