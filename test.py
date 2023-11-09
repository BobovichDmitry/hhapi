import numpy as np

a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 3, 3, 3, 1]

b = []
for i in a:
    if not b or b[-1][0] != i:
        b.append([i, 1])   # a new element - append and start the count at 1
    else:
        b[-1][1] += 1  # a duplicate - increment the count

counts = ['{}*{}'.format(*l) for l in b]

print(counts)
print(b[0][1])


my_array = np.random.randint(-5, 5, (4, 4))
print(my_array)
print( my_array[:2])
my_array = np.array((57, 322, 57, 11, 77))

var = [34, 67, 8.9, 12, 56, 89, "привет", 5.8]
print(type(var))
print(np.linspace(5, 8, 100))