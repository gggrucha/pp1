'''
9.	Create a dictionary describing a mobile phone. Use at least 6 key-value pairs of data. Use different value types. 
Then, using 'for' loop, display the contents of the dictionary. 
To read a key and value, use the items() method.
'''
phon = {'make':'realme','model':'GT master edition','screensize':r'6,43"'}

for i in phon.items():
    print(i)