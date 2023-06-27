print('Укажите цвет и размер толстовки')
shirt_color =input('Цвет толстовки: ')
shirt_size = input('Размер толстовки:')

if ((shirt_color.lower() == 'черный' or shirt_color.lower() == 'белый') and not shirt_size == '50'):
    print("Ваш заказ принят")
# else:
#     print("Толстовки с такими параметрами нет в наличии")
