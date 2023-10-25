'''
24.	A computer program analyses the price of a product in an online store. 
If the product price decreases by at least 10%, the program displays a purchase recommendation
Buy the product!!
Product price reduced by 17%
'''
price = 1000
new_price = 700
price_red = 1-700/1000
if price_red >= 0.10:
    print('Buy the product!!\nProduct price reduced by ',round(price_red*100,2),'%')