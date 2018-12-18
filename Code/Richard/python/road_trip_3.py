city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}


hop_dict = {}
origin = 'Philadelphia'
n_hops = 3
for i in range(n_hops + 1):
    for city in city_to_accessible_cities[origin]:
        hop_dict[i] = (origin, city)
        origin = city
print(hop_dict)