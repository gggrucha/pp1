'''
33.	The password is valid if it is at least 8 characters long. 
Write a program that checks whether the password read from the keyboard is correct. 
Sample result:
Enter password: qwertyXX
Password is valid: True
'''
password = input('Enter password: ')
if len(password) >= 8:
    valid = True
else:
    valid = False
print('Password is valid:',valid)