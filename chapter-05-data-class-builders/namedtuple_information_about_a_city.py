import json
from collections import namedtuple

City = namedtuple(typename='City', field_names='name country population coordinates')
tokyo = City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))

print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
print(City._fields)

Coordinate = namedtuple(typename='Coordinate', field_names='lat lon')
delhi_data = ('Dalhi NCR', 'IN', 21.935, Coordinate(lat=28.613889, lon=77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())
print(json.dumps(delhi._asdict()))

Coordinate = namedtuple(typename='Coordinate', field_names='lat lon reference', defaults=['WGS84'])
print(Coordinate(lat=0, lon=0))
print(Coordinate._field_defaults)
