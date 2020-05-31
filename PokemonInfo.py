class Pokemon:
    myName = ''
    myIDNum = 0

    myTypes = [0, 0]
    myMoves = [0, 0, 0, 0]

    myBaseStats = [0, 0, 0, 0, 0, 0,]

    def __init__(self, _name):
        self.myName = _name

        if self.myName == "Jumpluff":
            #grass flying
            self.myTypes[0] = 2
            self.myTypes[1] = 11
