def f(number,even):
    sum = 0
    for char in str(number):
        if int(char)%2==0 and even == True:
            sum+=int(char)
        if int(char)%2!=0 and even == False:
            sum+=int(char)
    return sum

if __name__ == '__main__':
    print(f(3124,True))
    print(f(3124,False)) 
    print(f(20576,False)) 
    print(f(20576,True)) 
