import pygame
name = None

class Player:
    def __init__(self,name,texture,attack1,attack2,attack3,attack4,attack5,attack6):
        self.playername = name

        self.texture = texture
        self.hitPoints = 100 #  change the hitpoints and conditionpoints !!!
        self.conditionPoints = 15
        self.savePosition = None #Optional for a saving option
        self.dice1 = attack1
        self.dice2 = attack2
        self.dice3 = attack3
        self.dice4 = attack4
        self.dice5 = attack5
        self.dice6 = attack6

TerryCrews = Player(name,"images/TerryCrews.png",10,15,25,30,20,10)
JasonStatham = Player(name,"images/JasonStatham.png",10,11,19,21,23,26)
WesleySniper = Player(name,"images/WesleySniper.png",30,14,14,20,18,14)
JetRi = Player(name,"images/JetRi.png",10,30,12,25,10,23)
StevenSeagal = Player(name,"images/StevenSeagal.png",27,15,12,11,25,20)
SuperMario = Player(name,"images/SuperMario.png",10,10,30,30,15,15)
JackieChan = Player(name,"images/JackieChan.png",20,25,5,25,20,15)
ChackNorris = Player(name,"images/ChackNorris.png",10,26,25,24,24,1)
