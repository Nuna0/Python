"""Параметры sep, end для команды print """

print('Текст1', 'Текст2', 'Текст3')  # стандартный вывод
print('Текст1', 'Текст2', 'Текст3', sep=' ----- ')  # sep переназначает разделитель
print('Текст1', 'Текст2', 'Текст3', sep='\n')  # \n - перевод на новую строку

print()  # вывод пустой строки
print('Блок1', end='___')  # end переназначает последний символ, по умолч. \n
print('Блок2', end='---')
print('Блок3', end='+++')