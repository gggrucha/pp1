'''
A valid number on the planet Metis consists of digits 1 to 7 and lowercase or uppercase letters a to d.
A plus (+) or minus (-) sign may also appear at the beginning of the number. The mnumbers array contains sample numbers. 
Create a function f(mnumbers) that returns how many numbers in the array that are valid in the planet Metis. Example:
f(["A15","-31","7abC","+D1","-gH"])  4
f(["A05","-3+1","7ab8C","+D1","-22k"])  1
'''
def f(mnumbers):
    dobre_znaki = set("1234567abcdABCD")
    counter = 0
    for s in mnumbers:

        if s[0] in ('+', '-'):
            s = s[1:]

        if all(char in dobre_znaki for char in s):
            counter += 1
        
    return counter


print(f(["A15","-31","7abC","+D1","-gH"]))
print(f(["A05","-3+1","7ab8C","+D1","-22k"]))