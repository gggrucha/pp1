'''
23.	Write a program that calculates a dog's age in dog’s years. 
For the first two years, a dog's life is equal to 10.5 human years.
 After that, each dog year is equal to 4 human years. Sample result:
Enter the dog's age in human years: 15
The dog's age in dog’s years is 73 years.
'''
dog_age = 15 #in human years
if dog_age <= 2:
    dog_age = 10.5 
else:
    dog_age = (dog_age - 2)*4 + 10.5
print(dog_age)
