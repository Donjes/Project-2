class Character:
    def __init__(self,eye1,eye2,eye3,eye4,eye5,eye6):
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

TerryCrews = Character(10, 15, 25, 30, 20, 10)
JasonStatham = Character(10, 11, 19, 21, 23, 26)
WesleySniper = Character(30, 14, 14, 20, 18, 14)
JetRi = Character(10, 30, 12, 25, 10, 23)
StevenSeagal = Character(27, 15, 12, 11, 25, 20)
SuperMario = Character(10, 10, 30, 30, 15, 15)
VinDieser = Character(20, 25, 5, 25, 20, 15)
ChackNorris = Character(10, 26, 25, 24, 24, 1)