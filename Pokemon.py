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

while ((player.myTeam[0].myCurrentHealth != 0 and player.myTeam[1].myCurrentHealth != 0 and player.myTeam[2].myCurrentHealth != 0) or (computer.myTeam[0].myCurrentHealth != 0 and computer.myTeam[1].myCurrentHealth != 0 and computer.myTeam[2].myCurrentHealth != 0)):
    print("NEW TURN WOW!!!")
    print("Hit 0 for swapping your goon or 1 to select a move")
    mover = int(input())
    moveModifier = int(input())
    Gamer.ProcessTurn(mover, moveModifier, player, computer, GamerAI, player.myTeam[0], computer.myTeam[0])
