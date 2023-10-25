'''
28.	Correct body weight has a significant impact on health. 
Write a program that calculates the Body Mass Index (BMI) based on your height in cm and weight in kg.
 A user enters data from the keyboard. 
 Find the formula on the Internet for calculating the BMI. 
 Then, using your program, check that you have the correct weight. 
 Display the calculated BMI and display True if the weight is within the valid range, or display False otherwise. Sample result:
Enter your height in cm: ...
Enter your weight in kg: ...
Your BMI index: ...
Correct weight: True
'''
height = float(input('Enter your height in cm: '))
weight = float(input('Enter your weight in kg: '))
bmi = weight/(height/100)**2
print(bmi)
if bmi > 25:
    print('You are obese')
elif bmi < 20:
    print('You are too skinny')
else:
    print('You are healthy')
