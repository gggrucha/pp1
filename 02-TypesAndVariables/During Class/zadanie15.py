# użytkownik wprowadza wartość w stopniach celcjusza
celc = float(input('Proszę podać wartość w stopniach celcjusza'))

#program konwertuje temperature do innych jednostek
kelvin = celc + 273.15
fahrenheit = 1.8 * celc + 32

#wyświetlenie wartości
print(f'Wartość {celc}°C wynosi:\t{kelvin}K lub {fahrenheit}F')