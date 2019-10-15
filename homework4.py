import random
class Warrior:
    name = ''
    health = 0
    power = 0
    def __init__(self, name):
        self.name = name
        self.health = random.randint(100, 150)
        self.power = random.randint(20, 30)
    def showHealth(self):
        return self.health
    def showPower(self):
        return self.power
    def getDamage(self, power2):
        self.health = self.health - power2
        if self.health > 0:
            print('Воин {0} получил {1} урона. Осталось {2} здоровья'.format(self.name, power2, self.health))
        else:
            print('Воин {0} получил {1} урона и погиб'.format(self.name, power2))

class ShieldWarrior(Warrior):
    shield = 0
    def __init__(self, name):
        Warrior.__init__(self, name)
        self.shield = random.randint(5, 10)
    def getDamage(self, power2):
        self.health = self.health - power2 + self.shield
        if self.health > 0:
            print('Воин {0} получил {1} урона. Осталось {2} здоровья'.format(self.name, power2 - self.shield, self.health))
        else:
            print('Воин {0} получил {1} урона и погиб'.format(self.name, power2 - self.shield))


class ExpertWarrior(Warrior):
    def showPower(self):
        Warrior.showPower(self)
        p = random.randint(1, 5)
        if p == 1:
            return self.power * 2
        else:
            return self.power

#Задача 1 (создать объекты):

warrior1 = ShieldWarrior('Алеша')
warrior1.getDamage(30)

warrior2 = ShieldWarrior('Добрыня')
warrior2.getDamage(30)

warrior3 = ExpertWarrior('Илья')
warrior3.getDamage(30)

#Задача 2 (провести бои друг с другом):

#бой между обычным воином и воином со щитом:

warrior1 = ShieldWarrior('Алеша')
warrior2 = ShieldWarrior('Добрыня')

while warrior1.health >= 0 and warrior2.health >= 0:
    warrior1.getDamage(warrior2.power)
    if warrior1.health < 0:
        print('Воин', warrior2.name, 'победил')
        break
    warrior2.getDamage(warrior1.power)
    if warrior2.health < 0:
        print('Воин', warrior1.name, 'победил')
        break

#бой между обычным воином и воином-экспертом:

warrior1 = ShieldWarrior('Алеша')
warrior3 = ExpertWarrior('Илья')

while warrior1.health >= 0 and warrior3.health >= 0:
    warrior1.getDamage(warrior3.power)
    if warrior1.health < 0:
        print('Воин', warrior3.name, 'победил')
        break
    warrior3.getDamage(warrior1.power)
    if warrior3.health < 0:
        print('Воин', warrior1.name, 'победил')
        break

#бой между воином со щитом и воином-экспертом:

warrior2 = ShieldWarrior('Добрыня')
warrior3 = ExpertWarrior('Илья')

while warrior2.health >= 0 and warrior3.health >= 0:
    warrior2.getDamage(warrior3.power)
    if warrior2.health < 0:
        print('Воин', warrior3.name, 'победил')
        break
    warrior3.getDamage(warrior2.power)
    if warrior3.health < 0:
        print('Воин', warrior2.name, 'победил')
        break

#Задача 3 (провести бои между двумя армиями):

army1 = []
army2 = []

for i in range(1, 5):
    war = Warrior('1 армии обычный'+ str(i))
    army1.append(war)
    war = Warrior('2 армии обычный'+ str(i))
    army2.append(war)
for i in range(5, 9):
    war = ShieldWarrior('1 армии с защитой'+ str(i))
    army1.append(war)
    war = ShieldWarrior('2 армии с защитой'+ str(i))
    army2.append(war)
for i in range(9, 11):
    war = ExpertWarrior('1 армии эксперт'+ str(i))
    army1.append(war)
    war = ExpertWarrior('2 армии эксперт'+ str(i))
    army2.append(war)

q = 1
while len(army1) > 0 and len(army2) > 0:
    i = random.randint(0, len(army1)-1)
    j = random.randint(0, len(army2)-1)
    if q % 2 == 1:
        while army1[i].health >= 0 and army2[j].health >= 0:
            army2[j].getDamage(army1[i].power)
            if army2[j].health < 0:
                del army2[j]
                break
            army1[i].getDamage(army2[j].power)
            if army1[i].health < 0:
                del army1[i]
                break
        q = q + 1
    else:
        while army1[i].health >= 0 and army2[j].health >= 0:
            army1[i].getDamage(army2[j].power)
            if army1[i].health < 0:
                del army1[i]
                break
            army2[j].getDamage(army1[i].power)
            if army2[j].health < 0:
                del army2[j]
                break
        q = q + 1
if len(army1) <= 0:
    print('Армия_2 победила')
if len(army2) <= 0:
    print('Армия_1 победила')
