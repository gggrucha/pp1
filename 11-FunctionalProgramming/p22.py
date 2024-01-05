'''
22.	The array below contains employee data: 
[("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
 ("Jackson","Peter"),("Johnson","Rick"),
 ("Lewis","Terry"),("Clarke","Robin")]
Write a program that determines and displays a list of employees whose last names are given in capital letters followed by first names, 
separated by commas. Sample result:
SMITH, Lucy
JONES, Janet
…
…
'''
employees = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
 ("Jackson","Peter"),("Johnson","Rick"),
 ("Lewis","Terry"),("Clarke","Robin")]

new = list(map(lambda x:x[0].upper()+', '+x[1],employees))

for element in new:
    print(element,end='\n')