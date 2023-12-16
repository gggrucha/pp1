'''
44.	A valid password should consist of at least six different characters. 
Define a function f(password) that returns True if the password is correct or False otherwise. 
Sample result:
f("ax15") returns False
f("book123") returns False
f("A2water3") returns True
f("qwerty") returns True
f("") returns False
'''
def f(password):
    list_of_char = []
    for char in password:
        if char in list_of_char:
            return False # jakiś znak występuje więcej niż jeden raz
        list_of_char.append(char)
    # koniec iteracji po pętli for (całe hasło przeanalizowane)
    if len(list_of_char)<6:
        return False # długość hasła jest mniejsza niż 6
    return True

print(
f("ax15"),
f("book123"),
f("A2water3"),
f("qwerty"),
f("")
)