# Общее описание:
# Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными
# характеристиками. Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон
# друг другу, пока у одного из героев не закончится здоровье.
#
# Требования:
# Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# Игра должна быть реализована как консольное приложение.
#
# Классы:

# Класс Hero:
# Атрибуты:
# Имя (name)
# Здоровье (health), начальное значение 100
# Сила удара (attack_power), начальное значение 20
# Методы:
# attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
# is_alive(): возвращает True, если здоровье героя больше 0, иначе False

# Класс Game:
# Атрибуты:
# Игрок (player), экземпляр класса Hero
# Компьютер (computer), экземпляр класса Hero
# Методы:
# start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет.
# Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника)
# и объявляет победителя.


import random


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f'Герой {self.name} атакует героя {other.name}.')
        print(f'Здоровье героя {other.name}: {other.health}.\n')

    def is_alive(self):
        if self.health <= 0:
            print(f'Герой {self.name} мертв.')
            return False
        return True


class Game:
    def __init__(self, player: Hero, computer: Hero):
        self.player = player
        self.computer = computer

    def start(self):
        print('Игра началась!')
        choice = random.randint(0, 1)
        if choice == 0:
            print(f'Первым действует герой {self.computer.name}.\n')
        elif choice == 1:
            print(f'Первым действует герой {self.player.name}.\n')
        while self.player.is_alive() and self.computer.is_alive():
            if choice % 2 == 0:
                comp_choice = random.randint(1, 3)
                if comp_choice == 1:
                    self.computer.attack(self.player)
                elif comp_choice == 2:
                    self.computer.attack_power += 5
                    print(f'Герой {self.computer.name} увеличил силу удара.')
                    print(f'Сила удара героя {self.computer.name}: {self.computer.attack_power}.\n')
                elif comp_choice == 3:
                    self.computer.health += 15
                    print(f'Герой {self.computer.name} увеличил очки здоровья.')
                    print(f'Здоровье героя {self.computer.name}: {self.computer.health}.\n')
            if choice % 2 == 1:
                pl_choice = int(input('Введите номер действия: 1 - атака, 2 - сила удара, 3 - здоровье.\n'))
                if pl_choice == 1:
                    self.player.attack(self.computer)
                elif pl_choice == 2:
                    self.player.attack_power += 5
                    print(f'Герой {self.player.name} увеличил силу удара.')
                    print(f'Сила удара героя {self.player.name}: {self.player.attack_power}.\n')
                elif pl_choice == 3:
                    self.player.health += 15
                    print(f'Герой {self.player.name} увеличил очки здоровья.')
                    print(f'Здоровье героя {self.player.name}: {self.player.health}.\n')
            choice += 1
        print('Игра окончена.')
        if self.player.is_alive():
            print(f'Герой {self.player.name} победил!')
        elif self.computer.is_alive():
            print(f'Герой {self.computer.name} победил!')


player1 = Hero('player')
computer1 = Hero('computer')

game = Game(player1, computer1)
game.start()
