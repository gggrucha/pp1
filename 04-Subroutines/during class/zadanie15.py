'''
15.	Define a function phone_keyboard() that displays numbers in the layout as below 
(like on a phone keypad). Apply a loop statement. Then, call the function. Sample result:
1 2 3
4 5 6
7 8 9
'''
def phone_keyboard():
    for i in range(2,9,3):
        print(i-1,i,i+1)
phone_keyboard()