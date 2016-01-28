import pygame
import time
from Playerscreen import *
from Rulesscreen import *
from Gameboard import *
pygame.init()


#navi=[(575,20),(20,20),(575,590),(20,590)]
size = width, height = 650, 650
tile = 0
white = (255, 255, 255)
chooseChars = []
firstround = True

#playerList = [player1,player2,player3,player4]
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Survivor')
clock = pygame.time.Clock()

startup_screen = pygame.image.load("images/startscherm2.png")
rules_screen = pygame.image.load("images/rules.png")
character_screen = pygame.image.load("images/playermenu.png")
punch_sound = pygame.mixer.music.load("sounds/punch_sound.mp3")
TileShift = pygame.mixer.music.load("sounds/TileShift.mp3")
diceSound = pygame.mixer.music.load("sounds/dice.mp3")
big_glove = pygame.image.load("images/handschoen.png")
red_glove = pygame.image.load("images/red_handschoen.png")
green_glove = pygame.image.load("images/green_handschoen.png")
yellow_glove = pygame.image.load("images/yellow_handschoen.png")
blue_glove = pygame.image.load("images/blue_handschoen.png")
board_screen = pygame.image.load("images/speelveld.png")

# imgTerry = pygame.image.load("images/TerryCrews.png")
# imgJason = pygame.image.load("images/JasonStatham.png")
# imgWesley = pygame.image.load("images/WesleySniper.png")
# imgJet = pygame.image.load("images/JetRi.png")
# imgSteven = pygame.image.load("images/StevenSeagal.png")
# imgMario = pygame.image.load("images/SuperMario.png")
# imgJackie = pygame.image.load("images/JackieChan.png")
# imgChack = pygame.image.load("images/ChackNorris.png")


board_screen_rect = board_screen.get_rect()
startup_screen_rect = startup_screen.get_rect()                 #start at top left
rules_screen_rect = startup_screen.get_rect()
character_screen_rect = character_screen.get_rect()

screenlist = [startup_screen, rules_screen, character_screen, board_screen]
screen_index = 0

s_rect = startup_screen_rect
r_rect = rules_screen_rect
p_rect = character_screen_rect
b_rect = board_screen_rect
rectlist = [s_rect, r_rect, p_rect,b_rect]

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





def glove_update(button, screen_index):                   #geeft handschoen.png weer
    if screen_index == 0:           #standard vector
        gameDisplay.blit(big_glove,(button))
    elif screen_index == 2:
        gameDisplay.blit(big_glove,(button))



def character_glove(char_button):
    gameDisplay.blit(red_glove,(char_button))

def screen_update(screen,rect):
    gameDisplay.blit(screen,(rect))

def sound_play(punch_sound):
    pygame.mixer.music.play(0)

def StartScreen(screenlist, rectlist, screen_index, menu_index, crashed, punch_sound):

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
                sound_play(punch_sound)
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
                    crashed = True
                if menu_index == 1 and event.key == pygame.K_SPACE:
                    screen_index = 1
                if menu_index == 0 and event.key == pygame.K_SPACE:
                    screen_index = 2
    b = 0
    return screen, rect, button, screen_index, menu_index, crashed, b


while not crashed:
    
    if screen_index == 0:#start

        screen, rect, button, screen_index, menu_index, crashed, b = \
        StartScreen(screenlist, rectlist, screen_index, menu_index, crashed, punch_sound)
        screen_update(screen, rect)
        glove_update(button, screen_index)                         #hier word button meegegeven aan glove_update
 
    elif screen_index == 1:#rules

        screen, rect,screen_index, menu_index, crashed = \
        RulesScreen(screenlist, rectlist, screen_index, menu_index, crashed, b)
        screen_update(screen, rect)
        glove_update(button, screen_index)

    elif screen_index == 2:#character

        screen, rect ,crashed, button, menu_index, screen_index, b, char_button,character_index,chooseChars = \
        PlayerScreen(chooseChars,screenlist, rectlist, crashed, menu_index, screen_index,character_index,punch_sound)
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
        #hier moet Gameboard() komen
        firstround,chooseChars,roll,p,screenlist, rectlist, crashed, menu_index, screen_index = \
        BoardScreen(firstround,chooseChars,roll, p,screenlist, rectlist, crashed, menu_index, screen_index)
        size = width, height = 650, 746
        gameDisplay = pygame.display.set_mode(size)
        gameDisplay.blit(pygame.image.load("images/speelveld.png"),(pygame.image.load("images/speelveld.png").get_rect()))    
        small_glove(gloveSmall1,navigate[chooseChars[0].savePosition%40])
        small_glove(gloveSmall2,navigate[chooseChars[1].savePosition%40])
        small_glove(gloveSmall3,navigate[chooseChars[2].savePosition%40])
        small_glove(gloveSmall4,navigate[chooseChars[3].savePosition%40])
        small_glove(chooseChars[p%4].texture,(290,230))
        small_glove(chooseChars[0].texture,(110,110))
        small_glove(chooseChars[1].texture,(470,110))
        small_glove(chooseChars[2].texture,(470,470))
        small_glove(chooseChars[3].texture,(110,470))
        dice_img(roll)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
