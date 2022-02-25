from unicodedata import normalize

s1 = 'café'
s2 = 'cafe\N{COMBINING ACUTE ACCENT}'

print(s1, s2)
print(len(s1), len(s2))
print(s1 == s2)

print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))
print(normalize('NFC', s1) == normalize('NFC', s2))
print(normalize('NFD', s1) == normalize('NFD', s2))
