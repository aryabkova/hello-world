import random
class Warrior:
    health = random.randint(100, 150)
    power = random.randint(20, 30)
    def __init__(self, name):
        self.name = name
    def showHealth(self):
        print('Воин', self.name, '. Здоровье:', self.health)
    def showPower(self):
        print('Воин', self.name, '. Сила атаки:', self.power)
    def weaken(self, power2):
        self.health = self.health - power2
        if self.health > 0:
            print('Воин', self.name, 'получил', power2, 'урона. Осталось', self.health, 'здоровья')
        else:
            print('Воин', self.name, 'получил', power2, 'урона и погиб')


class ShieldWarrior(Warrior):
    shield = random.randint(5, 10)
    def showShield(self):
        print('Воин', self.name, 'имеет', self.shield, 'защиты')
    def weaken(self, power2):
        self.health = self.health - power2 + self.shield
        if self.health > 0:
            print('Воин', self.name, 'получил', power2, 'урона. Осталось', self.health, 'здоровья')
        else:
            print('Воин', self.name, 'получил', power2, 'урона и погиб')


class ExpertWarrior(Warrior):
    def showPower(self):
        powerexp = self.power
        p = random.randint(1, 5)
        if p == 1:
            powerexp = self.power * 2
        else:
            powerexp = self.power
        print('Воин', self.name, '. Сила атаки:', powerexp)


#задача 1:

Warrior1 = Warrior('Алеша')
Warrior1.showHealth()
Warrior1.showPower()
Warrior1.weaken(25)

Warrior2 = ShieldWarrior('Добрыня')
Warrior2.showHealth()
Warrior2.showPower()
Warrior2.showShield()
Warrior2.weaken(30)

Warrior3 = ExpertWarrior('Илья')
Warrior3.showHealth()
Warrior3.showPower()
Warrior3.weaken(30)

#задача 2:

#бой между обычным воином и воином со щитом:

Warrior1 = Warrior('Алеша')
Warrior2 = ShieldWarrior('Добрыня')

while Warrior1.health >= 0 and Warrior2.health >= 0:
    Warrior1.weaken(Warrior2.power)
    if Warrior1.health < 0:
        print(Warrior2.name, 'победил')
        break
    Warrior2.weaken(Warrior1.power)
    if Warrior2.health < 0:
        print(Warrior1.name, 'победил')
        break

#бой между обычным воином и воином-экспертом:

Warrior1 = Warrior('Алеша')
Warrior3 = ShieldWarrior('Илья')

while Warrior1.health >= 0 and Warrior3.health >= 0:
    Warrior1.weaken(Warrior3.power)
    if Warrior1.health < 0:
        print(Warrior3.name, 'победил')
        break
    Warrior3.weaken(Warrior1.power)
    if Warrior3.health < 0:
        print(Warrior1.name, 'победил')
        break

#бой между воином с щитом и воином-экспертом:

Warrior2 = Warrior('Алеша')
Warrior3 = ShieldWarrior('Илья')

while Warrior2.health >= 0 and Warrior3.health >= 0:
    Warrior2.weaken(Warrior3.power)
    if Warrior2.health < 0:
        print(Warrior3.name, 'победил')
        break
    Warrior3.weaken(Warrior2.power)
    if Warrior3.health < 0:
        print(Warrior2.name, 'победил')
        break

