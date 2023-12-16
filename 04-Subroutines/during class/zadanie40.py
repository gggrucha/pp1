def f(number):
    repeat_arr = []
    suma = 0
    for i in str(number):
        if int(i) in repeat_arr:           
            suma+=int(i)
        repeat_arr.append(int(i))
    print(repeat_arr)
    return suma

print(f(199),f(10))