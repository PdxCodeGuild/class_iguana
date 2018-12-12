city_to_accessible_cities = {
  'Boston': ('New York', 'Albany', 'Portland'),
  'New York': ('Boston', 'Albany', 'Philadelphia'),
  'Albany': ('Boston', 'New York', 'Portland'),
  'Portland': ('Boston', 'Albany'),
  'Philadelphia': ('New York')
}

def city_hop(origin, n_hops):
    hop = city_to_accessible_cities[origin]
    print(hop)
    for i in range(n_hops):
        for city in hop:
            hop += city_to_accessible_cities[city]
    hop_set = set(hop)
    print(hop_set)

city_hop('Portland', 3)