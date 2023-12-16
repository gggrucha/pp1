'''
18.	Write a program that writes to a file ICAO.txt 
the contents of a dictionary containing ICAO spelling alphabet. Sample file content:
A Alfa
B Bravo
C Charlie
D Delta
…
…
Z Zulu

'''
dictionary = {'A':'Alfa',	
'B':'Bravo',	
'C':'Charlie',	
'D':'Delta',
'E':'Echo',	
'F':'Foxtrot',	
'G':'Golf',	
'H':'Hotel',	
'I':'India',	
'J':'Juliett',	
'K':'Kilo',	
'L':'Lima',
'M':'Mike',	
'N':'November',	
'O':'Oscar',	
'P':'Papa',	
'Q':'Quebec',	
'R':'Romeo',
'S':'Sierra',
'T':'Tango',
'U':'Uniform',
'V':'Victor',	
'W':'Whiskey',	
'X':'Xray',	
'Y':'Yankee',	
'Z':'Zulu'
}
file = open(r"D:\test\ICAO.txt",'w')
for item in dictionary.items():
    for element in item:
        file.write(str(element)+' ')
    file.write('\n')