from Moves import Move


class Pokemon:

    def __init__(self, _name):

        self.myName = _name
        self.myIDNum = 0

        self.myTypes = [0, 0]
        self.myMoves = [0, 0, 0, 0]

        if self.myName == "Poliwrath":
            # water fighting
            self.myTypes[0] = 10
            self.myTypes[1] = 1

            self.myBaseStats = [90, 95, 95, 70, 90, 70]

            self.myMoves[0] = Move(503)
            self.myMoves[1] = Move(509)
            self.myMoves[2] = Move(95)
            self.myMoves[3] = Move(182)

        elif self.myName == "Hitmonlee":
            #fighting
            self.myTypes[0] = 1
            self.myTypes[1] = -1

            self.myBaseStats = [50, 120, 53, 35, 110, 87]

            self.myMoves[0] = Move(282)
            self.myMoves[1] = Move(370)
            self.myMoves[2] = Move(174)
            self.myMoves[3] = Move(444)

        elif self.myName == "Jumpluff":
            # flying grass
            self.myTypes[0] = 2
            self.myTypes[1] = 11

            self.myBaseStats = [75, 55, 70, 55, 95, 110]

            self.myMoves[0] = Move(73)
            self.myMoves[1] = Move(79)
            self.myMoves[2] = Move(369)
            self.myMoves[3] = Move(512)

        elif self.myName == "Whimsicott":
            # grass fairy
            self.myTypes[0] = 11
            self.myTypes[1] = 17

            self.myBaseStats = [60, 67, 85, 77, 75, 116]

            self.myMoves[0] = Move(585)
            self.myMoves[1] = Move(412)
            self.myMoves[2] = Move(94)
            self.myMoves[3] = Move(369)
