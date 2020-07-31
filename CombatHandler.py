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

    def ProcessPlayerPokemonDeath(self, _pokemon, _player):
        print(_pokemon.myName, " has fainted!")
        print("Select goon to swap to")
        print("1: ", _player.myTeam[1].myName, " ", _player.myTeam[1].myCurrentHealth, "/",
              _player.myTeam[1].myBaseStats[0])
        print("2: ", _player.myTeam[2].myName, " ", _player.myTeam[2].myCurrentHealth, "/",
              _player.myTeam[2].myBaseStats[0])
        T_Input = int(input())
        _player.swap(T_Input)

    def ProcessComputerPokemonDeath(self, _pokemon, _computer, _computerAI):
        print(_pokemon.myName, " has fainted!")
        _computerAI.swap(_computer.myTeam)

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

        # ice beam
        if _move.myIDNum == 58:
            T_DieRoll = self.rollD100()
            # 10%
            if T_DieRoll > 90:
                _defender.myPrimaryStatus = 6

        # leech seed
        if _move.myIDNum == 73:
            _defender.isSeeded = True

        # sleep powder
        if _move.myIDNum == 79:
            _defender.myPrimaryStatus = 2

        # Psychic
        # TODO
        if _move.myIDNum == 94:
            T_DieRoll = self.rollD100()
            # 10%
            if T_DieRoll > 90:
                print("please lower defender's special defense by one stage, I still don't know what that means LOLE")

        # hypnosis
        elif _move.myIDNum == 95:
            _defender.myPrimaryStatus = 2

        # TODO
        # substitute
        elif _move.myIDNum == 164:
            print("bro why did I even put substitute in this thing")

        # Yawn
        elif _move.myIDNum == 281:
            _defender.isDrowsy = True

        # TODO
        # knockoff
        elif _move.myIDNum == 282:
            print("knockoff currently doing nothing because Items aren't in the game yet lole")

        # TODO
        # uturn
        elif _move.myIDNum == 369:
            print("Need access to Trainer.swap method so uturn can do the turn part")

        # close combat
        # TODO LOLE THIS SUCKS
        elif _move.myIDNum == 370:
            --_attacker.myBaseStats[2]
            --_attacker.myBaseStats[4]

        # stealth rocks
        # TODO
        elif _move.myIDNum == 446:
            print("Need defender's trainer to stealth rock it up")

        # scald
        elif _move.myIDNum == 503:
            _defender.myPrimaryStatus = 5

        # shell smash
        # TODO
        elif _move.myIDNum == 504:
            print("shell smash")

        # circle throw
        # TODO
        elif _move.myIDNum == 509:
            print("circle throw")

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
        self.ProcessDamage(_attacker, _defender, _move)
        self.MoveSecondaryAffect(_move, _attacker, _defender)

    # TODO comment
    def ProcessTurn(self, _actionTypeID, _actionID, _player, _computer, _computerAI, _playerPokemon, _computerPokemon):
        if _actionTypeID == 0:
            _player.swap(_actionID)

            # TODO
            # comp attacks still LOLE!

        elif _actionTypeID == 1:

            print("actionTypeID == 1")

            T_PlayerAttackPossible = True
            T_ComputerAttackPossible = True

            T_ComputerPrio = 0
            T_PlayerPrio = 0

            # TODO
            # determinePrio needs to exist eventually

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

            if _computerPokemon.myPrimaryStatus == 1:
                T_ParCheck = self.rollD100()
                if T_ParCheck > 50:
                    print("computer is paralyzed LOLE!!!!!")
                    T_ComputerAttackPossible = False

            if T_PlayerAttackPossible:
                print("Attacking the comp naow")
                self.ProcessMove(_playerPokemon, _computerPokemon, _player.selectMove(_actionID))
                if _computerPokemon.myCurrentHealth > 0 and T_ComputerAttackPossible:
                    self.ProcessDamage(_computerPokemon, _playerPokemon, _computerAI.selectMove(_computerPokemon))

            # else:
            self.ProcessMove(_computerPokemon, _playerPokemon, _computerAI.selectMove(_computerPokemon))
            if _playerPokemon.myCurrentHealth > 0 and T_PlayerAttackPossible:
                self.ProcessMove(_playerPokemon, _computerPokemon,
                                 _player.selectMove(_player.myTeam[0].myMoves[_actionID]))

            # TODO
            print("Need bad poison check at the end of ProcessTurn")

            # player statuses
            # poison
            if _playerPokemon.myPrimaryStatus == 3:
                print("Player is hurt by poison")
                _playerPokemon.myCurrentHealth -= _playerPokemon.myBaseStats[0] * 0.125

            elif _playerPokemon.myPrimaryStatus == 4:
                print("Player is hurt by bad poison")
                ++_playerPokemon.badPoisonTurns

            elif _playerPokemon.myPrimaryStatus == 5:
                print("Burn taking place at the end of turn, not accounting for case where PlayerPokemon attacked",
                      " where it should trigger right after their attack")
                _playerPokemon.myCurrentHealth -= _playerPokemon.myBaseStats[0] * 0.125

            # computer statuses
            if _computerPokemon.myPrimaryStatus == 3:
                print("computer is hurt by poison")

            elif _computerPokemon.myPrimaryStatus == 4:
                print("computer is hurt by bad poison")
                ++_computerPokemon.badPoisonTurns

            elif _computerPokemon.myPrimaryStatus == 5:
                print("Burn taking place at the end of turn, not accounting for case where ComputerPokemon attacked",
                      " where it should trigger right after their attack")
                _computerPokemon.myCurrentHealth -= _computerPokemon.myBaseStats[0] * 0.125

            print("Beginning death checks")
            if _playerPokemon.myCurrentHealth <= 0:
                self.ProcessPlayerPokemonDeath(_playerPokemon, _player)

            if _computerPokemon.myCurrentHealth < 1:
                self.ProcessComputerPokemonDeath(_computerPokemon, _computer, _computerAI)
