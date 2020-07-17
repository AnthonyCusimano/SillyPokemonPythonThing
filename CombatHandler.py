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
        self.playerCritStage = 0
        self.enemyCritStage = 0

    # TODO comment
    def returnIsStab(self, _user, _move):
        if _user.myTypes[0] == _move.myType or _user.myTypes[1] == _move.myType:
            return 1

        else:
            return 0

    # TODO comment
    def returnCrit(self, _attacker, _boolPlayerIsAttacking):
        T_CritRoll = random.randrange(24)  # need access to crit stages in battle

        if _boolPlayerIsAttacking:
            if self.playerCritStage == 0 and T_CritRoll == 24:
                return 1.5

            elif self.playerCritStage == 1 and T_CritRoll > 16:  # I think?
                return 1.5

            elif self.playerCritStage == 2 and T_CritRoll > 12:  # I'm pretty sure?!?!
                return 1.5

            elif self.playerCritStage == 3:
                return 1.5

        if not _boolPlayerIsAttacking:
            if self.enemyCritStage == 0 and T_CritRoll == 24:
                return 1.5

            elif self.enemyCritStage == 1 and T_CritRoll > 16:  # I think?
                return 1.5

            elif self.enemyCritStage == 2 and T_CritRoll > 12:  # I'm pretty sure?!?!
                return 1.5

            elif self.enemyCritStage == 3:
                return 1.5


        else:
            return 1

    # TODO comment
    def CalculateTypeEffectiveness(self, _move, _attacker, _defender):
        print("prototype method CalculateTypeEffectiveness called")
        # leaving this blank cus I need to come up with a good way to do this using the chart above this class
        T_Modifier = typeEffectiveness[_move.myType][_defender.myTypes[0]]

        if _defender.myTypes[2] != -1:
            T_Modifier *= typeEffectiveness[_move.myType][_defender.myTypes[1]]

        # check for 

        return T_Modifier


    # TODO comment
    def rollAccuracy(self, _move):
        T_Role = random.randrange(1, 100)
        if T_Role <= _move.myAccuracy:
            return True

        else:
            return False

    def rollD100(self):
        return random.randrange(1, 100)

    # currently doesn't involve switching, should it? :0
    def DetermineSpeedOrder(self, _pokemon1, _pokemon2):
        # return
        if _pokemon1.myBaseStats[5] > _pokemon2.myBaseStats[5]:
            return 0

        elif _pokemon1.myBaseStats[5] < _pokemon2.myBaseStats[5]:
            return 1

        # speed tie
        else:
            # coinflip return
            return random.randrange(1)

    def MoveSecondaryAffect(self, _move, _attacker, _defender):
        # sleep powder
        if _move.myIDNum == 79:
            _defender.myPrimaryStatus = 2

    # TODO comment
    def ProcessDamage(self, _attacker, _defender, _move):
        # TODO improve :)
        print("_move's name is ", _move.myName)
        print("_move's base power is  ", _move.myBasePower)
        print("_attacker's attack is ", _attacker.myBaseStats[1])
        print("_defender's defense is ", _defender.myBaseStats[3])
        T_Damage = (2 * 50) + 2

        if _move.myDamageType == 1:
            T_Damage *= _move.myBasePower * (_attacker.myBaseStats[1] / _defender.myBaseStats[3])

        elif _move.myDamageType == 2:
            T_Damage *= _move.myBasePower * (_attacker.myBaseStats[2] / _defender.myBaseStats[4])

        else:  # meaning it's a special / status move
            return

        T_Damage /= 50
        T_Damage + 2
        print(T_Damage, " is damage before T_DamageMod applied")
        T_DamageMod = random.randrange(85, 100) / 100

        #TODO Adaptability (pokmemon ability) check
        if self.returnIsStab(_attacker, _move) == 1:
            T_DamageMod *= 1.5

        # true as in player is attacking, for now
        T_DamageMod *= self.returnCrit(_attacker, True)

        T_Damage *= T_DamageMod

        print(T_Damage)
        _defender.myCurrentHealth -= T_Damage

        # ignoring weather, badge, targets,

    def ProcessMove(self, _attacker, _defender, _move):
        self.ProcessDamage(_move)
        self.MoveSecondaryAffect(_move)

    # TODO comment
    def ProcessTurn(self, _actionTypeID, _actionID, _player, _computer, _computerAI, _playerPokemon, _computerPokemon):
        if _actionTypeID == 0:
            _player.swap(_actionID)

        elif _actionTypeID == 1:
            T_PlayerAttackPossible = True
            T_ComputerAttackPossible = True

            T_Order = self.DetermineSpeedOrder(_playerPokemon, _computerPokemon)

            # paralyze  
            if _playerPokemon.myPrimaryStatus == 1:
                T_ParCheck = self.rollD100()
                if T_ParCheck > 50:
                    print("lole ur paralyze lole!")
                    T_PlayerAttackPossible = False

                else:
                    print("you're attack is going off even though you're paralized, lucky :)")

            # sleep
            elif _playerPokemon.myPrimaryStatus == 2:
                if _playerPokemon.myTurnsSleeping == _playerPokemon.mySleepTarget:
                    # waking up
                    _playerPokemon.myPrimaryStatus = 0
                    _playerPokemon.myTurnsSleeping = _playerPokemon.mySleepTarget = 0
                    print(_playerPokemon.myName, " woke up!!!!!!!!!!!!!!")

                else:
                    ++_playerPokemon.myTurnsSleeping
                    T_PlayerAttackPossible = False

            # freeze
            elif _playerPokemon.myPrimaryStatus == 6:
                T_ThawCheck = self.rollD100()
                if T_ThawCheck > 80:
                    _playerPokemon.myPrimaryStatus = 0

                else:
                    print("Still frozen :)")
                    T_PlayerAttackPossible = False

            if T_PlayerAttackPossible:
                self.ProcessMove(_playerPokemon, _computerPokemon, _player.selectMove(_actionID))
                if (_computerPokemon.myCurrentHealth > 0 and T_ComputerAttackPossible):
                    self.ProcessDamage(_computerPokemon, _playerPokemon, _computer.selectMove())

            # else:
            self.ProcessMove(_computerPokemon, _playerPokemon, _computerAI.selectMove(_computerPokemon))
            if (_playerPokemon.myCurrentHealth > 0 and T_PlayerAttackPossible):
                self.ProcessMove(_playerPokemon, _computerPokemon, _player.selectMove(_actionID))

            # TODO
            print("Need poison, bad poison, and burn checks at the end of ProcessTurn")
