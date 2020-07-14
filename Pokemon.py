# from PokemonInfo import *
from Trainer import *
# import Trainer
from BadAIGen1 import BadAIGen1
# from Moves import Move
from CombatHandler import *

player = Trainer("Jumpluff", "Poliwrath", "Magcargo")

GamerAI = BadAIGen1()

Gamer = CombatHandler()

computer = Trainer("Whimsicott", "Hitmonlee", "Gorebyss")

print(player.myTeam[0].myBaseStats[5])

# not big on this cus it crashes if you do something stupid
# mover = int(input())

# player.selectMove(mover)
# replace ProcessDamage calls with "Process turn"

# Gamer.ProcessDamage(player.myTeam[0], computer.myTeam[0], player.myTeam[0].myMoves[mover])

# T_SelectedMove = computer.selectMove()

# Gamer.ProcessDamage(computer.myTeam[0], player.myTeam[0], computer.myTeam[0].myMoves[GamerAI.selectMove()])

# TODO
# you can swap to the same pokemon
# you cannot select a different action
while ((player.myTeam[0].myCurrentHealth != 0 and player.myTeam[1].myCurrentHealth != 0 and player.myTeam[2].myCurrentHealth != 0) or (computer.myTeam[0].myCurrentHealth != 0 and computer.myTeam[1].myCurrentHealth != 0 and computer.myTeam[2].myCurrentHealth != 0)):
    print("NEW TURN WOW!!!")
    print("Enemy health is ", computer.myTeam[0].myCurrentHealth, " our of ", computer.myTeam[0].myBaseStats[0])
    print("Your health is ", player.myTeam[0].myCurrentHealth, " our of ", player.myTeam[0].myBaseStats[0])
    print("Hit 0 for swapping your goon or 1 to select a move")
    mover = int(input())

    if mover == 0:
        print("1: ", player.myTeam[1].myName, " ", player.myTeam[1].myCurrentHealth, "/", player.myTeam[1].myBaseStats[0])
        print("2: ", player.myTeam[2].myName, " ",player.myTeam[2].myCurrentHealth, "/", player.myTeam[2].myBaseStats[0])

    moveModifier = int(input())
    Gamer.ProcessTurn(mover, moveModifier, player, computer, GamerAI, player.myTeam[0], computer.myTeam[0])
