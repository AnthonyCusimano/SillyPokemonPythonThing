import random


class CombatHandler:

    def __init__(self):
        print("CombatHandler default constructor called")

    def returnIsStab(self, _user, _move):
        if _user.myType == _move.myType:
            return 1

        else:
            return 0

    def roleAccuracy(self, _move):
        T_Role = random.randrange(1, 100)
        if T_Role <= _move.myAccuracy:
            return True

        else:
            return False

    def ProcessDamage(self, _attacker, _defender, _move):
        # TODO improve :)
        print("Damage dealt with my calc is currently ", _move.myBasePower)
