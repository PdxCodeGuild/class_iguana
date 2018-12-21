"""
author: Richard Sherman
2018-12-21
lab-road-trip.py, an exercise in sets and dictionaries,
finds the cities from an origin that are accessible by taking n 'hops'
"""
# this is the dictionary of sets of cities that can be reached from a given origin
# a pair are added to the original lab to facilitate testing
city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'},
  'Kalamazoo' : {'Philadelphia'},
  'End of the World' : {'End of the World'}
}

# the main trick here is the in-place version of the union of sets operator | , |= , analogous to +=
def road_trip(origin, n_hops):
    origin = {origin}
    for hops in range(n_hops):
        dest = set()
        for city in origin:
            dest |= city_to_accessible_cities[city]
        origin = dest
    print(dest)
    return dest

print('\nOne hop from Philadelphia:')
road_trip('Philadelphia', 1)

print('\nTwo hops from Philadelphia:')  # respect to W.C. Fields
road_trip('Philadelphia', 2)

print('\nThree hops from Philadelphia -- does not return to Philadelphia:')
road_trip('Philadelphia', 3)

print('\nTwo hops from Kalamazoo:')
road_trip('Kalamazoo', 2)

print('\nThree hops from Portland -- goes everywhere:')
road_trip('Portland', 3)

print('\nTwo hops from New York:')
road_trip('New York', 2)

print('\nThree hops from New York - goes everywhere:')
road_trip('New York', 3)

print('\nFive hops from the End of the World:')
road_trip('End of the World', 5)