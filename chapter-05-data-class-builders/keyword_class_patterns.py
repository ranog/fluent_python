import typing


class City(typing.NamedTuple):
    continent: str
    name: str
    country: str


cities = [
    City(continent='Asia', name='Tokyo', country='JP'),
    City(continent='Asia', name='Delhi', country='IN'),
    City(continent='North America', name='Mexico City', country='MX'),
    City(continent='North America', name='New York', country='US'),
    City(continent='South America', name='São Paulo', country='BR'),
]


def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia'):
                results.append(city)
    return results


print(match_asian_cities())


def match_asian_countries():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia', country=country):
                results.append(country)
    return results


print(match_asian_countries())
