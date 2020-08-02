

# 
class Item:

    def __init__(self, _name):
        self.myName = _name

        if self.myName == "Red Card":
            self.myIDNumber = 1

    def ProcessMyEndOfTurnEffect(self, _myHolder):
        print("Item end of turn item effect")

    def ProcessMyOnAttackedEffect(self, _attack, _myHolder, _attacker, _attackerTrainer):
        print("Item on attacked effect")
