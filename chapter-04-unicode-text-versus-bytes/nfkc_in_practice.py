from unicodedata import normalize, name

half = '\N{VULGAR FRACTION ONE HALF}'
print(half)
print(normalize('NFKC', half))
for char in normalize('NFKC', half):
    print(char, name(char), sep='\t')

print()
print('##########################################')
print()

four_squared = '4²'
print(four_squared)
print(normalize('NFKC', four_squared))
for char in normalize('NFKC', four_squared):
    print(char, name(char), sep='\t')

print()
print('##########################################')
print()

micro = 'µ'
micro_kc = normalize('NFKC', micro)
print(micro, micro_kc)
print(ord(micro), ord(micro_kc))
print(name(micro) + ' / ' + name(micro_kc))
