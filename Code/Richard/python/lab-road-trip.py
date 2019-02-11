
"""
author: Richard Sherman
2018-12-09
lab-road-trip.py, identifies connections between cities
"""
city_to_accessible_cities = {
  'Boston': ('New York', 'Albany', 'Portland'),
  'New York': ('Boston', 'Albany', 'Philadelphia'),
  'Albany': ('Boston', 'New York', 'Portland'),
  'Portland': ('Boston', 'Albany'),
  'Philadelphia': ('New York', )
}

origin = 'Philadelphia'
hop = []
hop.extend(city_to_accessible_cities[origin])
print(hop)
i = 1
#while i < 4:
while True:
  for city in hop:
      hop = (city_to_accessible_cities[city])
      print(len(hop))
  i += 1
hop_set = set([hop])
print(hop_set)

# origin = 'Portland'
# hop = city_to_accessible_cities[origin]
# print(hop)
# for i in range(3):
#    for city in hop:
#        hop += city_to_accessible_cities[city]
# hop_set = set(hop)
# print(hop_set)