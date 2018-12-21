city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

# def hop(origin):
#     dest = city_to_accessible_cities[origin]
#     print(dest)
#     return(dest)
#
# hop('Portland')

origin = 'Portland'
dest = city_to_accessible_cities[origin]
print(dest)
final_dest = {}
for city in dest:
    final_dest[city] = city_to_accessible_cities[city]
    dest = final_dest.values()
print(dest)



# hop = []
# city = 'Portland'
# for i in range(4):
#     for city in city_to_accessible_cities[city]:
#         hop.append(city_to_accessible_cities[city])
# print(hop)
