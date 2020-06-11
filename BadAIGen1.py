import AI
import random


class BadAIGen1(AI):
    pass

    def __init__(self):
        print("bad gen 1 AI created")

    def selectMove(self):
        movePicked = random.randrange(3)
        print(movePicked)
