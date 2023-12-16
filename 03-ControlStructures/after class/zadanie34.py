'''
34.	There are coins of 1, 2 and 5 Polish Zlotys (PLN). 
Write a program showing any amount (natural number) read from the keyboard with as few coins as possible.
Enter the amount in PLN: 18
The amount of PLN 18 in coins:
5 zł – 3 
2 zł – 1 
1 zł – 1
'''
coins = 18

jeden = 0
dwa = 0
piec = 0


if coins >= 5:
    piec = coins//5
    coins = coins-piec*5
    print('piatki: ', piec)
    print('Stan monet: ',coins)
if coins>=2:
    dwa = coins//2
    coins = coins - dwa *2
    print('coins: ', dwa)
if coins>=1:
    jeden = coins  
    print('jedynki: ', jeden)
print(f'5tki: {piec}, 2jki: {dwa}, 1nki: {jeden}')