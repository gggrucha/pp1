'''
13.	Write a program where you create a dictionary containing student data. 
Try to describe a student in detail, using different data types that can be used in the dictionary. 
Then save the data about student in the file student.json, in a readable form
'''
import json
student_data = {'imie':'bartek','wiek':20,'ulubione przedmioty':['pp','wdm']}

file = open(r"D:\test\student_data.json",'w')
json.dump(student_data,file,indent=4)
