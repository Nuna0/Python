age = int(input("Введите ваш возраст: "))



if age > 120:
    print("Как вы дожили до стольки")
elif  120 >= age > 18:
    print("Проходите")
elif age == 18 or age == 17:
    print("Вам 17 либо 18")
elif age < 17 and age > 0:
        print("Вы несовершенолетний")
else:
    print("Ошибка")



