#from Game import *
import pygame
from Character import *
pygame.mixer.init()

punchsound = pygame.mixer.Sound("sounds/punch.ogg")
punchsound.set_volume(15)
dicesound = pygame.mixer.Sound("sounds/dice.ogg")
mariosound = pygame.mixer.Sound("sounds/mario.ogg")
tilesound = pygame.mixer.Sound("sounds/tileshift.ogg")
tapsound = pygame.mixer.Sound("sounds/tapsound.ogg")
introping = pygame.mixer.Sound("sounds/introping.ogg")
fightsound = pygame.mixer.Sound("sounds/fight.wav")

soundtrack = pygame.mixer.music.load("sounds/soundtrack.wav")
class Sounds:
    def Punch():
        pygame.mixer.Sound.play(punchsound)
    def Dice():
        pygame.mixer.Sound.play(dicesound)
    def Mario():
        pygame.mixer.Sound.play(mariosound)
    def Tile():
        pygame.mixer.Sound.play(tilesound)
    def Tapsound():
        pygame.mixer.Sound.play(tapsound)
    def Introping():
        pygame.mixer.Sound.play(introping)
    def Fightsound():
        pygame.mixer.Sound.play(fightsound)


Charlist = []




def PlayerScreen(Charlist,chooseChars,screenlist, rectlist,crashed, menu_index, screen_index,character_index,last_page,nextplayer):
    #JetRi,SuperMario,ChackNorris,JackieChan,JasonStatham,StevenSeagal,WesleySniper,TerryCrews = Charlist
    start = x, y = 0, 650
    rules = x, y = 225, 650
    exit = x, y = 450, 650
    size = width, height = 750, 780
    gameDisplay = pygame.display.set_mode(size)
    start_corner = [0,10,20,30]
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
            Sounds.Tapsound()
            if event.key == pygame.K_SPACE:
                Sounds.Punch()
            if event.key == pygame.K_RIGHT:
                Sounds.Tapsound()
                menu_index += 1
                if menu_index > 2:
                    menu_index = 0
            if event.key == pygame.K_LEFT:
                Sounds.Tapsound()
                menu_index -= 1
                if menu_index < 0:
                    menu_index = 2
            if menu_index == 2 and event.key == pygame.K_SPACE:
                Sounds.Punch()
                crashed = True
            elif menu_index == 1 and event.key == pygame.K_SPACE:
                Sounds.Punch()
                screen_index = 4
                menu_index = 0
                last_page = 2
            elif menu_index == 0 and event.key == pygame.K_SPACE and len(chooseChars) == 4:
                Sounds.Punch()
                screen_index = 3
 
            if event.key == pygame.K_DOWN:
                Sounds.Tapsound()
                character_index += 1
                if character_index > 7:
                    character_index = 0
            if event.key == pygame.K_UP:
                Sounds.Tapsound()
                character_index -= 1
                if character_index < 0:
                    character_index = 7

            
            
            if len(chooseChars) < 4:

                    if event.key == pygame.K_RETURN and char_button == characterlist[0] and Jet not in Charlist:
                        name = playerNames[nextplayer]
                        corner = start_corner[nextplayer]
                        Sounds.Mario()   
                        JetRi = Player(name,corner,"images/JetRi.png",10,30,12,25,10,23)                   
                        chooseChars.append(JetRi)
                        Charlist.append(Jet)
                        nextplayer += 1
                    elif event.key == pygame.K_RETURN and char_button == characterlist[1] and Mario not in Charlist:
                        name = playerNames[nextplayer]
                        corner = start_corner[nextplayer]
                        Sounds.Mario()
                        SuperMario = Player(name,corner,"images/SuperMario.png",10,10,30,30,15,15)                        
                        chooseChars.append(SuperMario)
                        Charlist.append(Mario)
                        nextplayer += 1
                    elif event.key == pygame.K_RETURN and char_button == characterlist[2] and Chack not in Charlist:
                        name = playerNames[nextplayer]
                        corner = start_corner[nextplayer]
                        Sounds.Mario()
                        ChackNorris = Player(name,corner,"images/ChackNorris.png",10,26,25,24,24,1)
                        chooseChars.append(ChackNorris)
                        Charlist.append(Chack)
                        nextplayer += 1
                    elif event.key == pygame.K_RETURN and char_button == characterlist[3] and Jackie not in Charlist:
                        name = playerNames[nextplayer]
                        corner = start_corner[nextplayer]
                        Sounds.Mario()
                        JackieChan = Player(name,corner,"images/JackieChan.png",20,25,5,25,20,15)
                        chooseChars.append(JackieChan)
                        Charlist.append(Jackie)
                        nextplayer += 1
                    elif event.key == pygame.K_RETURN and char_button == characterlist[4] and Jason not in Charlist:
                        name = playerNames[nextplayer]
                        corner = start_corner[nextplayer]
                        Sounds.Mario()
                        JasonStatham = Player(name,corner,"images/JasonStatham.png",10,11,19,21,23,26)
                        chooseChars.append(JasonStatham)
                        Charlist.append(Jason)
                        nextplayer += 1
                    elif event.key == pygame.K_RETURN and char_button == characterlist[5] and Steven not in Charlist:
                        name = playerNames[nextplayer]
                        corner = start_corner[nextplayer]
                        Sounds.Mario()
                        StevenSeagal = Player(name,corner,"images/StevenSeagal.png",27,15,12,11,25,20)
                        chooseChars.append(StevenSeagal)
                        Charlist.append(Steven)
                        nextplayer += 1
                    elif event.key == pygame.K_RETURN and char_button == characterlist[6] and Wesley not in Charlist:
                        name = playerNames[nextplayer]
                        corner = start_corner[nextplayer]
                        Sounds.Mario()
                        WesleySniper = Player(name,corner,"images/WesleySniper.png",30,14,14,20,18,14)
                        chooseChars.append(WesleySniper)
                        Charlist.append(Wesley)
                        nextplayer += 1
                    elif event.key == pygame.K_RETURN and char_button == characterlist[7] and Terry not in Charlist:
                        name = playerNames[nextplayer]
                        corner = start_corner[nextplayer]
                        Sounds.Mario()
                        TerryCrews = Player(name,corner,"images/TerryCrews.png",10,15,25,30,20,10)
                        chooseChars.append(TerryCrews)
                        Charlist.append(Terry)
                        nextplayer += 1
                  
    
                    
    b = 2


    return screen, rect, crashed, button, menu_index, screen_index, b, char_button, character_index,chooseChars,last_page,Charlist,nextplayer