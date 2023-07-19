food = "Помидоры","Огурцы","Масло"
food = ("Помидоры","Огурцы","Масло")
print(food)
print(food[1])
# food[1] = "кабачки" ошибка нельзя изменять кортеж
food2 = "apples", "onion"#запятая 
print(food2)

veg1, veg2, veg3 = food # Распаковка картежа
print(veg1, veg2, veg3)

num1, num2 = 10, 15
print(num1, num2)