from Moves import *

class Pokemon:
    myName = ''
    myIDNum = 0

    myTypes = [0, 0]
    myMoves = Move[0, 0, 0, 0]

    myBaseStats = [0, 0, 0, 0, 0, 0,]

    def __init__(self, _name):
        self.myName = _name

        if self.myName == "Jumpluff":
            #grass flying
            self.myTypes[0] = 2
            self.myTypes[1] = 11

            self.myMoves[0] = Move(73)
            self.myMoves[1] = Move(79)
            self.myMoves[2] = Move(369)
            self.myMoves[3] = Move(512)
