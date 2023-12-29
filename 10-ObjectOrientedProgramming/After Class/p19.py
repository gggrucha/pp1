'''
19.	The medical thermometer measures the patient's temperature in the range from 34.0 to 42.0 degrees Celsius, 
with an accuracy of 0.1 degrees. Write a program in which define a class that describes the states and behaviors of the thermometer. 
The thermometer should enable temperature measurement (do it by generating a random number from the 34.0 to 42.0 range) 
and display the measured value. If the temperature is at least 37 degrees Celsius, 
the thermometer should additionally display the 'Fever' message, e.g.
Temperature: 37.2C (fever)
When the temperature is at least 41.0, the thermometer should additionally display the message 'CRITICAL TEMPERATURE!!'. 
Place the class definition and the main program in separate files. Then use the program and:
a.	Create a thermometer
b.	Turn thermometer on
c.	Measure temperature
d.	Display temperature
e.	Turn thermometer off
'''
import thermometer
import random

pacjent = round(random.uniform(35,42),1)  # temperatura pacjenta
termo = thermometer.Thermometer()  # a
termo.turn_on()  # b
termo.measurement(pacjent)  # c d
termo.turn_off()  # e
