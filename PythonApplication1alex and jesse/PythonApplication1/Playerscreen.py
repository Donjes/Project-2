#from Game import *
import pygame
from Character import *
pygame.init()

punchsound = pygame.mixer.Sound("sounds/punch.ogg")
dicesound = pygame.mixer.Sound("sounds/dice.ogg")
mariosound = pygame.mixer.Sound("sounds/mario.ogg")
tilesound = pygame.mixer.Sound("sounds/tileshift.ogg")

class Sounds:
    def Punch():
        pygame.mixer.Sound.play(punchsound)
    def Dice():
        pygame.mixer.Sound.play(dicesound)
    def Mario():
        pygame.mixer.Sound.play(mariosound)
    def Tile():
        pygame.mixer.Sound.play(tilesound)

Charlist = [JetRi,SuperMario,ChackNorris,JackieChan,JasonStatham,StevenSeagal,WesleySniper,TerryCrews]




def PlayerScreen(Charlist,chooseChars,screenlist, rectlist,crashed, menu_index, screen_index,character_index,last_page):
    JetRi,SuperMario,ChackNorris,JackieChan,JasonStatham,StevenSeagal,WesleySniper,TerryCrews = Charlist
    start = x, y = 0, 650
    rules = x, y = 225, 650
    exit = x, y = 450, 650
    size = width, height = 750, 780
    gameDisplay = pygame.display.set_mode(size)

    Jet = x,y = 450, 145
    Mario = x,y = 450, 235
    Chack = x,y = 450, 325
    Jackie = x,y = 450, 415
    Jason = x,y = 560, 145
    Steven = x,y = 560, 235
    Wesley = x,y = 560, 325
    Terry = x,y = 560, 415
    characterlist = [ Jet, Mario, Chack,  Jackie,  Jason, Steven, Wesley, Terry]
    playerNames = ['P1','P2','P3','P4']
    char_button = characterlist[character_index]
    menulist = [start, rules, exit] #lijst van de buttons
    button = menulist[menu_index]
    rect = rectlist[screen_index]
    screen = screenlist[screen_index]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True                  #programma sluit af met rode X
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Sounds.Punch()
            if event.key == pygame.K_RIGHT:
                menu_index += 1
                if menu_index > 2:
                    menu_index = 0
            if event.key == pygame.K_LEFT:
                menu_index -= 1
                if menu_index < 0:
                    menu_index = 2
            if menu_index == 2 and event.key == pygame.K_SPACE:
                crashed = True
            elif menu_index == 1 and event.key == pygame.K_SPACE:
                screen_index = 4
                menu_index = 0
                last_page = 2
            elif menu_index == 0 and event.key == pygame.K_SPACE and len(chooseChars) == 4:
                screen_index = 3
 
            if event.key == pygame.K_DOWN:
                character_index += 1
                if character_index > 7:
                    character_index = 0
            if event.key == pygame.K_UP:
                character_index -= 1
                if character_index < 0:
                    character_index = 7



            if len(chooseChars) < 4:
                for i in range(0,4):
                    if event.key == pygame.K_RETURN:
                        if char_button == characterlist[0] and JetRi not in chooseChars:
                            name = playerNames[i]
                            Sounds.Mario()   
                            JetRi = Player(name,"images/JetRi.png",10,30,12,25,10,23)                   
                            chooseChars.append(JetRi)
    
                        elif char_button == characterlist[1] and SuperMario not in chooseChars:
                                name = playerNames[i]
                                Sounds.Mario()
                                SuperMario = Player(name,"images/SuperMario.png",10,10,30,30,15,15)                        
                                chooseChars.append(SuperMario)
 
                        elif char_button == characterlist[2] and ChackNorris not in chooseChars:
                            name = playerNames[i]
                            Sounds.Mario()
                            ChackNorris = Player(name,"images/ChackNorris.png",10,26,25,24,24,1)
                            chooseChars.append(ChackNorris)

                        elif char_button == characterlist[3] and JackieChan not in chooseChars:
                            name = playerNames[i]
                            Sounds.Mario()
                            JackieChan = Player(name,"images/JackieChan.png",20,25,5,25,20,15)
                            chooseChars.append(JackieChan)

                        elif char_button == characterlist[4] and JasonStatham not in chooseChars:
                            name = playerNames[i]
                            Sounds.Mario()
                            JasonStatham = Player(name,"images/JasonStatham.png",10,11,19,21,23,26)
                            chooseChars.append(JasonStatham)

                        elif char_button == characterlist[5] and StevenSeagal not in chooseChars:
                            name = playerNames[i]
                            Sounds.Mario()
                            JasonStatham = Player(name,"images/JasonStatham.png",10,11,19,21,23,26)
                            chooseChars.append(StevenSeagal)

                        elif char_button == characterlist[6] and WesleySniper not in chooseChars:
                            name = playerNames[i]
                            Sounds.Mario()
                            WesleySniper = Player(name,"images/WesleySniper.png",30,14,14,20,18,14)
                            chooseChars.append(WesleySniper)

                        elif event.key == pygame.K_RETURN and char_button == characterlist[7] and TerryCrews not in chooseChars:
                            name = playerNames[i]
                            Sounds.Mario()
                            TerryCrews = Player(name,"images/TerryCrews.png",10,15,25,30,20,10)
                            chooseChars.append(TerryCrews)

    

    b = 2


    return screen, rect, crashed, button, menu_index, screen_index, b, char_button, character_index,chooseChars,last_page,Charlist