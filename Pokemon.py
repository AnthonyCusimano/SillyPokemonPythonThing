# from PokemonInfo import *
from Trainer import *
# import Trainer
from BadAIGen1 import BadAIGen1
# from Moves import Move
from CombatHandler import *

player = Trainer("Jumpluff", "Poliwrath", "Magcargo")

Gamer = CombatHandler()

computer = Trainer("Whimsicott", "Hitmonlee", "Gorebyss")

GamerAI = BadAIGen1(computer)

# gamer
while (player.myTeam[0].myCurrentHealth != 0 and player.myTeam[1].myCurrentHealth != 0 and
       player.myTeam[2].myCurrentHealth != 0) or (computer.myTeam[0].myCurrentHealth != 0 and
                                                  computer.myTeam[1].myCurrentHealth != 0 and
                                                  computer.myTeam[2].myCurrentHealth != 0):
    print("NEW TURN WOW!!!")
    print("Enemy health is ", computer.myTeam[0].myCurrentHealth, " our of ", computer.myTeam[0].myBaseStats[0])
    print("Your health is ", player.myTeam[0].myCurrentHealth, " our of ", player.myTeam[0].myBaseStats[0])
    print("Hit 0 for swapping your goon or 1 to select a move")
    mover = int(input())

    if mover == 0:
        print("1: ", player.myTeam[1].myName, " ", player.myTeam[1].myCurrentHealth, "/",
              player.myTeam[1].myBaseStats[0])
        print("2: ", player.myTeam[2].myName, " ", player.myTeam[2].myCurrentHealth, "/",
              player.myTeam[2].myBaseStats[0])

    elif mover == 1:

        if player.myTeam[0].myItem.myIDNumber == 4 and player.myTeam[0].myChoiceMade:
            moveModifier = player.myTeam[0].myChoiceID

        else:
            print("0: ", player.myTeam[0].myMoves[0].myName)
            print("1: ", player.myTeam[0].myMoves[1].myName)
            print("2: ", player.myTeam[0].myMoves[2].myName)
            print("3: ", player.myTeam[0].myMoves[3].myName)
            
            moveModifier = int(input())

    Gamer.ProcessTurn(mover, moveModifier, player, computer, GamerAI, player.myTeam[0], computer.myTeam[0])

# TODO
print("Battle over I guess : D")
