'''32.	23% VAT was paid from an amount. 
Write a program that reads an amount from the keyboard. 
Then, it calculates and displays both the amount and its VAT. 
Apply formatting with two decimal places. Sample result:
Amount  : 15.84
VAT 23% :  3.64
'''
amount = 15.84
vat_amount = amount*0.23
print(round(vat_amount,2))