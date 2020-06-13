# from PokemonInfo import *
from Trainer import *
# from Moves import Move
from CombatHandler import *

player = Trainer("Jumpluff", "Poliwrath", "Magcargo")

Gamer = CombatHandler()

computer = Trainer("Whimsicott", "Hitmonlee", "Gorebyss")

# not big on this cus it crashes if you do something stupid
mover = int(input())

player.selectMove(mover)

Gamer.ProcessDamage(player.myTeam[0], computer.myTeam[0], player.myTeam[0].myMoves[mover])

