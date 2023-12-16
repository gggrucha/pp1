# def f(n):
#     counter = n
#     while counter>0:
#         print('*',end='')
#         counter-=1
#         if counter > 0:
#             print('/',end='')

def f(n):
    counter = n
    line = ''
    while counter>0:
        line+='*'
        counter-=1
        if counter > 0:
            line+='/'
    return line

print(f(4),'\n',f(5))