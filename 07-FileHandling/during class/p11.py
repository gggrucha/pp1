file = open(r"D:\test\numbers.txt",'r',encoding='utf-8')
suma = 0
for line in file:
    suma+=int(line)

print(suma)