def solve_eq(a=1, b=0, c=0):  # значения a, b, c заданы по умолчанию
    discr = b ** 2 - 4 * a * c
    print('РЕШЕНИЕ')
    if discr < 0:
        print('У уравнения нет корней.')
        return  # по умолчанию вернет None
    elif discr == 0:
        x = -b / (2 * a)
        print(f'x = {x:.3f}')
        return x
    else:
        x1 = (-b + discr ** 0.5) / (2 * a)
        x2 = (-b - discr ** 0.5) / (2 * a)
        print(f'x1 = {x1}\nx2 = {x2}')  # \n перевожу второй корень на новую строку
        return x1, x2  # вернется кортеж из корней

solve_eq()

solve_eq(2, -1, 0)  # позиционные аргументы
solve_eq(c=0, b=-1, a=1)  # именованные аргументы
solve_eq(1, c=0, b=-1)  # позиционные и именованные аргументы