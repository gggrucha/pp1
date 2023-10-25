'''
38.	To improve readability, telephone numbers are often presented with a dash or 
space separating some digits. 
Write a program that displays a 9-digit telephone number entered from the keyboard as 
three groups of 3 digits each, separated by a dash character. Sample result:
Enter phone number: 543097329
Phone number: 543-097-329
'''
phone = str(input('Enter phone number: '))
new_phone = phone[:3] + '-' + phone[3:6] + '-' + phone[6:]
print('Phone number: ', new_phone)