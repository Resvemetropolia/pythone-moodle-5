city_list = []
for i in range(5):
    city_name = input(f"Enter the name of city {i + 1}: ")
    city_list.append(city_name)
print("City names:")
for city in city_list:
    print(city)