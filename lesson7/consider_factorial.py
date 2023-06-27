import math
import random

random_num = random.randint(0,10)
result = int(input("Факториал числа " + str(random_num) + " равен"))
if result == math.factorial(random_num):
    print("Верно, молодец")
else:
    print("Садись,два")