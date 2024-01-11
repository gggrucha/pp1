'''
Create a function f(arr2D) that returns true when the sum of the values in at least two columns is the same. 
Otherwise, the function returns false. Example:
arr = [[3,4,2],[2,2,2,0],[5,0,0,5],[4,7,0,2],[0,2,0,0]]
f([[3,4,2],[5,1,6]])  True
f([[3,4,2],[5,1,7]])  False
f([[3,4],[5,1],[4,7]])  True
f([[3,4],[5,9],[4,7]])  False
'''
def f(arr2D):
 
    # szukanie największego elementu w arr2D
    maxi = len(max(arr2D,key=len)) # największy element
    for lista in arr2D:
        while len(lista)<maxi: # wykona się jeśli jakaś lista ma mniej elementow niz najwieksza z pozostalych
            lista.append(0)
    
    # szukanie dwóch takich samych sum
    sumy = []
    for i in range (len(arr2D[0])):
        sumka = 0
        for j in range(len(arr2D)):
            sumka += arr2D[j][i]  # suma jednej wewnętrznej listy
        if sumka in sumy:
            return True
        sumy.append(sumka)
    return False

print(f([[3,4,2],[2,2,2,0],[5,0,0,5],[4,7,0,2],[0,2,0,0]]))
print(f([[3,4,2],[5,1,6]]))
print(f([[3,4,2],[5,1,7]]) )
print(f([[3,4],[5,1],[4,7]]))
print(f([[3,4],[5,9],[4,7]]))
