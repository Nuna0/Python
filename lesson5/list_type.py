# Списки - упорядоченный изменяемый тип данных

# Создание списка
# cities = []
cities = ['Махачкала', 'Ростов-на-Дону', 'Бостон']
print(cities)

# Добавление записи
cities.append('Краснодар') # Добавление элемента в конец
print(cities)
cities.insert(2, 'Питер') # Добавление элемента по индексу
print(cities)

# Получение записи
print(cities[1]) # Получение значения по индексу
print(cities[:2]) # Срез списка
print(cities.pop()) # Получение последнего элемента с удалением
print(cities)
print(cities.pop(2)) # Получение элемента по индексу с удалением
print(cities)

# Изменение значения записи
cities[2] = 'Детройт' # Изменение значения элемента
print(cities)

# Удаление записи
del cities[1] # Удаление элемента по индексу
print(cities)
cities.remove('Детройт') # Удаление элемента по значению
print(cities)


# Объединение двух списков
new_cities = ['Москва', 'Екатеринбург']
# cities.extend(new_cities) # Добавление списка в другой список, 1 способ
cities += new_cities # Добавление списка в другой список, 2 способ
print(cities)