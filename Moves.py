class Move:

    myName = ""
    myIDNum = 0

    myType = 0
    myDamageType = 0
    myBasePower = 0
    myAccuracy = 0

    def __init__(self, _idNum):
        self.myIDNum = _idNum

        if self.myIDNum == 73:
            self.myName = "Leech Seed"

            self.myType = 3 #grass
            self.myDamageType = 0

            self.myBasePower = 0
            self.myAccuracy = 90

        elif self.myIDNum == 79:
            self.myName = "sleep powder"

            self.myType = 3  # grass
            self.myDamageType = 0 #status

            self.myBasePower = 0
            self.myAccuracy = 75

        elif self.myIDNum == 94:
            self.myName = "Phychic"

            self.myType = 13 #phychic
            self.myDamageType = 2 #special

            self.myBasePower = 90
            self.myAccuracy = 100

        elif self.myIDNum == 369:
            self.myName = "U-turn"

            self.myType = 6  # bug
            self.myDamageType = 1  # physical

            self.myBasePower = 70
            self.myAccuracy = 100

        elif self.myIDNum == 412:
            self.myName = "Energy Ball"

            self.myType = 11 #grass
            self.myDamageType = 2 #special

            self.myBasePower = 90
            self.myAccuracy = 100

        elif self.myIDNum == 512:
            self.myName = "acrobatics"

            self.myType = 1 #flying
            self.myDamageType = 1 #physical

            self.myBasePower = 55
            self.myAccuracy = 100

        elif self.myIDNum == 585:
            self.myName = "Moonblast"

            self.myType = 17 #fairy
            self.myDamageType = 2 #special

            self.myBasePower = 95
            self.myAccuracy = 100
