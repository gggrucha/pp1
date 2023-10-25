'''
39.	The price of the product on the price tag is given before and after the discount is applied. 
Write a program that allows you to enter the product price and discount. 
Display the product price, discount, discounted product price, 
and the difference between the product price before and after the discount. 
Display all prices with two decimal places. Sample result:
Enter price: 24.72
Enter discount %: 15
Price with discount: 21.01
Reduction: 3.71
'''
price = float(input('Enter price: '))
discount = float(input('Enter discount %: '))
price_w_discount = price * ((100-discount)/100)
reduction = price - price_w_discount
print(f'Price with discount: {round(price_w_discount,2)}\nReduction: {round(reduction,2)}')