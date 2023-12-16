a = 0
b = 1
n=1
line=''
while n<20:
    t = a
    a = b
    b = t + b
    line+=str(b)+' '
    n+=1
print('0 1', line)