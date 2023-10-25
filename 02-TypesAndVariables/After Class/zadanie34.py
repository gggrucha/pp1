'''
34.	The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. 
Write a program that checks whether the vehicle speed entered from the keyboard is correct.
 Sample result:
Enter vehicle speed: 158
Speed is valid: False
'''
speed = float(input('enter speed: '))
if speed >= 40 and speed<=140:
    valid = True
else:
    valid = False
print(f'Speed is valid: {valid}')