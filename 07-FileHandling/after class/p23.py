'''
23.	Create a program that saves to a text file integer numbers in the range <1,10> with their second and third power. Sample result:
1,1,1
2,4,8
3,9,27
4,16,64
…
'''
file = open(r"D:\test\1to10power.txt",'a')

for number in range(1,11):
    file.write(f'{str(number)},{str(number**2)},{str(number**3)}\n')