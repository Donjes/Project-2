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
