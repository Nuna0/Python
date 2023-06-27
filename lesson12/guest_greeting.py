def greet(special, *args, **kwargs):
    for guest in args:
        print(f'Добро пожаловать {guest}!')
    print(f'{special}, для вас отдельный вход.')
    print(f'{kwargs["special2"]}, для вас отдельный вход.')

greet('Магомед','Али', special2='Тамара')

# kwargs - для имеенованных аргументов