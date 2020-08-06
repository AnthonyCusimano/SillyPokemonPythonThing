import math

from Moves import Move
from Nature import Nature

class Pokemon:

    def __init__(self, _name):

        self.myName = _name
        self.myIDNum = 0

        self.myNature = 0

        self.myLevel = 50

        self.myTypes = [0, 0]
        self.myMoves = [0, 0, 0, 0]

        self.myTurnsSleeping = 0
        self.mySleepTarget = 0
        self.badPoisonTurns = 0

        # normal, paralyzed(1), asleep(2), poisoned(3), bad poisoned(4), burned(5), frozen(6)
        self.myPrimaryStatus = 0
        self.isConfused = False
        self.isDrowsy = False

        if self.myName == "Poliwrath":
            # water fighting
            self.myTypes[0] = 10
            self.myTypes[1] = 1

            self.myNature = Nature(10)

            self.mySpeciesBaseStats = [90, 95, 95, 70, 90, 70]
            self.myEffortValues = [252, 0, 252, 0, 4, 0]
            self.myBaseStats = [0, 0, 0, 0, 0, 0]
            self.ApplyBaseStats()

            self.myMoves[0] = Move(503)
            self.myMoves[1] = Move(509)
            self.myMoves[2] = Move(95)
            self.myMoves[3] = Move(182)

        elif self.myName == "Hitmonlee":
            # fighting
            self.myTypes[0] = 1
            self.myTypes[1] = -1

            self.myNature = Nature(3)

            self.mySpeciesBaseStats = [50, 120, 53, 35, 110, 87]
            self.myEffortValues = [252, 0, 252, 0, 4, 0]
            self.myBaseStats = [0, 0, 0, 0, 0, 0]
            self.ApplyBaseStats()

            self.myMoves[0] = Move(282)
            self.myMoves[1] = Move(370)
            self.myMoves[2] = Move(174)
            self.myMoves[3] = Move(444)

        elif self.myName == "Jumpluff":
            # flying grass
            self.myTypes[0] = 2
            self.myTypes[1] = 11

            self.myNature = Nature(13)

            self.mySpeciesBaseStats = [75, 55, 70, 55, 95, 110]
            self.myEffortValues = [0, 0, 4, 0, 252, 252]
            self.myBaseStats = [0, 0, 0, 0, 0, 0]
            self.ApplyBaseStats()

            self.myMoves[0] = Move(73)
            self.myMoves[1] = Move(79)
            self.myMoves[2] = Move(369)
            self.myMoves[3] = Move(512)

        elif self.myName == "Magcargo":
            # fire rock
            self.myTypes[0] = 9
            self.myTypes[1] = 5

            self.myNature = Nature(20)

            self.mySpeciesBaseStats = [60, 50, 120, 90, 80, 30]
            self.myEffortValues = [252, 0, 252, 0, 4, 0]
            self.myBaseStats = [0, 0, 0, 0, 0, 0]
            self.ApplyBaseStats()

            self.myMoves[0] = Move(446)
            self.myMoves[1] = Move(281)
            self.myMoves[2] = Move(153)
            self.myMoves[3] = Move(436)

        elif self.myName == "Gorebyss":
            # water
            self.myTypes[0] = 10
            self.myTypes[1] = -1

            self.myNature = Nature(15)

            self.mySpeciesBaseStats = [55, 84, 105, 114, 75, 52]
            self.myEffortValues = [252, 0, 252, 0, 4, 0]
            self.myBaseStats = [0, 0, 0, 0, 0, 0]
            self.ApplyBaseStats()

            self.myMoves[0] = Move(58)
            self.myMoves[1] = Move(56)
            self.myMoves[2] = Move(504)
            self.myMoves[3] = Move(164)

        elif self.myName == "Whimsicott":
            # grass fairy
            self.myTypes[0] = 11
            self.myTypes[1] = 17

            self.myNature = Nature(10)

            self.mySpeciesBaseStats = [60, 67, 85, 77, 75, 116]
            self.myEffortValues = [252, 0, 252, 0, 4, 0]
            self.myBaseStats = [0, 0, 0, 0, 0, 0]
            self.ApplyBaseStats()

            self.myMoves[0] = Move(585)
            self.myMoves[1] = Move(412)
            self.myMoves[2] = Move(94)
            self.myMoves[3] = Move(369)

        self.myCurrentHealth = self.myBaseStats[0]

        self.ApplyNature()

    # double check your work, for no reason in particular :)
    def ApplyNature(self):

        # lonely
        if self.myNature.myID == 1:
            self.myBaseStats[1] *= 1.10
            self.myBaseStats[2] *= 0.90

        # brave
        elif self.myNature.myID == 2:
            self.myBaseStats[1] *= 1.10
            self.myBaseStats[5] *= 0.90

        # adamant
        elif self.myNature.myID == 3:
            self.myBaseStats[1] *= 1.10
            self.myBaseStats[3] *= 0.90

        # naughty
        elif self.myNature.myID == 4:
            self.myBaseStats[1] *= 1.10
            self.myBaseStats[4] *= 0.90

        # bold
        elif self.myNature.myID == 5:
            self.myBaseStats[2] *= 1.10
            self.myBaseStats[1] *= 0.90

        # relaxed
        elif self.myNature.myID == 7:
            self.myBaseStats[2] *= 1.10
            self.myBaseStats[5] *= 0.90

        # impish
        elif self.myNature.myID == 8:
            self.myBaseStats[2] *= 1.10
            self.myBaseStats[3] *= 0.90

        # lax
        elif self.myNature.myID == 9:
            self.myBaseStats[2] *= 1.10
            self.myBaseStats[4] *= 0.90

        # timid
        elif self.myNature.myID == 10:
            self.myBaseStats[5] *= 1.10
            self.myBaseStats[1] *= 0.90

        # hasty
        elif self.myNature.myID == 11:
            self.myBaseStats[5] *= 1.10
            self.myBaseStats[2] *= 0.90

        # jolly
        elif self.myNature.myID == 13:
            self.myBaseStats[5] *= 1.10
            self.myBaseStats[3] *= 0.90
            self.myBaseStats[5] = math.floor(self.myBaseStats[5])
            self.myBaseStats[3] = math.floor(self.myBaseStats[3])

        # naive
        elif self.myNature.myID == 14:
            self.myBaseStats[5] *= 0.90
            self.myBaseStats[4] *= 1.10

        # modest
        elif self.myNature.myID == 15:
            self.myBaseStats[3] *= 0.90
            self.myBaseStats[1] *= 1.10

        # mild
        elif self.myNature.myID == 16:
            self.myBaseStats[3] *= 0.90
            self.myBaseStats[2] *= 1.10

        # quiet
        elif self.myNature.myID == 17:
            self.myBaseStats[3] *= 0.90
            self.myBaseStats[5] *= 1.10

        # rash
        elif self.myNature.myID == 19:
            self.myBaseStats[3] *= 0.90
            self.myBaseStats[5] *= 1.10

        # calm
        elif self.myNature.myID == 20:
            self.myBaseStats[4] *= 0.90
            self.myBaseStats[1] *= 1.10

        # gentle
        elif self.myNature.myID == 21:
            self.myBaseStats[4] *= 0.90
            self.myBaseStats[2] *= 1.10

        # sassy
        elif self.myNature.myID == 22:
            self.myBaseStats[4] *= 0.90
            self.myBaseStats[5] *= 1.10

        # careful
        elif self.myNature.myID == 23:
            self.myBaseStats[4] *= 0.90
            self.myBaseStats[3] *= 1.10

        if self.myName == "Jumpluff":
            for i in range(6):
                print(self.myBaseStats[i])

    def ApplyBaseStats(self):
        # every pokemon in this app is 50
        # all instances of 50 in these formulas could be replaced by self.level if we included it
        # every pokemon has 31 IVs in every stat
        # TODO need nature implementation
        self.myBaseStats[0] = math.floor(((2 * self.mySpeciesBaseStats[0] + 31 + (self.myEffortValues[0] / 4))
                                          * 50 / 100) + 50 + 10)

        for i in range(1, 6):
            self.myBaseStats[i] = math.floor(((2 * self.mySpeciesBaseStats[i] + 31 + (self.myEffortValues[i] / 4))
                                              * 50 / 100) + 5)
