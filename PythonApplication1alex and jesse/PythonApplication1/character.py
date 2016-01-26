class Character:
    def __init__(self,eye1,eye2,eye3,eye4,eye5,eye6, texture):
        self.card = characterCard(eye1,eye2,eye3,eye4,eye5,eye6)
        self.hitPoints = 100
        self.conditionPoints = 15
        self.savePosition = None #Optional for a saving option
        self.texture = texture

class characterCard:
    def __init__(self,attack1,attack2,attack3,attack4,attack5,attack6):
        self.dice1 = attack1
        self.dice2 = attack2
        self.dice3 = attack3
        self.dice4 = attack4
        self.dice5 = attack5
        self.dice6 = attack6

TerryCrews = Character(10, 15, 25, 30, 20, 10, "TerryCrews.png")
JasonStatham = Character(10, 11, 19, 21, 23, 26, "JasonStatham.png")
WesleySniper = Character(30, 14, 14, 20, 18, 14, "WesleySniper.png")
JetRi = Character(10, 30, 12, 25, 10, 23, "JetRi.png")
StevenSeagal = Character(27, 15, 12, 11, 25, 20, "StevenSeagal.png")
SuperMario = Character(10, 10, 30, 30, 15, 15, "SuperMario.png")
JackieChan = Character(20, 25, 5, 25, 20, 15, "JackieChan.png")
ChackNorris = Character(10, 26, 25, 24, 24, 1, "ChackNorris.png")