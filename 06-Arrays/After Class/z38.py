'''
38.	Write a program that, for the given array of real numbers, 
displays the number of elements that are greater than the given value entered from the keyboard.
'''
arr = [123,3,3123,334,5,]
print('Array: ', arr)
value = int(input('Enter value: '))
number = 0  # number of elements greater coś tam coś tam
for element in arr:
    if element>value:
        number+=1
print('number of elements in array that are greater than the given value: ', number)
