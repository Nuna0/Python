import random

player_one = {'жизни': 50 }
player_two = {'жизни': 50 }

player_one['имя'] = input("Имя первого игрока: ")
player_two['имя'] = input("Имя второго игрока: ")

while player_one['жизни'] > 0 and player_two['жизни'] > 0 :
    input('Бой!')
    player_one['удар'] = random.randint(0,20)
    player_two['удар'] = random.randint(0,20)

    print('Первый игрок нанес ' + str(player_one['удар']) + ' урона')
    print('Второй игрок нанес ' + str(player_two['удар']) + ' урона')

    player_two['жизни'] -= player_one['удар']
    player_one['жизни'] -= player_two['удар']

    print('У первого игрока осталось' + str(player_one['жизни']) + ' жизни')
    print('У второго игрока осталось' + str(player_two['жизни'])  + ' жизни')

if player_one['жизни'] <= 0 and player_two['жизни'] <=0:
    print('Оба игрока погибли. Ничья.')
elif player_one['жизни'] <= 0:
    print('Игрок ' + player_one['имя'] + ' погиб. Победа ' + player_two['имя'])
elif player_two['жизни'] <= 0:
    print('Игрок ' + player_two['имя'] +  ' погиб. Победа ' + player_one['имя'])