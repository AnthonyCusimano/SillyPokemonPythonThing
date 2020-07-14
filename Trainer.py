from PokemonInfo import *
# from AI import


class Trainer:

    def __init__(self):
        self.myTeam = Pokemon[0, 0, 0, 0, 0, 0]

    # send Pokemon objects please
    def __init__(self, _guy1, _guy2, _guy3):
        self.myTeam = [Pokemon(_guy1), Pokemon(_guy2), Pokemon(_guy3), 0, 0, 0]

    def swap(self, _newGuyAddress):
        if self.myTeam[_newGuyAddress].myCurrentHealth > 0:
            temp = self.myTeam[0]
            self.myTeam[0] = self.myTeam[_newGuyAddress]
            self.myTeam[_newGuyAddress] = temp

    def selectMove(self, _moveID):
        if _moveID == '1' or _moveID == 2 or _moveID == 3 or _moveID == 4:
            print(self.myTeam[0].myMoves[_moveID].myName, "selected")
            return self.myTeam[0].myMoves[_moveID]

