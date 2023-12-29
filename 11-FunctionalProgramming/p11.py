'''
11.	Write a program that calculates the average speed of a vehicle. 
Enter from the keyboard: a distance in km, a number of travel hours and a number of travel minutes. 
Use an anonymous function. Sample result:
Enter distance in km: 70
Enter number of travel hours: 1
Enter number of travel minutes: 23
Average speed: 50.6 km/h
'''
avg_speed = lambda distance,hours,minutes: (distance/(hours+minutes/60))
distance = 70
hours = 1
minutes = 23

print(avg_speed(distance,hours,minutes))