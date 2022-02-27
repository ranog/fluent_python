from unicodedata import name


micro = 'µ'
print(name(micro))

micro_cf = micro.casefold()
print(name(micro_cf))
print(micro, micro_cf)

print()
print('######################################')
print()

eszett = 'ß'
print(name(eszett))

eszett_cf = eszett.casefold()
print(eszett, eszett_cf)
