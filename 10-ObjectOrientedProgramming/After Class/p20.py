'''
20.	The bank account has a 26-digit number assigned when creating an account. 
The initial account balance is PLN 0. You can deposit any amount on the account. 
You can also withdraw any amount from the account, provided that it does not exceed the account balance. 
If you try to withdraw a larger amount, the following message will be displayed: "Insufficient funds on the account". 
At any time, it is possible to display information about the number and balance of the bank account in the following format:
Bank Account No: 11 1111 1111 1111 1111 1111 1111
Balance: PLN 25,38
Create a program that handles the bank account.
a.	Familiarises yourself with a problem.
b.	Identify an object
c.	Define the states and behaviors of the object.
d.	Transform the states and behaviors of the object into the fields and methods of the class that will serve as a pattern for creating an object.
e.	Create a sketch of the class without creating any method content.
f.	Create the content of each method.
Then, use the program and:
g.	Create a bank account with the number 12 3456 5555 9090 1111 0000 7722
h.	Display account balance
i.	Deposit PLN 25,30
j.	Display account balance
k.	Withdraw PLN 31,70
l.	Display account balance
m.	Withdraw PLN 14
n.	Display account balance
'''
class Bank():
    def __init__(self, number, balance=0):
        self.number = number
        self.balance = balance

    def depo(self,value):
        self.balance+=value

    def withdraw(self,value):
        if value<=self.balance:
            self.balance-=value
        elif value>self.balance:
            print("Insufficient funds on the account")

    def __str__(self):
        return f'Bank Account No: {self.number} \nBalance: PLN {self.balance}' 
    

numb = '12 3456 5555 9090 1111 0000 7722'
my_account = Bank(numb)
print(my_account)
my_account.depo(25.30)  # a
print(my_account)
my_account.withdraw(31.70)  # b 
print(my_account)
my_account.withdraw(14)
print(my_account)