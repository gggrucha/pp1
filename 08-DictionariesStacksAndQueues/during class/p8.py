'''
8.	Create a dictionary as in the example below. 
Note the structure of the dictionary (key-value) and the value types in the example below. 
What type of value was used in each of the six key-value pairs?
'''
person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }
'''
Then, create a program and do the following tasks:
a.	Display contents of the dictionary
b.	Display name
c.	Display hobby
d.	Change surname to Nowak
e.	Change person's marriage status
f.	Add gender: male
g.	Add a new hobby: bicycle
h.	Add work phone to existing phones: 313131444
'''
print(person.items())  # a
print(person['name'])  # b
print(person['hobby'])  # c
person['surname']='Nowak'
print(person['surname'])  # d
person['married']=False
print(person['married'])  # e
person['gender']='male' 
print(person['gender'])  # f
person['hobby'].append('bicycle')
print(person['hobby'])
person['phone'].update({'work':'313131444'})
print(person['phone'])