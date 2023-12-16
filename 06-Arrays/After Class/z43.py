'''
43.	A variable contains text:
An apple a day keeps the doctor away
Create a module MyText, containing:
a.	A function that returns the number of words in the text
b.	A function that returns an ordered array of words, from longest to shortest
c.	A function that returns an alphabetically ordered array of words
Then, write a program, call the functions and display results. Sample result:
Text: An apple a day keeps the doctor away
Number of words: 8
Words from the longest: doctor,apple,…
Words ordered alphabetically: a,An,apple,away,…
'''
text = 'An apple a day keeps the doctor away'

def num_of_words(t):
    num_of_space = 0
    for char in t:
        if char == ' ':
            num_of_space+=1
    return num_of_space+1 # zakładam że tekst ma conajmniej jeden znak

def ordered_by_lenght(t):
    arab = t.split()
    sorted_arr = sorted(arab, key=len, reverse=True)
    return sorted_arr

def alfabetycznie(t):
    arab = t.split()
    arab.sort(key= lambda x: x.lower()) 
    return arab

print(f'Text: {text}')
print(f'Number of words: {num_of_words(text)}')
print(f'Words from the longest: {ordered_by_lenght(text)}')
print(f'Words ordered alphabetically: {alfabetycznie(text)}')
