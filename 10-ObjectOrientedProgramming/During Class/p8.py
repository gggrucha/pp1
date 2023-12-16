'''
8.	Identify at least 3 states and 3 behaviors for a telephone object. Then, for the listed states and behaviors, 
create a class with fields (attributes) and methods. Try to use verbs in method names as they describe activities. 
Finally, create a object, call its methods and display object's properties.
'''
class Phone():
    def __init__(self, marka,model,rozmiar_ekranu):
        self.marka = marka
        self.model = model
        self.rozmiar_ekranu = rozmiar_ekranu
        self.wlaczony = True

    def wlacz(self):
        self.wlaczony = True

    def wylacz(self):
        self.wlaczony = False

    def __del__(self):
        return 'telefon utopiono w ubikacji'

    def __str__(self):
        return ':D' 

motorola = Phone('motorola','costam',6.43)
motorola.wylacz()
print(motorola.rozmiar_ekranu)
print(motorola.__del__())
