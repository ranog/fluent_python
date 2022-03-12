from coordinates import Coordinate

moscow = Coordinate(lat=55.76, lon=37.62)

print(moscow)

location = Coordinate(lat=55.76, lon=37.62)
print(location == moscow)
print((location.lat, location.lon) == (moscow.lat, moscow.lon))
