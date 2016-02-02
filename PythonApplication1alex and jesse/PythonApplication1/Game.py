import pygame
import time
from Playerscreen import *
from Options import *
from Gameboard import *
from SaveGame import *
pygame.init()



size = width, height = 650, 650
tile = 0
white = (255, 255, 255)
black = (0, 0, 0)
chooseChars = []
firstround = True
save_game = False
load_old_game = False
last_page = 0
letsSuperFight = 0
letsFight = 0
nextturn = 0
p = 0
roller1 = False
roller2 = False
roller_reset = False
roller1_img = "DiceRolling.png" 
roller2_img = "DiceRolling.png"
tempTile = 0
newLocation = False
dice_rolled = False
#playerList = [player1,player2,player3,player4]
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Survivor')
clock = pygame.time.Clock()

startup_screen = pygame.image.load("images/startscherm2.png")
rules_screen = pygame.image.load("images/rules.png")
character_screen = pygame.image.load("images/playermenu.png")
big_glove = pygame.image.load("images/handschoen.png")
red_glove = pygame.image.load("images/red_handschoen.png")
green_glove = pygame.image.load("images/green_handschoen.png")
yellow_glove = pygame.image.load("images/yellow_handschoen.png")
blue_glove = pygame.image.load("images/blue_handschoen.png")
board_screen = pygame.image.load("images/speelveld.png")
options_screen = pygame.image.load("images/Options.png")
winning_screen = pygame.image.load("images/winningscreen.png")
# imgTerry = pygame.image.load("images/TerryCrews.png")
# imgJason = pygame.image.load("images/JasonStatham.png")
# imgWesley = pygame.image.load("images/WesleySniper.png")
# imgJet = pygame.image.load("images/JetRi.png")
# imgSteven = pygame.image.load("images/StevenSeagal.png")
# imgMario = pygame.image.load("images/SuperMario.png")
# imgJackie = pygame.image.load("images/JackieChan.png")
# imgChack = pygame.image.load("images/ChackNorris.png")

options_screen_rect = options_screen.get_rect()
board_screen_rect = board_screen.get_rect()
startup_screen_rect = startup_screen.get_rect()                 #start at top left
rules_screen_rect = startup_screen.get_rect()
character_screen_rect = character_screen.get_rect()
winning_screen_rect = winning_screen.get_rect()

screenlist = [startup_screen, rules_screen, character_screen, board_screen, options_screen]
screen_index = 0

s_rect = startup_screen_rect
r_rect = rules_screen_rect
p_rect = character_screen_rect
b_rect = board_screen_rect
o_rect = options_screen_rect
rectlist = [s_rect, r_rect, p_rect,b_rect,o_rect]

remove = x, y = -100, - 100
start = x, y = 70, 150 #coordinates glove --> start
rules = x, y = 70, 250 #coordinates glove --> rules
exit = x, y = 350, 520 #coordinates glove --> exit
#navi = (-100,-100) #1Ruben speler kleine handschoen word buiten beeld neer gezet
character_index = 0
crashed = False

menu_index = 0                           #startwaarde = start
pics = []

v1 = (100, 85)
v2 = (100, 215)
v3 = (100, 345)
v4 = (100, 475)
vectorlist = [v1, v2, v3, v4]

font = pygame.font.SysFont(None, 50)

#koffie logo bij het opstarten van het spel
#def Koffielogo():
#    size = width, height = 650, 650
#    gameDisplay = pygame.display.set_mode(size)
    
#    for i in range (9):
#        gameDisplay.blit(pygame.image.load("Koffielogo/Koffie"+ str(i) +".png"),(pygame.image.load("Koffielogo/Koffie"+ str(i) +".png").get_rect()))  
#        pygame.display.update()
#        if i == 0:
#            time.sleep(1)
#        elif i == 6:
#            Sounds.Introping()
#        time.sleep(0.08)
#    time.sleep(2)
    
#Koffielogo()

def text_pop(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [225, 275])

def winning_pic(texture):
    gameDisplay.blit(texture(350, 325))

def glove_update(button, screen_index):                   #geeft handschoen.png weer
    if screen_index == 0:           #standard vector
        gameDisplay.blit(big_glove,(button))
    elif screen_index == 2:
        gameDisplay.blit(big_glove,(button))
    elif screen_index == 4:
        gameDisplay.blit(big_glove,(button))



def character_glove(char_button):
    gameDisplay.blit(red_glove,(char_button))

def screen_update(screen,rect):
    gameDisplay.blit(screen,(rect))


def StartScreen(screenlist, rectlist, screen_index, menu_index, crashed,last_page):

    start = x, y = 70, 150 #coordinates glove --> start
    rules = x, y = 70, 250 #coordinates glove --> rules
    exit = x, y = 350, 520 #coordinates glove --> exit
    menulist = [start, rules, exit] #lijst van de buttons
    rect = rectlist[screen_index]
    screen = screenlist[screen_index]
    button = menulist[menu_index]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True                  #programma sluit af met rode X

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Sounds.Punch()
        if screen_index == 0:      #start
            screen = screenlist[screen_index]
            rect = rectlist[screen_index]
            if event.type == pygame.KEYDOWN:    #als er een key wordt ingedrukt
                if event.key == pygame.K_DOWN:  #key = down arrow
                    menu_index += 1                      #index + 1
                    if menu_index > 2:
                        menu_index = 0                   #na exit button = start

                if event.key == pygame.K_UP:    #key = up arrow
                    menu_index -= 1                      #index - 1
                    if menu_index < 0:
                        menu_index = 2                   #na start button = exit
                
                if menu_index == 2 and event.key == pygame.K_SPACE:
                    Sounds.Punch()
                    crashed = True
                elif menu_index == 1 and event.key == pygame.K_SPACE:
                    Sounds.Punch()
                    screen_index = 4
                    menu_index = 0
                    last_page = 0
                elif menu_index == 0 and event.key == pygame.K_SPACE:
                    Sounds.Punch()
                    screen_index = 2
    b = 0
    return screen, rect, button, screen_index, menu_index, crashed, b,last_page


pygame.mixer.music.play(-1)
while not crashed:
    


    if screen_index == 0:#start
        size = width, height = 650, 650
        gameDisplay = pygame.display.set_mode(size)
        screen, rect, button, screen_index, menu_index, crashed, b,last_page = \
        StartScreen(screenlist, rectlist, screen_index, menu_index, crashed,last_page)
        screen_update(screen, rect)
        glove_update(button, screen_index)                         #hier word button meegegeven aan glove_update

    elif screen_index == 1:#rules
        size = width, height = 650, 650
        gameDisplay = pygame.display.set_mode(size)
        screen, rect,screen_index, menu_index, crashed = \
        RulesScreen(screenlist, rectlist, screen_index, menu_index, crashed, b)
        screen_update(screen, rect)
        glove_update(button, screen_index)

    elif screen_index == 4:

        screen, rect, crashed, button, menu_index, screen_index, b,save_game,load_old_game,last_page = \
        Options(screenlist, rectlist,crashed, menu_index, screen_index,character_index,b,save_game,load_old_game,last_page)
        screen_update(screen, rect)
        glove_update(button, screen_index)

    elif screen_index == 2:#character

        screen, rect ,crashed, button, menu_index, screen_index, b, char_button,character_index,chooseChars,last_page,Charlist = \
        PlayerScreen(Charlist,chooseChars,screenlist, rectlist, crashed, menu_index, screen_index,character_index,last_page)
        screen_update(screen, rect)
        glove_update(button, screen_index)
        character_glove(char_button)
        if len(chooseChars) > 0:
            small_glove(chooseChars[0].texture,(100,85))
        if len(chooseChars) > 1:
            small_glove(chooseChars[1].texture,(100,195))
        if len(chooseChars) > 2:
            small_glove(chooseChars[2].texture,(100,310))
        if len(chooseChars) > 3:
            small_glove(chooseChars[3].texture,(100,435))




    elif screen_index == 3:
#normale functie
        tempChar = chooseChars[p%4-1]
        if letsSuperFight == 0 and letsFight == 0:
            firstround,chooseChars,roll,p,screenlist, rectlist, crashed, menu_index, screen_index,last_page,letsSuperFight,letsFight,nextturn,tempTile,newLocation,dice_rolled = \
            BoardScreen(firstround,chooseChars,roll, p,screenlist, rectlist, crashed, menu_index, screen_index,last_page,letsSuperFight,letsFight,nextturn,tempTile,newLocation,dice_rolled)
            size = width, height = 650, 746
            gameDisplay = pygame.display.set_mode(size)

#fight functions      
        if letsSuperFight == 1:            
            roller1,roller2,roller_reset,roller1_img,roller2_img = superFight(tempChar,chooseChars,roller1,roller2,roller_reset,roller1_img,roller2_img)
            gameDisplay.blit(pygame.image.load("images/speelveld.png"),(pygame.image.load("images/speelveld.png").get_rect()))     
            cnt = 0
            for i in chooseChars:
                if chooseChars[cnt].savePosition%40 == chooseChars[p%4].savePosition%40 and cnt is not p%4:
                    if chooseChars[0].savePosition%40 == chooseChars[1].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveRB),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[0].savePosition%40 == chooseChars[2].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveGrB),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[0].savePosition%40 == chooseChars[3].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveBG),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[1].savePosition%40 == chooseChars[2].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveGrR),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[1].savePosition%40 == chooseChars[3].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveRG),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[2].savePosition%40 == chooseChars[3].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveGrG),navigate[chooseChars[p%4].savePosition%40])
             
                else:
                    gameDisplay.blit(pygame.image.load(gloveSmall[cnt]),navigate[chooseChars[cnt].savePosition%40])  
                cnt += 1  
                
            small_glove(chooseChars[p%4].texture,(290,230))
            small_glove(chooseChars[0].texture,(110,110))
            small_glove(chooseChars[1].texture,(470,110))
            small_glove(chooseChars[2].texture,(470,470))
            small_glove(chooseChars[3].texture,(110,470))  
            gameDisplay.blit(pygame.image.load("images/fight.png"),(-5,170))
            gameDisplay.blit(pygame.image.load(tempChar.texture),(30,180))
            gameDisplay.blit(pygame.image.load("images/"+ roller1_img),(30,250)) 
            gameDisplay.blit(pygame.image.load("images/"+ roller2_img),(170,250))             
            pygame.display.update()
            if roller_reset == True:
                time.sleep(2)
                roller1 = False
                roller2 = False
                roller_reset = False      
                letsSuperFight = 0 
                         
        elif letsFight == 1:
            tempChar = chooseChars[p%4-1]
            roller1,roller2,roller_reset,roller1_img,roller2_img = fight(tempChar,chooseChars,roller1,roller2,roller_reset,roller1_img,roller2_img)
            gameDisplay.blit(pygame.image.load("images/speelveld.png"),(pygame.image.load("images/speelveld.png").get_rect()))
            cnt = 0
            for i in chooseChars:
                if chooseChars[cnt].savePosition%40 == chooseChars[p%4].savePosition%40 and cnt is not p%4:
                    if chooseChars[0].savePosition%40 == chooseChars[1].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveRB),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[0].savePosition%40 == chooseChars[2].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveGrB),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[0].savePosition%40 == chooseChars[3].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveBG),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[1].savePosition%40 == chooseChars[2].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveGrR),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[1].savePosition%40 == chooseChars[3].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveRG),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[2].savePosition%40 == chooseChars[3].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveGrG),navigate[chooseChars[p%4].savePosition%40])
             
                else:
                    gameDisplay.blit(pygame.image.load(gloveSmall[cnt]),navigate[chooseChars[cnt].savePosition%40])  
                cnt += 1    
               
            small_glove(chooseChars[p%4].texture,(290,230))
            small_glove(chooseChars[0].texture,(110,110))
            small_glove(chooseChars[1].texture,(470,110))
            small_glove(chooseChars[2].texture,(470,470))
            small_glove(chooseChars[3].texture,(110,470))  
            gameDisplay.blit(pygame.image.load("images/fight.png"),(-5,170))
            gameDisplay.blit(pygame.image.load(tempChar.texture),(30,180))
            gameDisplay.blit(pygame.image.load("images/"+ roller1_img),(30,250)) 
            gameDisplay.blit(pygame.image.load("images/"+ roller2_img),(170,250))  
            pygame.display.update()
            if roller_reset == True:  
                time.sleep(2) 
                roller1 = False
                roller2 = False
                roller_reset = False    
                letsFight = 0   
#bij normale functie 
        elif nextturn == 1:
            gameDisplay.blit(pygame.image.load("images/speelveld.png"),(pygame.image.load("images/speelveld.png").get_rect()))     
            cnt = 0
            for i in chooseChars:
                if chooseChars[cnt].savePosition%40 == chooseChars[p%4].savePosition%40 and cnt is not p%4:
                    if chooseChars[0].savePosition%40 == chooseChars[1].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveRB),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[0].savePosition%40 == chooseChars[2].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveGrB),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[0].savePosition%40 == chooseChars[3].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveBG),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[1].savePosition%40 == chooseChars[2].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveGrR),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[1].savePosition%40 == chooseChars[3].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveRG),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[2].savePosition%40 == chooseChars[3].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveGrG),navigate[chooseChars[p%4].savePosition%40])
             
                else:
                    gameDisplay.blit(pygame.image.load(gloveSmall[cnt]),navigate[chooseChars[cnt].savePosition%40])  
                cnt += 1  
                
            small_glove(chooseChars[p%4].texture,(290,230))
            small_glove(chooseChars[0].texture,(110,110))
            small_glove(chooseChars[1].texture,(470,110))
            small_glove(chooseChars[2].texture,(470,470))
            small_glove(chooseChars[3].texture,(110,470))    
            gameDisplay.blit(pygame.image.load("images/nextturn.png"),(88,225))
            small_glove(chooseChars[p%4].texture,(150,250))
            pygame.display.update()
            time.sleep(0.1)#1 doen
            gameDisplay.blit(pygame.image.load("images/speelveld.png"),(pygame.image.load("images/speelveld.png").get_rect()))
            cnt = 0
            for i in chooseChars:
                if chooseChars[cnt].savePosition%40 == chooseChars[p%4].savePosition%40 and cnt is not p%4:
                    if chooseChars[0].savePosition%40 == chooseChars[1].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveRB),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[0].savePosition%40 == chooseChars[2].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveGrB),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[0].savePosition%40 == chooseChars[3].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveBG),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[1].savePosition%40 == chooseChars[2].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveGrR),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[1].savePosition%40 == chooseChars[3].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveRG),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[2].savePosition%40 == chooseChars[3].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveGrG),navigate[chooseChars[p%4].savePosition%40])
             
                else:
                    gameDisplay.blit(pygame.image.load(gloveSmall[cnt]),navigate[chooseChars[cnt].savePosition%40])  
                cnt += 1  
                
            small_glove(chooseChars[p%4].texture,(290,230))
            small_glove(chooseChars[0].texture,(110,110))
            small_glove(chooseChars[1].texture,(470,110))
            small_glove(chooseChars[2].texture,(470,470))
            small_glove(chooseChars[3].texture,(110,470))
            dice_img(roll)          
            nextturn = 0
        else:
            gameDisplay.blit(pygame.image.load("images/speelveld.png"),(pygame.image.load("images/speelveld.png").get_rect()))     
            cnt = 0
            for i in chooseChars:
                if chooseChars[cnt].savePosition%40 == chooseChars[p%4].savePosition%40 and cnt is not p%4:
                    if chooseChars[0].savePosition%40 == chooseChars[1].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveRB),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[0].savePosition%40 == chooseChars[2].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveGrB),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[0].savePosition%40 == chooseChars[3].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveBG),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[1].savePosition%40 == chooseChars[2].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveGrR),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[1].savePosition%40 == chooseChars[3].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveRG),navigate[chooseChars[p%4].savePosition%40])
                    if chooseChars[2].savePosition%40 == chooseChars[3].savePosition%40:
                        gameDisplay.blit(pygame.image.load(gloveGrG),navigate[chooseChars[p%4].savePosition%40])
             
                else:
                    gameDisplay.blit(pygame.image.load(gloveSmall[cnt]),navigate[chooseChars[cnt].savePosition%40])  
                cnt += 1  
                
            small_glove(chooseChars[p%4].texture,(290,230))
            small_glove(chooseChars[0].texture,(110,110))
            small_glove(chooseChars[1].texture,(470,110))
            small_glove(chooseChars[2].texture,(470,470))
            small_glove(chooseChars[3].texture,(110,470))
            dice_img(roll)

     
    elif screen_index == 5:
        if save_game == True:
            saveGame(firstround,chooseChars,roll,p,screenlist, rectlist, crashed, menu_index, screen_index)
            screen_index = 3
        elif load_old_game == True:           
            firstround,chooseChars,roll,p,screenlist, rectlist, crashed, menu_index, screen_index = loadGame()
            print(chooseChars[1])
            screen_index = 3

    # for x in chooseChars:          #   remove player if he is dead
    #     if x.hitPoints <= 0:
    #         chooseChars.alive = False
    #if list met dead == 3: change
    # if player alive == true   change    #   only 1 player so print win
    #     screen_update(winning_screen, winning_screen_rect)
    #     winning_pic(chooseChars[0].texture)
    #     text_pop('The winner is ' + chooseChars[0].name , black)
    #     for event in pygame.event.get():
    #         if event.key == pygame.K_ESCAPE:
    #             crashed = True
    #         elif event.key == pygame.K_TAB:
    #             screen_index = 2


    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()
