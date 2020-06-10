from PokemonInfo import *
# GITHUB


class Trainer:

    def __init__(self):
        self.myTeam = [0, 0, 0, 0, 0, 0]

    # send Pokemon objects please
    def __init__(self, _guy1, _guy2, _guy3):
        self.myTeam = [Pokemon(_guy1), Pokemon(_guy2), Pokemon(_guy3), 0, 0, 0]

    def swap(self, _newGuyAddress):
        temp = self.myTeam[0]
        self.myTeam[0] = self.myTeam[_newGuyAddress]
        self.myTeam[_newGuyAddress] = temp
