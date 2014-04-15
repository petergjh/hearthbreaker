import hsgame.constants

__author__ = 'Daniel'

def powers(character_class):
    if character_class == hsgame.constants.CHARACTER_CLASS.DRUID:
        return DruidPower
    elif character_class == hsgame.constants.CHARACTER_CLASS.MAGE:
        return MagePower
    elif character_class == hsgame.constants.CHARACTER_CLASS.PRIEST:
        return PriestPower


class Power:

    def __init__(self, player):
        self.player = player

    def can_use(self):
        return self.player.mana >= 2

    def use(self):
        if self.can_use():
            self.player.trigger("used_power")
            self.player.mana -= 2


class DruidPower(Power):

    def __init__(self, player):
        super().__init__(player)

    def use(self):
        super().use()
        self.player.increase_attack(1)
        self.player.increase_armour(1)


class MagePower(Power):

    def __init__(self, player):
        super().__init__(player)

    def use(self):
        super().use()
        target = self.player.find_power_target()
        target.damage(1, None)

class PriestPower(Power):

    def __init__(self, player):
        super().__init__(player)

    def use(self):
        super().use()
        target = self.player.find_power_target()
        target.heal(2)
