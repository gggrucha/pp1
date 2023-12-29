class Ebook():
    def __init__(self, autor, tytul, ilosc_stron, is_oppened = False, strona=1):
        self.autor = autor
        self.tytul = tytul
        self.ilosc_stron = ilosc_stron
        self.is_oppened = is_oppened
        self.strona = strona

    def open_ebook(self):
        if self.is_oppened==False:
            self.is_oppened = True

    def close_ebook(self):
        if self.is_oppened == True:
            self.is_oppened = False

    def nastepna_str(self):
        if self.is_oppened == True and int(self.strona)<int(self.ilosc_stron):
            self.strona+=1
        elif self.is_oppened == False:
            print('Nie można zmieniać stron w zamkniętej książce')

    def poprzednia_str(self):
        if self.is_oppened == True and self.strona>1:
            self.strona+=1
        elif self.is_oppened == False:
            print('Nie można zmieniać stron w zamkniętej książce')

    def __str__(self):
        return f'Title: {self.tytul}, Author: {self.autor}, Page numbers: {self.ilosc_stron}, Current page no: {self.strona}, Czy otwarta?: {self.is_oppened}'