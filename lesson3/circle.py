import math

radius = int(input("Radius:"))
c_length = round(2 * math.pi * radius, 3)
c_square = round(math.pi * radius ** 2 / 2, 2)
print("Длина окружности:", c_length)
print("Площадь окружности:",c_square)