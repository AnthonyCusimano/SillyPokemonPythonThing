from AI import AI
import random


# http://wiki.pokemonspeedruns.com/index.php/Pok%C3%A9mon_Red/Blue/Yellow_Trainer_AI
class GoodAIGen1(AI):
    pass

    # self.myTrainer = _trainer
    # self.movePicked = 0
    def __init__(self, _trainer):
        self.movePicked = 0
        self.myTrainer = _trainer

    # currently no action taken
    def selectMove(self, _pokemon):
        print("")

    # test this LOLE
    # currently no action taken
    def swap(self, _myParty):
        print("")
