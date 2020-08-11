from AI import AI
import random


# bad gen 1 AI just picked a random move every turn
# I dunno how switching worked but I'm fairly certain this is accurate
class BadAIGen1(AI):
    pass

    def __init__(self):
        print("bad gen 1 AI created")
        self.movePicked = 0

    def selectMove(self, _pokemon):

        if _pokemon.myItem.myIDNumber == 4 and _pokemon.myChoiceMade:
            return _pokemon.myMoves[_pokemon.myChoiceID]

        self.movePicked = random.randrange(3)
        _pokemon.myMoves[self.movePicked].myName
        return _pokemon.myMoves[self.movePicked]  # self.movePicked

    # test this LOLE
    def swap(self, _myParty):
        for x in _myParty:
            if _myParty[x].myCurrentHealth > 0:
                temp = self.myTeam[0]
                self.myTeam[0] = _myParty[x]
                _myParty[x] = temp
