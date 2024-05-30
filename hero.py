class SuperHero:
    people ="people"
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def test(self):
            print(self.name, self.nickname, self.superpower, self.health_points, self.catchphrase)

    def __str__(self):
                return (f'имя : {self.name}\n'
                        f'произвище : {self.nickname}\n'
                        f'суперсила : {self.superpower}\n'
                        f'очки здоровья : {self.health_points}\n'
                        f'крылатая фраза : {self.catchphrase}\n'
                        f'-----------------------\n')

    def double_health(self):
        return (self.health_points)*2

    def __len__(self):
        return len(self.catchphrase)
will = SuperHero ('will', 'megamind','genius', 100,'Даже у судьбы есть свои любимчики')
print(will.test())
print(will.double_health())
print(len(will))
print(str(will))