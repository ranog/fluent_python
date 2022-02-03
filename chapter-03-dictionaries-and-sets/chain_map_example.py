from collections import ChainMap

d1 = dict(a=1, b=3)
d2 = dict(a=2, b=4, c=6)

chain = ChainMap(d1, d2)
print(chain['a'])
print(chain['c'])
chain['b'] = -1
print(d1)
print(d2)
