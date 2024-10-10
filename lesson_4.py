from random import randint, choice, sample
import time

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    def choose_defence(self, heroes_list):
        random_hero = choice(heroes_list)
        self.__defence = random_hero.ability

    def attack(self, heroes_list):
        alive_heroes = [hero for hero in heroes_list if hero.health > 0]
        targets = sample(alive_heroes, min(3, len(alive_heroes)))  # Выбор до 3 случайных героев
        for hero in targets:
            if type(hero) == Berserk and self.__defence != hero.ability:
                hero.blocked_damage = choice([5, 10])
                hero.health -= (self.damage - hero.blocked_damage)
            else:
                hero.health -= self.damage

    @property
    def defence(self):
        return self.__defence

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def apply_super_power(self, boss, heroes_list):
        pass

    def attack(self, boss):
        boss.health -= self.damage


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss, heroes_list):
        coeff = randint(2, 5)
        boss.health -= coeff * self.damage
        print(f'Warrior {self.name} hits critically {coeff * self.damage}.')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BOOST')

    def apply_super_power(self, boss, heroes_list):
        # TODO здесь будет реализация увеличения атаки
        pass


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_DAMAGE')
        self.__blocked_damage = 0

    def apply_super_power(self, boss, heroes_list):
        boss.health -= self.blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage} damages to boss.')

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'REVIVE')

    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if hero.health <= 0:
                print(f'{self.name} sacrifices himself to revive {hero.name}.')
                hero.health = hero.health + 100  # Примерное количество здоровья при воскрешении
                self.health = 0  # Умирает сам


class Avrora(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'INVISIBILITY')
        self.invisible = False
        self.turns_invisible = 0

    def apply_super_power(self, boss, heroes_list):
        if not self.invisible:
            self.invisible = True
            self.turns_invisible = 2
            print(f'{self.name} has entered invisibility mode!')
        elif self.turns_invisible > 0:
            self.turns_invisible -= 1
        else:
            self.invisible = False
            print(f'{self.name} is now visible!')


class Megumin(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'EXPLOSION')
        self.can_use_ultimate = True

    def apply_super_power(self, boss, heroes_list):
        if self.can_use_ultimate and self.health <= 100:
            print(f'{self.name} is preparing to cast a spell...')
            time.sleep(5)  # Задержка для прочтения заклинания
            boss.health -= 2000
            print(f'{self.name} casts a spell dealing 2000 damage to the boss!')
            self.can_use_ultimate = False  # Можно использовать только один раз


round_number = 0


def is_game_over(boss, heroes_list):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = all(hero.health <= 0 for hero in heroes_list)
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def show_statistics(boss, heroes_list):
    print(f' ------------- ROUND {round_number} -------------')
    print(boss)
    for hero in heroes_list:
        print(hero)


def play_round(boss, heroes_list):
    global round_number
    round_number += 1
    boss.choose_defence(heroes_list)
    boss.attack(heroes_list)
    
    for hero in heroes_list:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes_list)
    
    show_statistics(boss, heroes_list)
    time.sleep(3)  # Пауза между раундами


def start_game():
    boss = Boss(name='Minotavr', health=6000, damage=50)

    warrior_1 = Warrior(name='Asterix', health=290, damage=10)
    warrior_2 = Warrior(name='Obelix', health=280, damage=15)
    magic = Magic(name='Alice', health=270, damage=5)
    berserk = Berserk(name='Guts', health=220, damage=10)
    doc = Medic(name='Doc', health=200, damage=5, heal_points=15)
    assistant = Medic(name='Junior', health=300, damage=5, heal_points=5)
    witcher = Witcher(name='Witcher', health=250, damage=15)
    avrora = Avrora(name='Avrora', health=300, damage=10)
    megumin = Megumin(name='Megumin', health=500, damage=0)

    heroes_list = [warrior_1, doc, warrior_2, magic, berserk, assistant, witcher, avrora, megumin]
    show_statistics(boss, heroes_list)

    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
