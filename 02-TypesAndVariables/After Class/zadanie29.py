import random
suma = 0
i = 0
while i < 3:
    oczka = random.randrange(1,7)
    suma += oczka
    print(f'Rzut nr.{i}, wyrzucone oczka: {oczka}, suma: {suma}')
    i+=1
print('Suma: ', suma)