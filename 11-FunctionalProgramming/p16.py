'''
16.	The data below contains a list of products available in stock and their unit price.
stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
Write a program that calculates the total value of products in stock. Use the map(), sum() and an anonymous function. Sample result:
Products in stock: [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
Total value: 423.35
'''
stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]


result = sum(list(map(lambda x: x[0]*x[1],stock)))
print(result)