from operator import methodcaller

s = 'The time has come'

upcase = methodcaller('upper')
print(upcase(s))

hyphenate = methodcaller('replace', ' ', '-')
print(hyphenate(s))

print(str.upper(s))
