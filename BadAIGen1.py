from AI import AI
import random


class BadAIGen1(AI):
    pass

    def __init__(self):
        print("bad gen 1 AI created")
        self.movePicked = 0

    def selectMove(self):
        self.movePicked = random.randrange(3)
        return self.movePicked

    #test this LOLE
    def swap(self, _myParty):
        for x in _myParty:
            if _myParty[x].myCurrentHealth > 0:
                temp = self.myTeam[0]
                self.myTeam[0] = _myParty[x]
                _myParty[x] = temp
