'''
18.	Define a function numbers(n) that returns a string containing integer numbers from 1 to n, 
separated by a single space character. 
Then, call the function and display numbers from 1 to 15 and from 1 to 7. 
Sample result:
Numbers <1,15>: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Numbers <1,7>: 1 2 3 4 5 6 7
'''
def numbers(n):
    line = ''
    for i in range(1,n+1):
        line += str(i) + ' '
    return f'Numbers <1,{n}>: {line}'
print(numbers(10))