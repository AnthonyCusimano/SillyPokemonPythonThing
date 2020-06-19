import random

# TODO
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


# mostly static methods pertaining to processing the effects of different pokemon attacks
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
        print("_move's base power is  ", _move.myBasePower)
        print("_attacker's attack is ", _attacker.myBaseStats[1])
        print("_defender's defense is ", _defender.myBaseStats[3])
        T_Damage = (2 * 50) + 2
        # for now we pretend all moves are physical and target defense
        if _move.myDamageType == 1:
            T_Damage *= _move.myBasePower * (_attacker.myBaseStats[1] / _defender.myBaseStats[3])

        else:
            T_Damage *= _move.myBasePower * (_attacker.myBaseStats[2] / _defender.myBaseStats[4])

        T_Damage /= 50
        T_Damage + 2
        print(T_Damage)
        T_DamageMod = 1
