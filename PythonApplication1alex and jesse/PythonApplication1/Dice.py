﻿import random

def Trow_dice():
    diceList = [1,2,3,4,5,6]
    dice = random.choice(diceList)
   #### #dice = 10 #testing for corner
    diceImglist = ["Dice1.png","Dice2.png","Dice3.png","Dice4.png","Dice5.png","Dice6.png"]
    diceImg = diceImglist[dice-1]
    ######diceImg = diceImglist[0]#testing
    return dice,diceImg


#for i in range(6):
#    dice = Trow_dice()
#    diceImg = dice[1]
#    dice = dice[0]
#    print (dice)
#    print (diceImg)
    
##functie Trow_dice() opnieuw uitvoeren voor player B 
# DIT IS VOOR DE SPOTFIGHT !!! 
#attack_b= 0

#if dice == 1:
#    attack_b += player_b.dice1
#elif dice == 2:
#    attack_b += player_b.dice2
#elif dice == 3:
#    attack_b += player_b.dice3
#elif dice == 4:
#    attack_b += player_b.dice4
#elif dice == 5:
#    attack_b += player_b.dice5
#elif dice == 6:
#    attack_b += player_b.dice6

#attack_a= 0

#if dice == 1:
#    attack_a += player_a.dice1
#elif dice == 2:
#    attack_a += player_a.dice2
#elif dice == 3:
#    attack_a += player_a.dice3
#elif dice == 4:
#    attack_a += player_a.dice4
#elif dice == 5:
#    attack_a += player_a.dice5
#elif dice == 6:
#    attack_a += player_a.dice6



#attack_a.conditionPoints -= 3 
#attack_b.conditionPoints -= 3

#if player_a.conditionPoints > -1 and player_b.conditionPoints > -1:
#    if attack_a => attack_b:
#        totalattack = attack_a - attack_b
#        player_b.hitPoints -= totalattack
#    else: 
#        totalattack = attack_b - attack_a
#        player_a.hitPoints -= totalattack
#elif player_a.condi/////// 
#    player_b.hitPoints -= attack_a
#elif player_a.conditionPoints < 0 and player_b.conditionPoints > -1:
#    player_a.hitPoints -= attack_a


# DIT IS VOOR DE CORNERFIGHT!!! attack a = defender  attack b = attacker 


#attack_b= 2

#if dice == 1:
#    attack_b += player_b.dice1
#elif dice == 2:
#    attack_b += player_b.dice2
#elif dice == 3:
#    attack_b += player_b.dice3
#elif dice == 4:
#    attack_b += player_b.dice4
#elif dice == 5:
#    attack_b += player_b.dice5
#elif dice == 6:
#    attack_b += player_b.dice6

#attack_a= 0

#if dice == 1:
#    attack_a += player_a.dice1
#elif dice == 2:
#    attack_a += player_a.dice2
#elif dice == 3:
#    attack_a += player_a.dice3
#elif dice == 4:
#    attack_a += player_a.dice4
#elif dice == 5:
#    attack_a += player_a.dice5
#elif dice == 6:
#    attack_a += player_a.dice6



#attack_a.conditionPoints -= 3 
#attack_b.conditionPoints -= 3

#if player_a.conditionPoints > -1 and player_b.conditionPoints > -1:
#    if attack_a => attack_b:
#        totalattack = attack_a - attack_b
#        player_b.hitPoints -= totalattack
#    else: 
#        totalattack = attack_b - attack_a
#        player_a.hitPoints -= totalattack
#elif player_a.conditionPoints > -1 and player_b.conditionPoints < 0:
#    player_b.hitPoints -= attack_a
#elif player_a.conditionPoints < 0 and player_b.conditionPoints > -1:
#    player_a.hitPoints -= attack_a

#DIT IS VOOR DE FIGHT TILE 

#attack_b= 0

#if dice == 1:
#    attack_b += player_b.dice1
#elif dice == 2:
#    attack_b += player_b.dice2
#elif dice == 3:
#    attack_b += player_b.dice3
#elif dice == 4:
#    attack_b += player_b.dice4
#elif dice == 5:
#    attack_b += player_b.dice5
#elif dice == 6:
#    attack_b += player_b.dice6

#attack_a= 0

#if dice == 1:
#    attack_a += player_a.dice1
#elif dice == 2:
#    attack_a += player_a.dice2
#elif dice == 3:
#    attack_a += player_a.dice3
#elif dice == 4:
#    attack_a += player_a.dice4
#elif dice == 5:
#    attack_a += player_a.dice5
#elif dice == 6:
#    attack_a += player_a.dice6



#attack_a.conditionPoints -= 3 
#attack_b.conditionPoints -= 3

#if player_a.conditionPoints > -1 and player_b.conditionPoints > -1:
#    if attack_a => attack_b:
#        totalattack = attack_a - attack_b
#        player_b.hitPoints -= totalattack
#    else: 
#        totalattack = attack_b - attack_a
#        player_a.hitPoints -= totalattack
#elif player_a.conditionPoints > -1 and player_b.conditionPoints < 0:
#    player_b.hitPoints -= attack_a
#elif player_a.conditionPoints < 0 and player_b.conditionPoints > -1:
#    player_a.hitPoints -= attack_a




#======================================================================================#
#tempChar = attacker #attacker
#chooseChar[i] = defender #defender

#damageA = 2

#if dice == 1:
#    damageA += attacker.dice1
#elif dice == 2:
#    damageA += attacker.dice2
#elif dice == 3:
#    damageA += attacker.dice3
#elif dice == 4:
#    damageA += attacker.dice4
#elif dice == 5:
#    damageA += attacker.dice5
#elif dice == 6:
#    damageA += attacker.dice6

#damageD= 0

#if dice == 1:
#    damageD += defender.dice1
#elif dice == 2:
#    damageD += defender.dice2
#elif dice == 3:
#    damageD += defender.dice3
#elif dice == 4:
#    damageD += defender.dice4
#elif dice == 5:
#    damageD += defender.dice5
#elif dice == 6:
#    damageD += defender.dice6

#defender.conditionPoints -= 3 
#attacker.conditionPoints -= 3
#totalattack = 0 

#if defender.conditionPoints > -1 and attacker.conditionPoints > -1:
#    if damageD => damageA:
#        totalattack = damageD - damageA
#        attacker.hitPoints -= totalattack
#    else: 
#        totalattack = damageA - damageD
#        defender.hitPoints -= totalattack
#elif defender.conditionPoints > -1 and attacker.conditionPoints < 0:
#    attacker.hitPoints -= damageD
#elif defender.conditionPoints < 0 and attacker.conditionPoints > -1:
#    defender.hitPoints -= damageD