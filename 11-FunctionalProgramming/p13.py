'''
13.	In a beverage factory, a machine fills bottles of various capacities. 
A computer checks whether a bottle has been filled correctly. 
The allowable tolerance is 2% for a 500ml bottle, 3% for a 1000ml bottle and 5% for a 1500ml bottle. 
Write a program that checks whether the bottle has been filled correctly or not. 
Define a higher order function. Sample result:
507: True
489: False
984: True
1032: False
1578: False
1430: True 
'''

def tolerance(bottle):
    if bottle >= 0 and bottle <= 600:
        tolerance = ('500',(bottle/500-1)*100)  # x %
    elif bottle >= 601 and bottle <= 1250:
        tolerance = ('1000',(bottle/1000-1)*100)
    elif bottle >= 1251 and bottle <= 2000:
        tolerance = ('1500',(bottle/1500-1)*100)

    return tolerance

def checker(tolerance):  # bo
    if tolerance[0] == '500': 
        if tolerance[1] >= -2 and tolerance[1] <= 2: 
            return (tolerance,True)
    
    if tolerance[0] == '1000':
        if tolerance[1] >= -3 and tolerance[1] <= 3:
            return True
    
    if tolerance[0] =='1500':
        if tolerance[1] >= -5 and tolerance[1] <= 5:
            return True

    return False

print(checker(tolerance(507))) # True
print(checker(tolerance((489)))) # False
print(checker(tolerance((984)))) # True
print(checker(tolerance((1032)))) # False
print(checker(tolerance((1578)))) # False
print(checker(tolerance((1430)))) # True 

