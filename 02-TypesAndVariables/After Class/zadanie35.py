'''
35.	A tree may be cut down if its diameter is at least 50 cm. 
Write a program that, based on the circumference of the tree entered from the keyboard, 
calculates and displays the value True if the tree can be cut down, or display the value False otherwise. 
Sample result:
Enter tree circumference: …
Tree can be cut down: …
'''
diameter= 2*float(input('Enter tree circumference: '))
if diameter>=50:
    cut_down = True
else:
    cut_down = False
print(f'Tree can be cut down: {cut_down}')