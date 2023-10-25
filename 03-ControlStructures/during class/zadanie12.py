per1_nam = input('Enter first person name: ')
per1_age = int(input('Enter first person age: '))

per2_nam = 'Anna'
per2_age = 18

if per1_age >= 18 and per2_age:
    print('Both adults')
elif per1_age>= 18 and per2_age<18:
    print('only adult is',per1_nam)
elif per1_age<18 and per2_age>=18:
    print('only',per2_nam)
else:
    print('none adult')
