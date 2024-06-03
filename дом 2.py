class SuperHero:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.fly = False

    def double_hp(self):
        self.hp *= 2

class AirHero(SuperHero):
    def __init__(self, name, hp, damage, air_property):
        super().__init__(name, hp, damage)
        self.air_property = air_property

    def double_hp(self):
        self.hp **= 2
        self.fly = True

    def true_phrase(self):
        return f"True in the {self.air_property}"

class LandHero(SuperHero):
    def __init__(self, name, hp, damage, land_property):
        super().__init__(name, hp, damage)
        self.land_property = land_property

    def double_hp(self):
        self.hp **= 2
        self.fly = True

    def true_phrase(self):
        return f"True in the {self.land_property}"

class SpaceHero(SuperHero):
    def __init__(self, name, hp, damage, space_property):
        super().__init__(name, hp, damage)
        self.space_property = space_property

    def double_hp(self):
        self.hp **= 2
        self.fly = True

    def true_phrase(self):
        return f"True in the {self.space_property}"

# Создание объектов для новых классов и вызов новых методов
air_hero = AirHero("Wind Warrior", 100, 20, "sky")
land_hero = LandHero("Earth Guardian", 150, 30, "ground")
space_hero = SpaceHero("Cosmic Defender", 200, 40, "universe")

print(air_hero.true_phrase())
print(land_hero.true_phrase())
print(space_hero.true_phrase())

air_hero.double_hp()
land_hero.double_hp()
space_hero.double_hp()

print(air_hero.hp, air_hero.fly)
print(land_hero.hp, land_hero.fly)
print(space_hero.hp, space_hero.fly)

class Villain(SpaceHero):
    def __init__(self, name, hp, damage, space_property):
        super().__init__(name, hp, damage, space_property)
        self.people = "monster"

    def gen_x(self):
        pass

    def crit(self, target):
        target.damage **= 2

# Создание объекта для класса Villain
villain = Villain("Galactic Overlord", 300, 50, "dark space")

# Применение метода crit на объект другого класса, у которого есть аргумент damage
villain.crit(air_hero)
print(air_hero.damage)

villain.crit(land_hero)
print(land_hero.damage)

villain.crit(space_hero)
print(space_hero.damage)
