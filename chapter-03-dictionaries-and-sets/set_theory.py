foo = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
print(foo)
print(set(foo))
print(list(set(foo)))

print(dict.fromkeys(foo).keys())
print(list(dict.fromkeys(foo).keys()))
