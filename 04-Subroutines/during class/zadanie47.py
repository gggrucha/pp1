'''
47.	Define a function f(text) that returns the given text with all characters separated by "-" (minus sign).
Example:
f("Univesity") returns "U-n-i-v-e-r-s-i-t-y"
f("UE") returns "U-E"
f("x") returns "x"
f("") returns ""
'''
# nie dizala chyba
# def f(text):
#     wynik = ''
#     for i in range(0,len(text)): # 0,1,2,3
#         if i!=len(text):
#             wynik+=text[i]+'-'
#     wynik = wynik[:2*len(text)-1]
#     if wynik[-1] =='-':
#         wynik = wynik[:-1]
#     return wynik


# drugi sposób
# def f(text):
#     result = ''
#     pauzy = len(text)-1
#     i = 0
#     while i<len(text):
#         result = result+text[i]
#         pauzy-=1
#         while pauzy>0:
#             result = result+'-'
#         i+=1
#     # result+=text[len(text)]
#     if result[-1] =='-':
#        result = result[:-1]

#     return result

#chat
def f(text):
    result = '-'.join(text)
    print(result)
    result = result[:-1]
    return result


print(f("Univesity\n"),
f("UE\n"),
f("x\n"),
f("")
)

# text = 'gah'
# print(text[-1])

# print(dir(str))