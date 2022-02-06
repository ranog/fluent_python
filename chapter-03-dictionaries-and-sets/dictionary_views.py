d = dict(a=10, b=20, c=30)
values = d.values()

print(values)
print(len(values))
print(list(values))
print(reversed(values))

# print(values[0]) - TypeError: 'dict_values' object is not subscriptable

d['z'] = 99

print(d)
print(values)

values_class = type({}.values())
# v = values_class() - TypeError: cannot create 'dict_values' instances
