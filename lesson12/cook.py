import random

ACTIONS = ['пожарим','сварим','потушим','запечем']

def cook(*args, **kwargs):
    for product in args:
        print(f'{random.choice(ACTIONS)} {product}')
    print(f'Готовое блюдо заправим соусом {kwargs.get("sause", "аджикой")}')

cook('картошка','помидоры','лук','баклажаны', sause='майонезом')
cook('картошка','помидоры','лук','баклажаны')

def cook2(*args, sause='аджика'):
    for product in args:
        print(f'{random.choice(ACTIONS)} {product}')
    print(f'Готовое блюдо заправим соусом {sause}')

cook2('картошка','помидоры','лук','баклажаны', sause='майонезом')
cook2('картошка','помидоры','лук','баклажаны')