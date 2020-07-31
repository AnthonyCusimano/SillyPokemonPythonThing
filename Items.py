
class Item:

    def __init__(self, _name):
        self.myName = _name
        self.myIDNumber = 0

    def ProcessMyEndOfTurnEffect(self, _myHolder):
        print("Item end of turn item effect")

    def ProcessMyOnAttackedEffect(self, _attack, _myHolder):
        print("Item on attacked effect")
