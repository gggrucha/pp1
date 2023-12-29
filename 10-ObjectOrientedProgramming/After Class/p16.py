'''
16.	Create a class that describes cell phones with at least 3 phone states and 2 behaviors. 
Define a text representation of an object. Then, create 2 objects. Display their features and call their bahaviors
'''
class Phone():
    def __init__(self,turned_on=False):
        self.turned_on = turned_on

    def wlacz(self):
        self.turned_on = True

    def wylacz(self):
        self.turned_on = False

    def __str__(self):
        return 'Telefon' + (' jest włączony' if self.turned_on else ' nie jest włączony')
    
tele = Phone()
tele.wlacz()
print(tele)