'''
30.	In a beverage factory, a machine fills 500ml bottles. 
The computer checks whether the bottle has been filled correctly. 
For a 500ml bottle, the allowable tolerance is 2%. In the last ten bottles checked, the filling was:
508,500,512,499,492,511,503,476,501,509
Write a program that calculates the percentage of incorrectly filled bottles. 
Use the filter() along with a higher order function. Sample result:
Bottle capacity:    500ml
Filling tolerance:  2%
Filled bottles:     508,500,512,499,492,511,503,476,501,509
Incorrectly filled: 30%
'''
bottles = [508,500,512,499,492,511,503,476,501,509]
bottle_cap = 500 # capacity
tolerance = 2

def incorect_counter(lista,tolerance,capacity):
    a = list(filter(lambda x:(x/capacity-1)*100>tolerance or (x/capacity-1)*100<-tolerance,lista))
    return len(a)

# wyświetlanie
max_znakow = 20


incorectly_filled = int(incorect_counter(bottles,tolerance,capacity=bottle_cap) / len(bottles) * 100)
str_bottles = [str(i) for i in bottles]

print(f"Bottle capacity:    {bottle_cap}ml")
print(f"Filling tolerance:  {tolerance}%")
print(f"Filled bottles:     {','.join(str_bottles)}")
print(f"Incorrectly filled: {incorectly_filled}%")
