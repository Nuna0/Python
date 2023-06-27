# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

i = 1
while i <= 5:
    print(i)
    i +=1

# while True:
#     print(i)
#     i +=1      бесконечный цикл

real_user_name = "Senior"
user_try = input("Назовите ваше имя: ")

while user_try.lower != real_user_name:
    print("Вы назвали неправильное имя")
    user_try = input("Назовите ваше имя: ")
print(real_user_name + ', добро пожаловать')

