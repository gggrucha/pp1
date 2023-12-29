'''
22.	The Contact class contains the 'name', 'email' and 'telephone' fields enabling the description of a single contact on a smartphone. 
The Contact_List class allows you to store contacts (store objects describing contacts in an array) and perform the following operations:
a.	Adds a new contact
b.	Displays the contact list
Write a program consisting of 3 files (smartphone.py, contact.py, contact_list.py). 
In the mail program (smartphone.py) create an object representing a contact list and add the following people data:
John Brown     brown@onet.pl       555234000
Anna May   	am@o2.pl            232000199
George Small   smallg@google.pl    222999100
Paola Big      bigpaola@poczta.pl  100200300
Then, display the contact list available on the smartphone.
'''
class Contact():
    def __init__(self,name,email,telephone) -> None:
        self.name = name
        self.email = email
        self.telephone = telephone

class Contact_List():
    def __init__(self):
        self.array = []
        
    def add(self,value):
        self.array.append(value)

    def __str__(self):
        return ''.join(self.array)

        


lista_kontaktow = Contact_List()
kontakt1 = Contact('bartek','g','696969')
lista_kontaktow.add(kontakt1)
print(lista_kontaktow)