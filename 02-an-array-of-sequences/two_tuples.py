a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])

print(f'''- The content of the tuple itself is immutable, but that only means
the references held by the tuple will always point to the same objects:
    a = {a}
    b = {b}
''')

b[-1].append(99)
print(f'''However, if one of the referenced objects is mutable - like a list - its
content may change:
    b[-1].append(99)
    a = {a}
    b = {b}
''')
