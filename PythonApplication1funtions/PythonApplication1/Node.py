class Node:
  def __init__(self, value, tail):
    self.Tail = tail
    self.Value = value
    self.IsEmpty = False



class Empty: 
  def __init__(self):
    self.IsEmpty = True

Empty = Empty()

class Character:
    def __init__(self,card,eye1,eye2,eye3,eye4,eye5,eye6):
        self.card = characterCard(eye1,eye2,eye3,eye4,eye5,eye6)
        self.hitPoints = 100
        self.conditionPoints = 15 
        self.SavePosition = None #Optional for a saving option

class characterCard:
    def __init__(self,attack1,attack2,attack3,attack4,attack5,attack6):
        self.Dice1 = attack1
        self.Dice2 = attack2
        self.Dice3 = attack3
        self.Dice4 = attack4
        self.Dice5 = attack5
        self.Dice6 = attack6

class Tile_interaction:
    def __init__(self,tnr,action):
        self.tileNum = tnr
        self.Action = action
#  ALL POSSIBLE VALUES FOR THE "fightnumber" in class FightingTile
0 = CornerFight 
1 = SpotFight
2 = SuperFight



class FightingTile:
    def __init__(self,tile,fightnumber,tnr,action):
        self.tile = Tile_interaction(tnr,action)
        self.fightingNumber = fightnumber
