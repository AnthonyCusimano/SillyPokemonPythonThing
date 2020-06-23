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
