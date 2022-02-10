d1 = dict(a=1, b=2, c=3, d=4)
d2 = dict(b=20, d=40, e=50)

print(d1.keys() & d2.keys())

s = {'a', 'e', 'i'}
print(d1.keys() & s)
print(d1.keys() | s)
