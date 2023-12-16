# 15.	The program contains two dictionaries with personal data:

basic_data = {
    "name":"Barbara",
    "age":21
}

advanced_data = {
    "status":"student",
    "married":False,
    "interest":["reading","swimming"]
}
'''Write a program that creates a dictionary called 'person' containing data from the two given dictionaries (five key-value pairs). 
Display the contents of the 'person' dictionary.'''
person = {}
person.update(basic_data)
person.update(advanced_data)
print(person)