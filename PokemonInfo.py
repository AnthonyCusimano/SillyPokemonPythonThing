from Moves import Move


class Pokemon:

    def __init__(self, _name):

        # myBaseStats = [0, 0, 0, 0, 0, 0]

        self.myName = _name
        self.myIDNum = 0

        self.myTypes = [0, 0]
        self.myMoves = [0, 0, 0, 0]

        if self.myName == "Poliwrath":
            # water fighting
            self.myTypes[0] = 10
            self.myTypes[1] = 1

            self.myMoves[0] = Move(503)
            self.myMoves[1] = Move(509)
            self.myMoves[2] = Move(95)
            self.myMoves[3] = Move(182)

        elif self.myName == "Jumpluff":
            # flying grass
            self.myTypes[0] = 2
            self.myTypes[1] = 11

            self.myMoves[0] = Move(73)
            self.myMoves[1] = Move(79)
            self.myMoves[2] = Move(369)
            self.myMoves[3] = Move(512)

        elif self.myName == "Whimsicott":
            # grass fairy
            self.myTypes[0] = 11
            self.myTypes[1] = 17

            self.myMoves[0] = Move(585)
            self.myMoves[1] = Move(412)
            self.myMoves[2] = Move(94)
            self.myMoves[3] = Move(369)
