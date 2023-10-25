'''
36.	A bank buys and sells Euro. 
Write a program that, based on the Euro buying and selling rates entered from the keyboard, 
calculates the difference between the buying and selling rates (spread). 
Display result with 4 decimal places. Sample result:
Bank buys EUR: 4.5940
Bank sells EUR: 4.6250
Spread: 0.0310
'''
buys = float(input('Bank buys EUR: '))
sells = float(input('Bank sells EUR: '))
spread = round(sells - buys, 4)
print(spread)