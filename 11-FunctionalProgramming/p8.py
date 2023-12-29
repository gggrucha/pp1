'''
8.	Write a program that converts speed in meters per second to speed in kilometers per hour. 
Define a function ms_to_kmh(ms) that returns the calculated speed in km/h. Sample result:
10 m/s = 36 km/h
35 m/s = 126 km/h
'''
def ms_to_komh(ms):
    return ms*3.6

ms = 35
print(ms,'m/s =',int(ms_to_komh(ms)),'km/h')