from geolib import geohash as gh  # type: ignore

PRECISION = 9


def geohash(lat_lon: tuple[float, float]) -> str:
    return gh.encode(*lat_lon, PRECISION)
