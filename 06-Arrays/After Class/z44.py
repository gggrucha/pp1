'''
44.	Write a program that draws the graph of the function f(x)=x^2-3. Sample result:
import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(-100,101):
    x = x + [n]

# create y values
for n in x:
    y = …

# display chart
…
…
'''
import matplotlib.pyplot as plt
x = []
y = []

for n in range(-100,101):
    x = x + [n]

for n in x:
    y += [n**2-3]

print(x)
print(y)

plt.plot(x,y, 'o:r')
plt.show()