'''
40.	The credit card number consists of 16 digits. 
Write a program that allows you to enter a credit card number from the keyboard. 
Display the credit card number in groups of 4 digits, separating the groups with a space character. 
Sample result:
Enter credit card number: 5020312109004442
Card number: 5020 3121 0900 4442
'''
numba = str(input('Enter credit card number: '))
niu_namba = numba[:4] + ' ' + numba[4:8] + ' ' + numba[8:12] + ' ' + numba[12:16]
print('Card number: ', niu_namba) 
