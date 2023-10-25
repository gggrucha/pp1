'''
25.	People up to and including 26 years of age are exempt from paying taxes in Poland. 
Write a program that, based on the person's age entered from the keyboard, 
displays True if the person is exempt from paying taxes and displays False otherwise. 
Sample result:
Enter age: 23
Exemption from paying taxes: True
'''
age = int(input('Enter age: '))
if age <= 26:
    exemption = True
else:
    exemption = False
print(f'Exemption from paying taxes: {exemption}')