'''
"Mr. John May, born on 1998-02-16"
Display the employee's name, surname, initials and date of birth on separate lines. Sample result:
Description: Mr. John May, born on 1998-02-16
Name: John
Surname: May
Initials: JM
Born: 1998-02-16
'''
desc = "Mr. John May, born on 1998-02-16"
print('Description:',desc)
name = desc[4:9]
print('Name: ', name)
surname = desc[9:12]
print('Surname: ', surname)
print(f'Initials: {str(name[0]+surname[0])}')
print('Born: ', desc[22:])
