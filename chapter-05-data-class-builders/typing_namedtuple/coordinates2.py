from typing import NamedTuple


class Coordinate(NamedTuple):
    lat: float
    lon: float
    reference: str = 'WGS84'
