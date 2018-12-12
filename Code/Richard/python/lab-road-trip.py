
"""
author: Richard Sherman
2018-12-09
lab-road-trip.py, identifies connections between cities
"""
city_to_accessible_cities = {
  'Boston': ['New York', 'Albany', 'Portland'],
  'New York': ['Boston', 'Albany', 'Philadelphia'],
  'Albany': ['Boston', 'New York', 'Portland'],
  'Portland': ['Boston', 'Albany'],
  'Philadelphia': ['New York'],
  'Kalamazoo': ['Philadelphia']
}


# a function to flatten lists
def flatten(l):
  out = []
  for item in l:
    if isinstance(item, (list, tuple)):
      out.extend(flatten(item))
    else:
      out.append(item)
  return out

# original problem used sets; lists are easier (?)
#
# city_to_accessible_cities = {
#   'Boston': {'New York', 'Albany', 'Portland'},
#   'New York': {'Boston', 'Albany', 'Philadelphia'},
#   'Albany': {'Boston', 'New York', 'Portland'},
#   'Portland': {'Boston', 'Albany'},
#   'Philadelphia': {'New York'}
# }



origin = input('Please enter a city. I\'ll tell you which cities you can reach from there in two hops.  ')

# where you can get in one hop
cities_one_hop = city_to_accessible_cities[origin]

cities_two_hop = []
for city in cities_one_hop:
    cities_two_hop.append(city_to_accessible_cities[city])
# print(cities_two_hop)

cities_two_hop = flatten(cities_two_hop)
cities_two_hop = set(cities_two_hop)
# if origin in cities_two_hop:     # this is optional, do we want to exclude a two-hop trip to the origin city or not?
#   cities_two_hop.remove(origin)
print(cities_two_hop)

def city_hop(origin, n_hops):
  hop = city_to_accessible_cities[origin]
  for n in n_hops:
    for city in hop:
      hop.append(city_to_accessible_cities[city])
  hop_set = set(hop)
  print(hop_set)
  return hop_set

print('\n')
origin = input('Please enter a city. Then I\'ll ask you how many hops you want to take from there:  ')
n_hops = input('How many hops do you want to take?  ')

city_hop(origin, n_hops)