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

        if self.myName == "Poliwrath":
            # water fighting
            self.myTypes[0] = 10
            self.myTypes[1] = 1

            self.myNature = Nature(10)

            self.myBaseStats = [90, 95, 95, 70, 90, 70]

            self.myMoves[0] = Move(503)
            self.myMoves[1] = Move(509)
            self.myMoves[2] = Move(95)
            self.myMoves[3] = Move(182)

        elif self.myName == "Hitmonlee":
            # fighting
            self.myTypes[0] = 1
            self.myTypes[1] = -1

            self.myNature = Nature(3)

            self.myBaseStats = [50, 120, 53, 35, 110, 87]

            self.myMoves[0] = Move(282)
            self.myMoves[1] = Move(370)
            self.myMoves[2] = Move(174)
            self.myMoves[3] = Move(444)

        elif self.myName == "Jumpluff":
            # flying grass
            self.myTypes[0] = 2
            self.myTypes[1] = 11

            self.myNature = Nature(13)

            self.myBaseStats = [75, 55, 70, 55, 95, 110]

            self.myMoves[0] = Move(73)
            self.myMoves[1] = Move(79)
            self.myMoves[2] = Move(369)
            self.myMoves[3] = Move(512)

        elif self.myName == "Magcargo":
            # fire rock
            self.myTypes[0] = 9
            self.myTypes[1] = 5

            self.myNature = Nature(20)

            self.myBaseStats = [60, 50, 120, 90, 80, 30]

            self.myMoves[0] = Move(446)
            self.myMoves[1] = Move(281)
            self.myMoves[2] = Move(153)
            self.myMoves[3] = Move(436)

        elif self.myName == "Gorebyss":
            # water
            self.myTypes[0] = 10
            self.myTypes[1] = -1

            self.myNature = Nature(15)

            self.myBaseStats = [55, 84, 105, 114, 75, 52]

            self.myMoves[0] = Move(58)
            self.myMoves[1] = Move(56)
            self.myMoves[2] = Move(504)
            self.myMoves[3] = Move(164)

        elif self.myName == "Whimsicott":
            # grass fairy
            self.myTypes[0] = 11
            self.myTypes[1] = 17

            self.myNature = Nature(10)

            self.myBaseStats = [60, 67, 85, 77, 75, 116]

            self.myMoves[0] = Move(585)
            self.myMoves[1] = Move(412)
            self.myMoves[2] = Move(94)
            self.myMoves[3] = Move(369)

        self.ApplyNature()

    # for now just applying Jumpluff's jolly nature
    def ApplyNature(self):
        if self.myNature.myID == 13:
            self.myBaseStats[3] *= 0.90
            self.myBaseStats[5] *= 1.10
