num =int(input('Введите число '))

if num > 0 and num != 10:
    print("Это число больше 0, но не 10")
elif num == 0:
    print("Число равно 0")    
else:
    print("Число отрицательное, либо это 10")