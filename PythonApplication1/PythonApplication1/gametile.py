class Tile_interaction:
    def __init__(self,tnr,action):
        self.tileNum = tnr
        self.Action = action
#  ALL POSSIBLE VALUES FOR THE "fightnumber" in class FightingTile
# 0 = CornerFight
# 1 = SpotFight
# 2 = SuperFight

class FightingTile:
    def __init__(self,tile,fightnumber,tnr,action):
        self.tile = Tile_interaction(tnr,action)
        self.fightingNumber = fightnumber
