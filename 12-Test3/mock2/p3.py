'''
Flight numbers along with the number of passengers are stored in a dictionary d. 
Define a function f(d) that returns the number of flights in which the number of passengers 
is greater than the average number of passengers on all flights. 
Example:
f({"LO231":150,"BA787":120,"NZ15":30})  2
f({"LO231":150,"BA787":20,"NZ15":30})  1
'''
def f(d):
    average=0
    for k,v in d.items():
        average+=v
    average=average/len(d)

    counter=0
    for k,v in d.items():
        if v>average:
            counter+=1

    return counter


print(f({"LO231":150,"BA787":120,"NZ15":30}))
print(f({"LO231":150,"BA787":20,"NZ15":30}))