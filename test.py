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
