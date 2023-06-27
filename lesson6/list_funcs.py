cities = ["Москва","Москва","Лондон","Токио","Нью-Йорк"]
print(len(cities))
print(cities.index("Лондон"))
print(cities.count("Москва"))

numbs = [15,5,10,3.5]
print(min(numbs))
print(max(numbs))

print(cities + numbs)
cities_text = ' <3 '.join(cities ) #только строки
print(cities_text)

print(cities_text.split(' <3 '))

# print(cities[::-1])
cities.reverse() #изменяет список 
print(cities)

# cities.sort()

print(sorted(cities))
print(cities)

cities.sort(reverse=True)
#cities.sort(key=lambda x: len(x))
print(cities)


# cities_copy = cities
# cities_copy[0]= "Гонконг"
# print(cities)
# print(cities_copy)

#citi_copy = cities[:]
citi_copy = cities.copy()
citi_copy[0]= "Гонконг"
print(cities)
print(citi_copy)

print("Кельн" in cities)
print("Москва" in cities)
print("Москва" not in cities)

