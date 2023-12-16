'''
32.	Yes-no question are often used in surveys to gauge people's 
attitudes with regard to specific ideas or beliefs. 
Write a program that displays a survey consisting of three questions. 
Save the answers to logical type variables. 
Then view the survey result. 
Sample result:
Are you interested in computer science? (Y/N): Y 
Do you like playing computer games? (Y/N): N
Do you have an Instagram account? (Y/N): Y
Interested in computer science: Yes
Playing computer games: No
Has an Instagram account: Yes
'''
pyt1 = input('Are you interested in computer science? (Y/N): ')
pyt2 = input('Do you like playing computer games? (Y/N): ')
pyt3 = input('Do you have an Instagram account? (Y/N): ')
print(f'Interested in computer science: {pyt1}')
print(f'Playing computer games: {pyt2}')
print(f'Has an Instagram account: {pyt3}')