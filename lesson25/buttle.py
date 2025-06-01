from consts import RANKS
class Warrior:
    def __init__(self, level = 1, rank = 'Pushover', xp = 100, achievements = ()):
        self.level = level
        self.rank = rank
        self.xp = xp
        self.achievements = [*achievements]

    def battle(self, enemy_lvl):
        if enemy_lvl < 1 or enemy_lvl > 100:
            return 'Invalid level'
        diff = self.level - enemy_lvl
        if diff == 0:
            self.xp += 10
            self.check_rank()
            return 'Draw fight'
        elif diff == 1:
            self.xp += 5
            self.check_rank()
            return 'A good fight'
        elif diff >= 2:
            self.xp += 0
            self.check_rank()
            return 'Easy fight'
        elif -5 <= diff <= -1:
            self.xp += 20 * diff * diff
            self.check_rank()
            return 'An intense fight'
        else:
            return "You've been defeated"
    def training (self, name, xp, level):
        if self.level >= level:
            self.xp += xp
            self.check_rank()
            self.achievements.append(name)
            return name
        return 'Not strong enough'
    def check_rank(self):
        self.level = self.xp // 100
        for i in RANKS:
            if self.level in i['rank']:
                self.rank = i['name']

bruce_lee = Warrior()
print(bruce_lee.level)
print(bruce_lee.xp)
print(bruce_lee.rank)
print(bruce_lee.achievements)
bruce_lee.training("Defeted Chuck Norris", 2900, 1)
print(bruce_lee.level)
print(bruce_lee.xp)
print(bruce_lee.rank)
print(bruce_lee.achievements)
bruce_lee.battle(90)
print(bruce_lee.xp)



