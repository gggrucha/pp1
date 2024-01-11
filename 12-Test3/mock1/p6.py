'''
Assume that a valid variable name in a computer program consists of one to five characters. 
The first character of a variable name must be a lowercase or uppercase letter or an underscore. 
The remaining characters in the variable name can be uppercase or lowercase letters, digits or the underscore character. 
Create a function f(vname) that returns true if the variable name vname is valid. Otherwise, the function returns false. 
Example:
f("abc")  True
f("Abc")  True
f("aBC")  True
f("_ab_c")  True
f("abcdef")  False
f("8abc")  False
f("_aB8_")  True
f("_4x")  True
'''
def f(vname):
    import string
    alfabet_low = list(string.ascii_lowercase)
    alfabet_high = list(string.ascii_uppercase)
    digits = [str(i) for i in range(0,10)]
    if len(vname)<1 or len(vname)>5:
        return False
    if vname[0] not in alfabet_low and vname[0] not in alfabet_high and vname[0] != '_':
        return False
    for char in range(1,len(vname)):
        if vname[char] not in alfabet_low and vname[char] not in alfabet_high and vname[char] not in digits and vname[char]!='_':
            return False
    return True

print(f("abc"),
f("Abc"),
f("aBC"),
f("_ab_c"),
f("abcdef"),
f("8abc"))
print(f("_aB8_"))
print(f("_4x"))