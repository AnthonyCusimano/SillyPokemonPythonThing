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
            self.myBaseStats = [0, 0, 0, 0, 0, 0]
            self.ApplyBaseStats()

            self.myMoves[0] = Move(585)
            self.myMoves[1] = Move(412)
            self.myMoves[2] = Move(94)
            self.myMoves[3] = Move(369)

        self.myCurrentHealth = self.myBaseStats[0]

        self.ApplyNature()

    # for now just applying Jumpluff's jolly nature
    def ApplyNature(self):
        if self.myNature.myID == 13:
            self.myBaseStats[3] *= 0.90
            self.myBaseStats[5] *= 1.10

    def ApplyBaseStats(self):
        # every pokemon in this app is 50
        # all instances of 50 in these formulas could be replaced by self.level if we included it
        # every pokemon has 31 IVs in every stat
        # TODO need EVs
        self.myBaseStats[0] = math.floor(((2 * self.mySpeciesBaseStats[0] + 31) * 50 / 100) + 50 + 10)

        for i in range(1, 6):
            self.myBaseStats[i] = self.mySpeciesBaseStats[i]

        if self.myName == "Jumpluff":
            for i in range(6):
                print(self.myBaseStats[i])
