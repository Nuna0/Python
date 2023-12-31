import random
import time


def create_player():  # функция создания игрока
    player = {'жизни': 50}  # создаем словарь с данными об игроке
    player['имя'] = input('Имя игрока: ')  # определяем имя игрока
    return player  # возвращаем словарь с данными

def attack(damager, defender):  # нанесение урона одним игроком второму
    damager['урон'] = random.randint(1, 20)  # случайное значение урона у игрока
    defender['жизни'] -= damager['урон']  # наносим сопернику урон
    print(damager['имя'] + ' нанёс ' + str(damager['урон']) + ' урона.')  # информация об нанесенном уроне

def player_info(player):  # информация об оставшихся жизнях игрока
    print('У ' + player['имя'] + ' осталось ' + str(player['жизни']) + ' здоровья')  # информация об остатках жизней
    
def win_check(player1, player2):  # проверяем, кто из игроков выжил и победил
    if player1['жизни'] <= 0 and player2['жизни'] <= 0:  # проверка на ничью
        return 'Оба игрока погибли. Ничья.'
    elif player1['жизни'] <= 0:  # проверка на поражение игрока 1
        return player1['имя'] + ' погиб. ' + player2['имя'] + ' победил!'
    elif player2['жизни'] <= 0:  # проверка на поражение игрока 2
        return player2['имя'] + ' погиб. ' + player1['имя'] + ' победил!'


player1 = create_player()  # создаем первого игрока
player2 = create_player()  # создаем второго игрока

while player1['жизни'] > 0 and player2['жизни'] > 0:  # проверка, живы ли бойцы
    time.sleep(3)  # останавливаем выполнение на 3 секунды
    print('----------------Новый раунд----------------')

    attack(player1, player2)  # первый игрок атакует второго
    attack(player2, player1)  # второй игрок атакует первого

    player_info(player1)  # информация о первом игроке
    player_info(player2)  # информация о втором игроке

print(win_check(player1, player2))  # вывод результата