'''
30.	Write a program that allows you to convert time in 24-hour format to 12-hour format. 
The time in 24-hour format (hh:mm) is read from the keyboard. 
Sample result:
Enter time (24-hour format): 16:32
Time in 12-hour format: 4:32pm
'''
time = '23:01'  # w formacie 24h
if int(time[:2]) > 12:
    hours = int(time[:2])-12
    time = str(hours) + time[2:]
    print(hours)
    time+='PM'
else:
    time+='AM'
print(time)