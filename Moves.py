class Move:

    def __init__(self, _idnum):
        self.myIDNum = _idnum

        if self.myIDNum == 56:
            self.myName = "Hydropump"

            self.myType = 10  # water
            self.myDamageType = 2  # special

            self.myBasePower = 110
            self.myAccuracy = 80

        elif self.myIDNum == 58:
            self.myName = "Ice Beam"

            self.myType = 14  # ice
            self.myDamageType = 2  # special

            self.myBasePower = 90
            self.myAccuracy = 100

        elif self.myIDNum == 73:
            self.myName = "Leech Seed"

            self.myType = 3  # grass
            self.myDamageType = 0

            self.myBasePower = 0
            self.myAccuracy = 90

        elif self.myIDNum == 79:
            self.myName = "sleep powder"

            self.myType = 3  # grass
            self.myDamageType = 0  # status

            self.myBasePower = 0
            self.myAccuracy = 75

        elif self.myIDNum == 94:
            self.myName = "Psychic"

            self.myType = 13  # Psychic
            self.myDamageType = 2  # special

            self.myBasePower = 90
            self.myAccuracy = 100

        elif self.myIDNum == 95:
            self.myName = "Hypnosis"

            self.myType = 13  # Psychic
            self.myDamageType = 0  # status

            self.myBasePower = 0
            self.myAccuracy = 60

        elif self.myIDNum == 153:
            self.myName = "Explosion"

            self.myType = 0  # normal
            self.myDamageType = 1  # physical

            self.myBasePower = 250
            self.myAccuracy = 100

        elif self.myIDNum == 164:
            self.myName = "Substitute"

            self.myType = 0  # normal
            self.myDamageType = 0  # status

            self.myBasePower = 0
            self.myAccuracy = 100

        elif self.myIDNum == 174:
            self.myName = "Curse"

            self.myType = 7  # ghost
            self.myDamageType = 0  # status

            self.myBasePower = 0
            self.myAccuracy = 100

        elif self.myIDNum == 182:
            self.myName = "Protect"

            self.myType = 0  # normal
            self.myDamageType = 0  # status

            self.myBasePower = 0
            self.myAccuracy = 100

        elif self.myIDNum == 281:
            self.myName = "Yawn"

            self.myType = 0  # normal
            self.myDamageType = 0  # status

            self.myBasePower = 0
            self.myAccuracy = 100

        elif self.myIDNum == 282:
            self.myName = "Knock Off"

            self.myType = 16  # dark
            self.myDamageType = 1  # physical

            self.myBasePower = 65
            self.myAccuracy = 100

        elif self.myIDNum == 369:
            self.myName = "U-turn"

            self.myType = 6  # bug
            self.myDamageType = 1  # physical

            self.myBasePower = 70
            self.myAccuracy = 100

        elif self.myIDNum == 370:
            self.myName = "Close Combat"

            self.myType = 1  # fighting
            self.myDamageType = 1  # physical

            self.myBasePower = 120
            self.myAccuracy = 100

        elif self.myIDNum == 412:
            self.myName = "Energy Ball"

            self.myType = 11  # grass
            self.myDamageType = 2  # special

            self.myBasePower = 90
            self.myAccuracy = 100

        elif self.myIDNum == 436:
            self.myName = "Lava Plume"

            self.myType = 9  # fire
            self.myDamageType = 2  # special

            self.myBasePower = 80
            self.myAccuracy = 100

        elif self.myIDNum == 444:
            self.myName = "Stone Edge"

            self.myType = 5  # rock
            self.myDamageType = 1  # physical

            self.myBasePower = 100
            self.myAccuracy = 80

        elif self.myIDNum == 446:
            self.myName = "Stealth Rock"

            self.myType = 5  # rock
            self.myDamageType = 0  # status

            self.myBasePower = 0
            self.myAccuracy = 100

        elif self.myIDNum == 503:
            self.myName = "Scald"

            self.myType = 10  # water
            self.myDamageType = 2  # special

            self.myBasePower = 80
            self.myAccuracy = 100

        elif self.myIDNum == 504:
            self.myName = "Shell Smash"

            self.myType = 0  # normal
            self.myDamageType = 0  # status

            self.myBasePower = 0
            self.myAccuracy = 100

        elif self.myIDNum == 509:
            self.myName = "Circle Throw"

            self.myType = 1  # fighting
            self.myDamageType = 1  # physical

            self.myBasePower = 60
            self.myAccuracy = 90

        elif self.myIDNum == 512:
            self.myName = "acrobatics"

            self.myType = 2  # flying
            self.myDamageType = 1  # physical

            self.myBasePower = 55
            self.myAccuracy = 100

        elif self.myIDNum == 585:
            self.myName = "Moonblast"

            self.myType = 17  # fairy
            self.myDamageType = 2  # special

            self.myBasePower = 95
            self.myAccuracy = 100
