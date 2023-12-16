file = open(r"D:\test\countries.txt",'r', encoding='utf-8')
for line in file:
    print(line,end="")