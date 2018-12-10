
"""
author: Richard Sherman
2018-12-09
lab-road-trip.py, identifies connections between cities
"""

# a function to flatten lists
def flatten(l):
  out = []
  for item in l:
    if isinstance(item, (list, tuple)):
      out.extend(flatten(item))
    else:
      out.append(item)
  return out

# original problem used sets; lists are easier

# city_to_accessible_cities = {
#   'Boston': {'New York', 'Albany', 'Portland'},
#   'New York': {'Boston', 'Albany', 'Philadelphia'},
#   'Albany': {'Boston', 'New York', 'Portland'},
#   'Portland': {'Boston', 'Albany'},
#   'Philadelphia': {'New York'}
# }

city_to_accessible_cities = {
  'Boston': ['New York', 'Albany', 'Portland'],
  'New York': ['Boston', 'Albany', 'Philadelphia'],
  'Albany': ['Boston', 'New York', 'Portland'],
  'Portland': ['Boston', 'Albany'],
  'Philadelphia': ['New York']
}

# make a list of the cities for use in subsetting
cities = ['Boston', 'New York', 'Albany', 'Portland', 'Philadelphia']


origin = input('Please enter a city. I\'ll tell you which cities you can reach from there in two hops.  ')

# where you can get in one hop
cities_one_hop = city_to_accessible_cities[origin]
cities.remove(origin)

cities_two_hop = []
for city in cities_one_hop:
    cities_two_hop.append(city_to_accessible_cities[city])
# print(cities_two_hop)

cities_two_hop = flatten(cities_two_hop)
cities_two_hop = set(cities_two_hop)
cities_two_hop.remove(origin)
print(cities_two_hop)