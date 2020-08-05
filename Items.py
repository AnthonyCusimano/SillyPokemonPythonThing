import math


def restorePokemonHealth (_pokemon, _healthRestored):

    if _pokemon.myCurrentHealth + _healthRestored > _pokemon.myBaseStats[0]:
        _pokemon.myCurrentHealth = _pokemon.myBaseStats[0]

    else:
        _pokemon.myCurrentHealth += _healthRestored


#
class Item:

    def __init__(self, _name):
        self.myName = _name

        if self.myName == "Red Card":
            self.myIDNumber = 1

        elif self.myName == "Leftovers":
            self.myIDNumber = 2

    def ProcessMyEndOfTurnEffect(self, _myHolder):
        print("Item end of turn item effect")
        # leftovers
        if self.myIDNumber == 2:
            restorePokemonHealth(_myHolder, math.floor(_myHolder.myBaseStats[0] * 0.0625))

    def ProcessMyOnAttackedEffect(self, _attack, _myHolder, _attacker, _attackerTrainer):
        print("Item on attacked effect")
