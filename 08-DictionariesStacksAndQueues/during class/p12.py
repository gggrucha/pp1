'''
12.	Create a dictionary that describes your favourite book or film with at least five key-value pairs. 
Then create a program that writes the dictionary data to the favourite.json file. Use the dump() method. 
Note the formatting of the data in the json file. Use the 'indent' parameter in the dump() method.
'''
import json
dictionary = {'tytul':'x','rezyser':'y'}
file = open(r'D:\test\favfilm.json','w')
json.dump(dictionary,file,indent=2)
