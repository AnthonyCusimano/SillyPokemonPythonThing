import random

#TODO
# proofread this chart maybe even format it different or something
typeEffectiveness = [[1, 1, 1, 1, 1, 0.5, 1, 0, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # normal
                     [2, 1, 0.5, 0.5, 1, 2, 0.5, 0, 2, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5],  # fighting
                     [1, 2, 1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 2, 0.5, 1, 1, 1, 1, 1],  # flying
                     [1, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 0, 1, 1, 2, 1, 1, 1, 1, 1, 2],  # poison
                     [1, 1, 0, 2, 1, 2, 0.5, 1, 2, 2, 1, 0.5, 2, 1, 1, 1, 1, 1],  # ground
                     [1, 0.5, 2, 1, 0.5, 1, 2, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 1, 1],  # rock
                     [1, 0.5, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 0.5, 1, 2, 1, 2, 1, 1, 2, 0.5],  # bug
                     [0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 1],  # ghost
                     [1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 1, 2, 1, 1, 2],  # steel
                     [1, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5, 0.5, 2, 0.5, 0.5, 2, 1, 1, 2, 0.5, 1, 1],  # fire
                     [1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 1, 0.5, 1, 1],  # water
                     [1, 1, 0.5, 0.5, 2, 2, 0.5, 1, 0.5, 0.5, 2, 0.5, 1, 1, 1, 0.5, 1, 1],  # grass
                     [1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 0.5, 1, 1],  # electric
                     [1, 2, 1, 2, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 0, 1],  # psychic
                     [1, 1, 2, 1, 2, 1, 1, 1, 0.5, 0.5, 0.5, 2, 1, 1, 0.5, 2, 1, 1],  # ice
                     [1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 2, 1, 0],  # dragon
                     [1, 0.5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5],  # dark
                     [1, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 0.5, 1, 1, 1, 1, 1, 2, 2, 1]]  # fairy


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
