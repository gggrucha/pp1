pin = "1234"

proba = 0
attempt = 1
while proba!=pin and attempt <= 3:
    proba = input('Enter the PIN code:')
    if proba == pin:
        print('Attempt ok')
        break
    attempt += 1
    print('Incorrect')
    if attempt >3:
        print('Sorry, your payment card has been blocked')
