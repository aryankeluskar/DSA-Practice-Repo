from collections import defaultdict

city_map = defaultdict(list)

# cn_cities = ["Vancouver", "Toronto", "Ottawa"]
# city_map["Canada"] = []
city_map["Canada"] += ["Vancouver", "Toronto", "Ottawa"]
city_map["India"] += ["Mumbai", "Delhi"]
city_map["America"] += ["DC", "NYC"]
city_map["Bhutan"] += ["Thimphu"]
city_map["Bangladesh"] += ["Dhaka"]

print(type(city_map.items()))
print(type(city_map.keys()))
print(list(city_map.values()))
