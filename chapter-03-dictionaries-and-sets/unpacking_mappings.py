def dump(**kwargs):
    return kwargs


dumps = dump(**{'x': 1}, y=2, **{'z': 3})
print(dumps)

print({'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}})
