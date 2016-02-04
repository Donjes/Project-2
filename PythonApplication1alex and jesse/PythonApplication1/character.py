import pygame
name = None
corner = None
class Player:
    def __init__(self,name,corner,texture,attack1,attack2,attack3,attack4,attack5,attack6):
        self.playerName = name
        self.texture = texture
        self.hitPoints = 1 #  change the hitpoints and conditionpoints !!!
        self.conditionPoints = 15
        self.savePosition = None #Optional for a saving option
        self.dice1 = attack1 
        self.dice2 = attack2 
        self.dice3 = attack3 
        self.dice4 = attack4 
        self.dice5 = attack5 
        self.dice6 = attack6 
        self.alive = True
        self.startCorner = corner
    def getDamage(self,dmgdone):
        self.hitPoints = self.hitPoints - dmgdone
    def doDamage(self,conditionLost):
        self.conditionPoints = self.conditionPoints - conditionLost

TerryCrews = Player(name,corner,"images/TerryCrews.png",10,15,25,30,20,10)
JasonStatham = Player(name,corner,"images/JasonStatham.png",10,11,19,21,23,26)
WesleySniper = Player(name,corner,"images/WesleySniper.png",30,14,14,20,18,14)
JetRi = Player(name,corner,"images/JetRi.png",10,30,12,25,10,23)
StevenSeagal = Player(name,corner,"images/StevenSeagal.png",27,15,12,11,25,20)
SuperMario = Player(name,corner,"images/SuperMario.png",10,10,30,30,15,15)
JackieChan = Player(name,corner,"images/JackieChan.png",20,25,5,25,20,15)
ChackNorris = Player(name,corner,"images/ChackNorris.png",10,26,25,24,24,1)
