from typing import NamedTuple

from geolib import geohash as gh  # type: ignore

PRECISION = 9


class Coordinate(NamedTuple):
    lat: float
    lon: float


def geohash(lat_lon: Coordinate) -> str:
    return gh.encode(*lat_lon, PRECISION)
