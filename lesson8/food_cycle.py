food_list = []
food_count = 0

while True:
    food = input('Введите продукт к покупке: ')

    if food == 'Достаточно':
        break # прерывает весь цикл

    food_count += 1
    if food == 'Пропустить':
        continue #прерывает иттерации
    food_list.append('Покупка №' + str(food_count) + ': ' + food)
print(food_list)