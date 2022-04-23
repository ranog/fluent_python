from copy import deepcopy

a = [10, 20]
b = [a, 20]

a.append(b)
print(a)

c = deepcopy(a)
print(c)
