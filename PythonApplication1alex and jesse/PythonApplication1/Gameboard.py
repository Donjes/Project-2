import pygame
import time
from Dice import *
import os
from Character import *
from Playerscreen import *

#======================================= Variable die vanuit player screen moeten komen

size = width, height = 700, 650
white = (255, 255, 255)
gloveSmall2 = "images/red_handschoen.png"
gloveSmall2move = "images/red_handschoen1.png"
gloveSmall1 = "images/blue_handschoen.png"
gloveSmall1move = "images/blue_handschoen1.png"
gloveSmall3 = "images/green_handschoen.png"
gloveSmall3move = "images/green_handschoen1.png"
gloveSmall4 = "images/yellow_handschoen.png"
gloveSmall4move = "images/yellow_handschoen1.png"
gloveSmall = [gloveSmall1,gloveSmall2,gloveSmall3,gloveSmall4]

gloveBG = "images/zelfde_tile/blauwVSgeel.png"
gloveRB = "images/zelfde_tile/roodVSblauw.png"
gloveRG = "images/zelfde_tile/roodVSgeel.png"
gloveGrB = "images/zelfde_tile/groenVSblauw.png"
gloveGrR = "images/zelfde_tile/groenVSrood.png"
gloveGrG = "images/zelfde_tile/groenVSgeel.png"
smallGlove = [gloveSmall1,gloveSmall2,gloveSmall3,gloveSmall4]
smallGlovemove =[gloveSmall1move,gloveSmall2move,gloveSmall3move,gloveSmall4move]
#=======================================================================================
pygame.font.init()
size = width, height = 750, 780
gameDisplay = pygame.display.set_mode(size)
fonttype = pygame.font.SysFont('system', 50)
roll = Throw_dice()

# ======================================== DRAW FUNCTIE VOOR SPELER OP BOARD EN HANDSCHOENEN NAVI
def Draw_navi(chooseChars): 
    cnt = 0
    x = len(chooseChars)
    fonttype = pygame.font.SysFont('system', 30) #font grote en type
    text_pop(fonttype,"HP:"+ str(chooseChars[0].hitPoints), white,[198, 135]) #hitpoints speler 1
    text_pop(fonttype,"Condition:"+ str(chooseChars[0].conditionPoints), white,[173, 165]) #condition speler 1
    small_glove(chooseChars[0].texture,(110,110)) #mugshot player 1
    text_pop(fonttype,"HP:"+ str(chooseChars[1].hitPoints), white,[370, 135]) #hitpoints speler 2
    text_pop(fonttype,"Condition:"+ str(chooseChars[1].conditionPoints), white,[345, 165]) #condition speler 2
    small_glove(chooseChars[1].texture,(470,110)) #mugshot player 2
    text_pop(fonttype,"HP:"+ str(chooseChars[2].hitPoints), white,[370, 448]) #hitpoints speler 3
    text_pop(fonttype,"Condition:"+ str(chooseChars[2].conditionPoints), white,[173, 479]) #condition speler 3
    small_glove(chooseChars[2].texture,(470,470)) #mugshot player 3
    text_pop(fonttype,"HP:"+ str(chooseChars[3].hitPoints), white,[198, 448]) #hitpoints speler 4
    text_pop(fonttype,"Condition:"+ str(chooseChars[3].conditionPoints), white,[345, 479]) #condition speler 4
    small_glove(chooseChars[3].texture,(110,470))  #mugshot player 4
    for i in range(x): #hier word de img bepaald of spelers op zelfde tile staan of dat ze alleen staan
      if cnt == 0:
        if   chooseChars[0].savePosition%40 == chooseChars[1].savePosition%40:
            small_glove("images/zelfde_tile/roodVSblauw.png",navigate[chooseChars[0].savePosition%40])
        elif   chooseChars[0].savePosition%40 == chooseChars[2].savePosition%40:
            small_glove("images/zelfde_tile/groenVSblauw.png",navigate[chooseChars[0].savePosition%40])
        elif   chooseChars[0].savePosition%40 == chooseChars[3].savePosition%40:
            small_glove("images/zelfde_tile/blauwVSgeel.png",navigate[chooseChars[0].savePosition%40])
        else:
            small_glove(gloveSmall1,navigate[chooseChars[0].savePosition%40]) 
      if cnt == 1:
        if   chooseChars[1].savePosition%40 == chooseChars[0].savePosition%40:
            small_glove("images/zelfde_tile/roodVSblauw.png",navigate[chooseChars[1].savePosition%40])
        elif   chooseChars[1].savePosition%40 == chooseChars[2].savePosition%40:
            small_glove("images/zelfde_tile/groenVSrood.png",navigate[chooseChars[1].savePosition%40])
        elif   chooseChars[1].savePosition%40 == chooseChars[3].savePosition%40:
            small_glove("images/zelfde_tile/roodVSgeel.png",navigate[chooseChars[1].savePosition%40])
        else:
            small_glove(gloveSmall2,navigate[chooseChars[1].savePosition%40]) 
      if cnt == 2:
        if   chooseChars[2].savePosition%40 == chooseChars[0].savePosition%40:
            small_glove("images/zelfde_tile/groenVSblauw.png",navigate[chooseChars[2].savePosition%40])
        elif   chooseChars[2].savePosition%40 == chooseChars[1].savePosition%40:
            small_glove("images/zelfde_tile/groenVSrood.png",navigate[chooseChars[2].savePosition%40])
        elif   chooseChars[2].savePosition%40 == chooseChars[3].savePosition%40:
            small_glove("images/zelfde_tile/groenVSgeel.png",navigate[chooseChars[2].savePosition%40])
        else:
            small_glove(gloveSmall3,navigate[chooseChars[2].savePosition%40]) 
      if cnt == 3:    
        if   chooseChars[3].savePosition%40 == chooseChars[0].savePosition%40:
            small_glove("images/zelfde_tile/blauwVSgeel.png",navigate[chooseChars[3].savePosition%40])
        elif   chooseChars[3].savePosition%40 == chooseChars[1].savePosition%40:
            small_glove("images/zelfde_tile/roodVSgeel.png",navigate[chooseChars[3].savePosition%40])
        elif   chooseChars[3].savePosition%40 == chooseChars[2].savePosition%40:
            small_glove("images/zelfde_tile/groenVSgeel.png",navigate[chooseChars[3].savePosition%40])
        else:
            small_glove(gloveSmall4,navigate[chooseChars[3].savePosition%40]) 
      cnt += 1


def small_glove(gloveSmall,navilist):                  # handschoen DRAW functie    
        gameDisplay.blit(pygame.image.load(gloveSmall),navilist)
def dice_img(roll):                                    # the dice DRAW functie
        gameDisplay.blit(pygame.image.load("images/" + roll[1]),(300,300))
def text_pop(fonttype,msg, color,location):            # text DRAW functie
    screen_text = fonttype.render(msg, True, color)
    gameDisplay.blit(screen_text, location)
# list van Tile lokaties
navigate = [(20,20),(80,20),(130,20),(180,20),(230,20),(300,20),(375,20),(425,20),(472,20),(520,20),(575,20),(575,85),(575,130),(575,180),(575,230),(575,300),(575,373),(575,425),(575,475),(575,525),(575,590),(520,590),(472,590),(425,590),(375,590),(300,590),(230,590),(180,590),(130,590),(80,590),(20,590),(20,525),(20,475),(20,425),(20,373),(20,300),(20,230),(20,180),(20,130),(20,85)]



#=================================================== NAVIGATIE FUNCTIE! ===========================================================================#
def BoardScreen(firstround, chooseChars,roll,p,screenlist, rectlist, crashed, menu_index, screen_index,last_page,letsSuperFight,letsFight,nextturn,tempTile,newLocation,dice_rolled, prevPositie):
    save_game = False
    load_old_game = False
    if firstround: #eerst ronde en restart creert start lokatie spelers
        chooseChars[0].savePosition = chooseChars[0].startCorner
        chooseChars[1].savePosition = chooseChars[1].startCorner
        chooseChars[2].savePosition = chooseChars[2].startCorner
        chooseChars[3].savePosition = chooseChars[3].startCorner
        firstround = False
    corner = [0,10,20,30] #lijst(van hoeken) komt van pas om te kijken of iemand in een corner staat
    player = chooseChars[p%4] #player vertegenwordigt de current speler
    tile = player.savePosition
# =========================================== Navigatie van de handschoenen bij elke dice throw optie om kant te kiezen
    event = pygame.event.poll()     
    if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_SPACE and newLocation == False and dice_rolled == False: 
            Sounds.Dice()
            roll = Throw_dice() 
            for i in range(1):#15 doen
                rolling = Throw_dice()
                dice_img(rolling) 
                small_glove("images/DiceRolling.png",(300,300)) 
                pygame.display.update()
                time.sleep(0.1)
                if i == 0:#14 doen
                    dice_img(roll)
            time.sleep(0.5)
            pygame.display.update()
            time.sleep(0.5)      
            dice_rolled = True
        if event.key == pygame.K_UP and dice_rolled == True: #laat zien waar je heen loopt bij UP
            for i in range(roll[0]):                   
                tile += 1 
                small_glove(smallGlovemove[p%4],navigate[tile%40])    
                Sounds.Tile()
                pygame.display.update()
                time.sleep(0.1)
                print("plus")  
            tempTile = tile
            newLocation = True
        if event.key == pygame.K_DOWN and dice_rolled == True: #laat zien waar je heen loopt bij DOWN
            for i in range(roll[0]):                   
                tile -= 1 
                small_glove(smallGlovemove[p%4],navigate[tile%40])    
                Sounds.Tile()
                pygame.display.update()
                time.sleep(0.1)
                print("plus")  
            tempTile = tile
            newLocation = True
# =========================================== Navigatie van de handschoenen bij space kies je je lokatie en worden alle variable returned
        if event.key == pygame.K_SPACE and tempTile != chooseChars[p%4].savePosition and newLocation == True:
            chooseChars[p%4].savePosition = tempTile
            prevPositie = chooseChars[p%4].savePosition%40
            if chooseChars[p%4].savePosition%40 == chooseChars[p%4].startCorner:
                chooseChars[p%4].conditionPoints = 15
            # bij corner fight van een tegenstander word the spotfight tussen 2 mensen negeert. Dit is bug
            if chooseChars[p%4].alive == True and (prevPositie == chooseChars[(p%4)-1].savePosition or prevPositie == chooseChars[(p%4)-2].savePosition or prevPositie == chooseChars[(p%4)-3].savePosition) and letsSuperFight == 0:
                Sounds.Fightsound()
                letsFight = 1#spot fight

            elif chooseChars[p%4].alive == True and ( prevPositie == 0 or prevPositie == 10 or prevPositie == 20 or prevPositie == 30 )and not prevPositie == chooseChars[p%4].startCorner and letsFight == 0:
                Sounds.Fightsound()
                letsSuperFight = 1#corner fight

            elif letsSuperFight == 0 and letsFight == 0:
                nextturn = 1
            p += 1
            newLocation = False
            dice_rolled = False
        elif event.key == pygame.K_ESCAPE:
            crashed = True
        elif event.key == pygame.K_o:
            screen_index = 4
            last_page = 3
        elif event.key == pygame.K_TAB:
            firstround = True
            for i in range(4):
                chooseChars[i].hitPoints = 100
                chooseChars[i].conditionPoints= 15
                chooseChars[i].alive = True
                p = 0


    return firstround,chooseChars,roll,p,screenlist, rectlist, crashed, menu_index, screen_index,last_page,letsSuperFight,letsFight,nextturn,tempTile,newLocation,dice_rolled, prevPositie

#===================================================== FIGHT FUNCTIES! =============================================================================#


#spot fight
def spotFight(tempChar, chooseChars, prevPositie, navigate, roller1,roller2,roller_reset,roller1_img,roller2_img, roll, roll2,damageA, damageD, attacker, defender,p):
        
        for i in range(4):
            
            if prevPositie == chooseChars[i%4].savePosition and not chooseChars[(p%4)-1] == chooseChars[i%4]:#player is de index
                defender = chooseChars[i%4]

                attacker = chooseChars[(p%4)-1]
                print(str(attacker.playerName) + ' asd' + str(defender.playerName))
                
                event = pygame.event.poll()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:#attacker
                        Sounds.Dice()
                        roll = Throw_dice()
                        roller1_img = roll[1]
                        roller1 = True     
                        
                                     
                        if roll[0] == 1:
                            
                           damageA = attacker.dice1 
                        elif roll[0] == 2:
                           damageA = attacker.dice2 
                        elif roll[0] == 3:
                           damageA = attacker.dice3 
                        elif roll[0] == 4:
                           damageA = attacker.dice4 
                        elif roll[0] == 5:
                           damageA = attacker.dice5 
                           print(str(damageA)+' foo')
                        elif roll[0] == 6:
                           damageA = attacker.dice6 

                    if event.key == pygame.K_RETURN:#defender
                        Sounds.Dice()
                        roll2 = Throw_dice()
                        roller2_img = roll2[1]
                        roller2 = True
                        if roll2[0] == 1:
                           damageD = defender.dice1
                        elif roll2[0] == 2:
                           damageD = defender.dice2
                        elif roll2[0] == 3:
                           damageD = defender.dice3
                        elif roll2[0] == 4:
                           damageD = defender.dice4
                        elif roll2[0] == 5:
                           damageD = defender.dice5
                           print(str(damageD)+' bla')
                        elif roll2[0] == 6:
                           damageD = defender.dice6
        
        if roller1 == True and roller2 == True:
            roller_reset = True

        return roller1,roller2,roller_reset,roller1_img,roller2_img, damageA, damageD, attacker, defender
 
# Corner fight
def cornerFight(tempChar, chooseChars, prevPositie, corner, roller1,roller2,roller_reset,roller1_img,roller2_img, roll, roll2,damageA, damageD, attacker, defender):
        
        for player in range(len(corner)):
            
            if prevPositie == corner[player]:#player is de index
                defender = chooseChars[player]
                attacker = tempChar

                
                event = pygame.event.poll()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:#attacker
                        Sounds.Dice()
                        roll = Throw_dice()
                        roller1_img = roll[1]
                        roller1 = True
                        extra = 2#2 extra dmg voor de attacker 
                        if roll[0] == 1:
                           damageA = attacker.dice1 + extra
                        elif roll[0] == 2:
                           damageA = attacker.dice2 + extra
                        elif roll[0] == 3:
                           damageA = attacker.dice3 + extra
                        elif roll[0] == 4:
                           damageA = attacker.dice4 + extra
                        elif roll[0] == 5:
                           damageA = attacker.dice5 + extra
                        elif roll[0] == 6:
                           damageA = attacker.dice6 + extra

                    if event.key == pygame.K_RETURN:#defender
                        Sounds.Dice()
                        roll2 = Throw_dice()
                        roller2_img = roll2[1]
                        roller2 = True
                        if roll2[0] == 1:
                           damageD = defender.dice1
                        elif roll2[0] == 2:
                           damageD = defender.dice2
                        elif roll2[0] == 3:
                           damageD = defender.dice3
                        elif roll2[0] == 4:
                           damageD = defender.dice4
                        elif roll2[0] == 5:
                           damageD = defender.dice5
                        elif roll2[0] == 6:
                           damageD = defender.dice6
        
        if roller1 == True and roller2 == True:
            roller_reset = True

        return roller1,roller2,roller_reset,roller1_img,roller2_img, damageA, damageD, attacker, defender

def calculation(defender,attacker, damageA, damageD, totalattack, x,playerLoses):
    defender.conditionPoints -= x
    attacker.conditionPoints -= x

    if attacker.conditionPoints < 0:
        attacker.conditionPoints = 0
    if defender.conditionPoints < 0:
        defender.conditionPoints = 0

    if defender.conditionPoints > 0 and attacker.conditionPoints > 0:#hoger dan 0
       if damageD > damageA:
           totalattack = damageD - damageA
           attacker.getDamage(totalattack)
           playerLoses = 1
       elif damageA > damageD:
           totalattack = damageA - damageD
           defender.getDamage(totalattack)
           playerLoses = 2
       else:
           attacker.getDamage(15)
           defender.getDamage(15)
    elif defender.conditionPoints > 0 and attacker.conditionPoints == 0:
       attacker.getDamage(damageD)
    elif defender.conditionPoints == 0 and attacker.conditionPoints > 0:
       defender.getDamage(damageA) 
    elif defender.conditionPoints == 0 and attacker.conditionPoints == 0:
        if damageD > damageA:
            attacker.getDamage(damageD)
        elif damageA > damageD:
            defender.getDamage(damageA)
        else:
           attacker.getDamage(10)
           defender.getDamage(10)

    return defender, attacker,playerLoses,totalattack

