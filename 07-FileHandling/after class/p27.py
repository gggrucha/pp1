'''
27.	Write a program that computes the number of words in the following text. Use regular expressions.
To be, or not to be, that is the question
'''
import re 
text = "To be, or not to be, that is the question"
reg = re.findall("\w+",text)
print(reg)
print(len(reg))