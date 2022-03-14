from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))

print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
