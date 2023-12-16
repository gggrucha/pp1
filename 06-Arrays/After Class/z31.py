'''
31.	Create a program that displays all unique elements in an array. Sample result:
Array: 2 3 2 5 8 1 9 8
Unique elements: 3 5 1 9
'''
# zasada działania: sprawdzamy czy sprawdzany element jest już w liście UNIQUE
  # jeśli tak, to kasujemy go z unique i dodajemy do listy skasowanych (to oznacza, że element się powtarza)
  # jeśli nie, to sprawdzamy czy nie jest już w skasowanych i dodajemy do unique 
array = [2, 3, 2, 5, 8, 1, 9, 8]
unique = []
skasowane = []
for i in array:
    if i in unique:
        unique.remove(i)
        skasowane.append(i)
    else:
        if i not in skasowane:
            unique.append(i)
print(unique)