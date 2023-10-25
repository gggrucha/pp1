'''
42.	Write a program that allows you to enter a binary, four-digit number. 
Convert the entered number from binary to decimal value. 
Do not use available Python functions. Sample result:
Enter binary number: 0110
Binary number in decimal notation: 6
'''
bin_num = str(input('Enter binary number: '))
if len(bin_num) > 4 or len(bin_num) < 1:
    print('Wrong value. Must be at least 1 digits and smaller or even 4 digits')
else:
    wynik=0
    potega = len(bin_num) - 1
    for char in bin_num:
        wynik+=int(char)*2**potega
        potega-=1
    print('Binary number in decimal notation:', wynik)
