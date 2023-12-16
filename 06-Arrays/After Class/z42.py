'''
42.	Define a function rand_elem(array) that returns a randomly selected array element. 
Using the function, display a few randomly selected array elements
'''
import random
def rand_elem(array):
    return random.choice(array)
arr = [2,35,5,1,24,5,5]
print(rand_elem(arr))
print(rand_elem(arr))
print(rand_elem(arr))
print(rand_elem(arr))