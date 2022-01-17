import numpy as np

print()
a = np.arange(12)
print(a)
print(type(a))
print(a.shape)

print()
a.shape = 3, 4
print(a)

print()
print(a[2])

print()
print(a[2, 1])

print()
print(a[:, 1])

print()
print(a.transpose())
