from AI import AI
import random


# bad gen 1 AI just picked a random move every turn
# I dunno how switching worked but I'm fairly certain this is accurate
# http://wiki.pokemonspeedruns.com/index.php/Pok%C3%A9mon_Red/Blue/Yellow_Trainer_AI
class BadAIGen1(AI):
    pass

    # self.myTrainer = _myTrainer
    def __init__(self, _myTrainer):
        print("bad gen 1 AI created")
        self.movePicked = 0
        self.myTrainer = _myTrainer

    # pick a random move unless we have an active choice item
    def selectMove(self, _pokemon):

        # choice item check
        if _pokemon.myItem.myIDNumber == 4 and _pokemon.myChoiceMade:
            return _pokemon.myMoves[_pokemon.myChoiceID]

        self.movePicked = random.randrange(3)
        _pokemon.myMoves[self.movePicked].myName
        return _pokemon.myMoves[self.movePicked]  # self.movePicked

    # test this LOLE
    def swap(self, _myParty):
        # for x in _myParty:
        for x in range(4):
            if self.myTrainer.myTeam[x].myBaseStats[0] > 0:
                temp = self.myTrainer.myTeam[0]
                self.myTrainer.myTeam[0] = _myParty[x]
                _myParty[x] = temp
