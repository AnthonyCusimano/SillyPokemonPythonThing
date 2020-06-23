# from PokemonInfo import *
from Trainer import *
#import Trainer
from BadAIGen1 import BadAIGen1
# from Moves import Move
from CombatHandler import *

player = Trainer("Jumpluff", "Poliwrath", "Magcargo")

GamerAI = BadAIGen1()

Gamer = CombatHandler()

computer = Trainer("Whimsicott", "Hitmonlee", "Gorebyss")

print(player.myTeam[0].myBaseStats[5])

# not big on this cus it crashes if you do something stupid
mover = int(input())

player.selectMove(mover)

Gamer.ProcessDamage(player.myTeam[0], computer.myTeam[0], player.myTeam[0].myMoves[mover])

# T_SelectedMove = computer.selectMove()

Gamer.ProcessDamage(computer.myTeam[0], player.myTeam[0], computer.myTeam[0].myMoves[GamerAI.selectMove()])
